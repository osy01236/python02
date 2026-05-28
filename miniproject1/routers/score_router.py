from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database.db import get_db
from service.score_service import (get_score_list, create_score_service)
from schemas.score_schema import (ScoreCreate, ScoreResponse)

router = APIRouter()


#
@router.post("/scores")
def create_score(score: ScoreCreate, 
                 db: Session= Depends(get_db)):
    create_score_service(db, score)
    

  


#성적조회 
@router.get("/scores")
def get_scores(db: Session = Depends(get_db)):
    

    return get_score_list(db)