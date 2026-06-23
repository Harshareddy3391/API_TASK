from fastapi import FastAPI 
from sqlalchemy.orm import Session

from models import Candidate

from dependencies import get_db
 