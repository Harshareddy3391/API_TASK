from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session
from datetime import  date
from dependencies import get_db
from models import Interview

router=APIRouter(prefix="/interviews",tags=["Interviews"])


@router.get("/count")
def get_interview_count(interview_date:date,
                        db:Session=Depends(get_db)):
    count=db.query(Interview).filter(Interview.interview_date == interview_date).count()

    return {
        "date":interview_date,
        "interview_count":count
    }
