from pydantic import BaseModel, EmailStr, Field


class StudentCreate(BaseModel):
    name: str = Field(..., min_length=2, max_length=100)
    email: EmailStr
    course: str = Field(..., min_length=2, max_length=100)
    semester: int = Field(..., ge=1, le=12)


class StudentUpdate(StudentCreate):
    pass


class StudentResponse(StudentCreate):
    id: int
