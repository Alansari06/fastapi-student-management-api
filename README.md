
# Student Management API

A beginner-friendly REST API built using FastAPI and Pydantic.

## Features

- Welcome API
- Get all students
- Get a student by ID
- Create a new student
- Update student details
- Request data validation
- HTTP 404 error handling
- In-memory storage using a Python list

## Technologies Used

- Python
- FastAPI
- Pydantic
- Uvicorn

## Project Structure

```text
FastAPI-Student-Management-API/
├── app/
│   ├── __init__.py
│   └── main.py
├── venv/
├── .gitignore
├── README.md
└── requirements.txt
```

## Installation

1. Clone or download this repository.
2. Open the project folder in the terminal.
3. Create a virtual environment:

   ```bash
   python -m venv venv
   ```

4. Activate it on Windows PowerShell:

   ```powershell
   .\venv\Scripts\Activate.ps1
   ```

5. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Run the Application

```bash
python -m uvicorn app.main:app --reload
```

## API Documentation

Open the following URL in your browser:

http://127.0.0.1:8000/docs

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | / | Welcome message |
| GET | /students | Get all students |
| GET | /students/{student_id} | Get a student by ID |
| POST | /students | Create a student |
| PUT | /students/{student_id} | Update a student |

## Storage

Student records are stored in an in-memory Python list.
No database or ORM is used. Data changes are lost when the
application restarts.

## Author

Developed as a FastAPI practical assignment.
