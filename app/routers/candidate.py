from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from models import Candidate
from dependencies import get_db

router = APIRouter(
    prefix="/candidates",
    tags=["Candidates"]
)



#get by id
@router.get("/id")
def get_candidate_id(
    name:str,
    db:Session=Depends(get_db)
):
    candidate=(db.query(Candidate).filter(Candidate.name==name).first())


    if not candidate:
        raise HTTPException(
            status_code=404,
            detail="Candidate Not Found..."

        )
    
    return {
        "candidate_id":Candidate.id,
        "name":candidate.name
    }



#get candidate datails by id

@router.get("/{candidate_id}")
def get_candidate_details(
    candidate_id:str,
    db:Session=Depends(get_db)
):
    candidate=(db.query(Candidate).filter(Candidate.id).first())

    if not candidate:
        raise HTTPException(
            status_code=404,
            detail="Candidate Not Found..."

        )
    
    return candidate
#get all candidates
@router.get("/")
def get_all_candidates(db:Session=Depends(get_db)):
    candidate=db.query(Candidate),all()

    return candidate


#get candidates by skill
@router.get("/skills/{skill}")
def get_all_candidates_by_skill(
    skill:str,
    db:Session=Depends(get_db)
    
    ):

    skill_candidate=(db.query(Candidate).filter(Candidate.skills.contains(skill)).all())

    if not skill_candidate:
        raise HTTPException(
            status_code=404,
            detail="No Candidates Found..."
        )