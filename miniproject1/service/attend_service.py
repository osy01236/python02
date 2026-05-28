from fastapi import HTTPException
from sqlalchemy.orm import Session

from models.student import Student
from models.attend import Attend
from schemas.attend_schema import AttendCreate


def create_attend(attend: AttendCreate, db: Session):
    student = db.query(Student).filter(Student.id == attend.student_id).first()

    if student is None:
        raise HTTPException(status_code=404, detail="학생 정보를 찾을 수 없습니다.")

    new_attend = Attend(
        student_id=attend.student_id,
        attend=attend.attend,
        late=attend.late,
        absent=attend.absent,
        early_leave=attend.early_leave,
    )

    db.add(new_attend)
    db.commit()
    db.refresh(new_attend)

    return {"message": "출석 데이터가 등록되었습니다."}


def get_attend_list(db: Session):
    attend_list = db.query(Attend, Student).join(
        Student, Attend.student_id == Student.id
    ).all()

    results = []

    for attend, student in attend_list:
        total_days = (
            attend.attend
            + attend.late
            + attend.absent
            + attend.early_leave
        )

        attendance_rate = 0
        if total_days > 0:
            attendance_rate = round(attend.attend / total_days * 100, 2)

        results.append({
            "id": attend.id,
            "student_id": attend.student_id,
            "student_name": student.name,
            "attend": attend.attend,
            "late": attend.late,
            "absent": attend.absent,
            "early_leave": attend.early_leave,
            "total_days": total_days,
            "attendance_rate": attendance_rate,
        })

    return results