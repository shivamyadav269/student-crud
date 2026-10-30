# FastAPI Student CRUD Application

A university assignment implementing a REST API for managing student records using FastAPI.

## Features
- Create a student
- Read all students
- Read a student by ID
- Update a student
- Delete a student
- Pydantic request validation
- In-memory Python dictionary storage (no database)

## Project structure
```text
student-crud/
├── main.py
├── models/
│   └── student_model.py
├── routes/
│   └── student_routes.py
├── controllers/
│   └── student_controller.py
└── requirements.txt
```

## Setup
Create and activate a virtual environment (recommended), then install dependencies:

```bash
python -m venv venv
```

Windows:
```bash
venv\Scripts\activate
```

Install packages:
```bash
pip install -r requirements.txt
```

## Run
From the `student-crud` project directory:

```bash
uvicorn main:app --reload
```

Open Swagger UI at http://127.0.0.1:8000/docs.

## Important
Student records are stored in memory and will be cleared whenever the application restarts.
