from fastapi import FastAPI
from routers.candidate import router 
from database import engine,Base
from routers.interview import router as r2
#Table creation 
Base.metadata.create_all(bind=engine)
app = FastAPI(
    title="ATS API",
    version="1.0.0",
    description="Applicant Tracking System"
)


@app.get("/")
def home():
    return {"message": "ATS API Running"}



#api router
app.include_router(router)
app.include_router(r2)

 