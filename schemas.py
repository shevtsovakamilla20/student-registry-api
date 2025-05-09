from pydantic import BaseModel

class StudentBase(BaseModel):
    first_name: str
    last_name: str
    email: str
    group: str
    average_grade: float

class StudentCreate(StudentBase):
    pass

class Student(StudentBase):
    id: int

    class Config:
        orm_mode = True