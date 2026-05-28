from pydantic import BaseModel

class AttendCreate(BaseModel):
    student_id: int
    attend : int
    late : int
    absent : int
    early_leave : int

class AttendResponse(BaseModel):
    id : int
    student_id : int
    student_name : str
    attend : int
    late : int
    absent : int
    early_leave : int
    total_days : int
    attendance_rate : float