from sqlalchemy import Column, Integer, String, Float
from database import Base

class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String)
    last_name = Column(String)
    email = Column(String, unique=True)
    group = Column(String)
    average_grade = Column(Float)