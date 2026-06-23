from sqlalchemy import Column,Integer,String,Date,Time,ForeignKey 
from database import Base

class Candidate(Base):
    __tablename__="candidates"
    id=Column(Integer,primary_key=True,index=True)
    name=Column(String(200),nullable=False)
    email=Column(String(100))
    phone=Column(String(20))
    skills=Column(String(300))
    experience=Column(Integer)




class Interview(Base):

    __tablename__="interview"
    id=Column(Integer,primary_key=True,index=True)
    Candidate_id=Column(Integer,ForeignKey=Candidate.id)
    Interview_date=Column(Date)
    Interview_time=Column(Time)
