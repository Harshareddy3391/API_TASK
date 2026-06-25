from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from models import Candidate
from dependencies import get_db
router = APIRouter(
    prefix="/candidates",
    tags=["Candidates"]
)


@router.get("/id")
def get_candidate_id(name: str, db: Session = Depends(get_db)):

    candidate = db.query(Candidate).filter(
        Candidate.name == name
    ).first()

    if not candidate:
        raise HTTPException(
            status_code=404,
            detail="Candidate Not Found"
        )

    return {
        "candidate_id": candidate.id,
        "name": candidate.name
    }


@router.get("/skills/{skill}")
def get_candidates_by_skill(
    skill: str,
    db: Session = Depends(get_db)
):

    candidates = db.query(Candidate).filter(
        Candidate.skills.contains(skill)
    ).all()

    if not candidates:
        raise HTTPException(
            status_code=404,
            detail="No Candidates Found"
        )

    return candidates


@router.get("/{candidate_id}")
def get_candidate_details(
    candidate_id: int,
    db: Session = Depends(get_db)
):

    candidate = db.query(Candidate).filter(
        Candidate.id == candidate_id
    ).first()

    if not candidate:
        raise HTTPException(
            status_code=404,
            detail="Candidate Not Found"
        )

    return candidate


@router.get("/")
def get_all_candidates(
    db: Session = Depends(get_db)
):

    
    return db.query(Candidate).all()