from fastapi import HTTPException
from models.student_model import StudentCreate, StudentUpdate

# In-memory storage: data disappears when the application restarts.
students = {}
next_student_id = 1


def create_student(student: StudentCreate):
    global next_student_id

    # Prevent duplicate email addresses.
    for existing_student in students.values():
        if existing_student["email"] == str(student.email):
            raise HTTPException(status_code=400, detail="A student with this email already exists")

    student_data = student.model_dump()
    student_data["email"] = str(student.email)
    student_data["id"] = next_student_id

    students[next_student_id] = student_data
    next_student_id += 1

    return student_data


def get_all_students():
    return list(students.values())


def get_student_by_id(student_id: int):
    student = students.get(student_id)
    if student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    return student


def update_student(student_id: int, student: StudentUpdate):
    if student_id not in students:
        raise HTTPException(status_code=404, detail="Student not found")

    for existing_id, existing_student in students.items():
        if existing_id != student_id and existing_student["email"] == str(student.email):
            raise HTTPException(status_code=400, detail="Another student already uses this email")

    updated_data = student.model_dump()
    updated_data["email"] = str(student.email)
    updated_data["id"] = student_id

    students[student_id] = updated_data
    return updated_data


def delete_student(student_id: int):
    if student_id not in students:
        raise HTTPException(status_code=404, detail="Student not found")

    del students[student_id]
    return
