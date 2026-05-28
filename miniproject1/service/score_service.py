from fastapi import HTTPException

from models.score import Score
from models.student import Student
from schemas.score_schema import ScoreResponse

from database.db import get_db
from sqlalchemy.orm import Session


def create_score_service(db, score):
    scoreData = [  score.python_score, score.numpy_score, 
                    score.pandas_score, score.java_score, score.project_score, ]
    
    subject = ("python", "numpy", "pandas", "java", "project")
    #점수 범위 검증
    for i, v in enumerate(scoreData):
        if v < 0 or v >100 :
            raise HTTPException(
                status_code=404,
                message= subject[i] + "점수는 0이상 100이하만 가능합니다."
            )

    student = db.query(Student).filter(Student.id == score.student_id).first()

    if student is None :
        raise HTTPException(
            status_code=404,
            message="학생 정보를 찾을 수 없습니다."
        )
    new_score = Score(
        student_id = score.student_id,
        python_score = score.python_score,
        numpy_score = score.numpy_score,
        pandas_score = score.pandas_score,
        java_score = score.java_score,
        project_score = score.project_score
    )

    db.add(new_score)
    db.commit()
    db.refresh(new_score)
    return new_score





def get_score_list(db):
    scores_list = db.query(Score, Student).join(
        Student, Score.student_id == Student.id
    ).all()

    result = []

    for score, std in scores_list:
        total_score = (
            score.python_score
            + score.numpy_score
            + score.pandas_score
            + score.java_score
            + score.project_score
        )
        avg_score = total_score / 5

        result.append( ScoreResponse(
            id=score.id,
            student_id=std.id,
            student_name=std.name,
            python_score=score.python_score,
            numpy_score=score.numpy_score,
            pandas_score=score.pandas_score,
            java_score=score.java_score,
            project_score=score.project_score,
            total_score=total_score,
            avg_score=avg_score,
            create_at=score.create_at
        ))

    return result


