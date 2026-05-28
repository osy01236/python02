from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database.db import get_db
from schemas.attend_schema import AttendCreate
from service import attend_service

router = APIRouter()


@router.post("/attend")
def create_attend(attend: AttendCreate, db: Session = Depends(get_db)):
    return attend_service.create_attend(attend, db)


@router.get("/attend")
def get_attend_list(db: Session = Depends(get_db)):
    return attend_service.get_attend_list(db)