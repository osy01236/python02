from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from database.db import Base,engine
from routers import student_router
from routers import score_router
from routers import attend_router
from routers import analysis_router

from models import student
from models import attend
from schemas import student_schema

app =FastAPI()
Base.metadata.create_all(bind=engine)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials =True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(student_router.router)
app.include_router(score_router.router)
app.include_router(attend_router.router)
app.include_router(analysis_router.router)