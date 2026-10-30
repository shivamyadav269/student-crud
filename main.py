from fastapi import FastAPI
from routes.student_routes import router as student_router

app = FastAPI(
    title="Student CRUD API",
    description="A simple FastAPI application to manage university student records.",
    version="1.0.0"
)

app.include_router(student_router)

@app.get("/")
def home():
    return {"message": "Welcome to the Student CRUD API", "docs": "/docs"}
