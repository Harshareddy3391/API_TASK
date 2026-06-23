from pydantic import BaseModel, EmailStr


class CandidateResponse(BaseModel):
    id: int
    name: str
    email: EmailStr
    phone: str
    skills: str
    experience: int

    class Config:
        from_attributes = True


class InterviewCountResponse(BaseModel):
    date: str
    interview_count: int


class RegisterSchema(BaseModel):
    name: str
    email: EmailStr
    phone: str
    password: str


class LoginSchema(BaseModel):
    email_or_phone: str
    password: str