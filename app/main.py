
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, EmailStr

app = FastAPI()

class Student(BaseModel):
    name: str
    email: EmailStr
    course: str
    is_active: bool

students = [
    {"id": 1, "name": "Rahul Sharma", "email": "rahul@example.com", "course": "Python", "is_active": True},
    {"id": 2, "name": "Priya Verma", "email": "priya@example.com", "course": "FastAPI", "is_active": True},
    {"id": 3, "name": "Amit Kumar", "email": "amit@example.com", "course": "Django", "is_active": True},
    {"id": 4, "name": "Neha Singh", "email": "neha@example.com", "course": "Java", "is_active": False},
    {"id": 5, "name": "Arjun Mehta", "email": "arjun@example.com", "course": "Python", "is_active": True}
]


@app.get("/")
def home():
    return {
        "message": "Welcome to FastAPI",
        "application": "Student Management API",
        "status": "running"
    }


@app.get("/students")
def get_students():
    return students


@app.get("/students/{student_id}")
def get_student(student_id: int):
    for student in students:
        if student["id"] == student_id:
            return student

    raise HTTPException(status_code=404, detail="Student not found")


@app.post("/students", status_code=201)
def add_student(student: Student):
    new_id = 1

    for s in students:
        if s["id"] >= new_id:
            new_id = s["id"] + 1

    new_student = student.model_dump()
    new_student["id"] = new_id

    students.append(new_student)
    return new_student


@app.put("/students/{student_id}")
def update_student(student_id: int, updated_student: Student):
    for student in students:
        if student["id"] == student_id:
            student["name"] = updated_student.name
            student["email"] = updated_student.email
            student["course"] = updated_student.course
            student["is_active"] = updated_student.is_active

            return student

    raise HTTPException(status_code=404, detail="Student not found")
