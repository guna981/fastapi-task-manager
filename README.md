# FastAPI Task Manager API

A lightweight FastAPI application for managing tasks with CRUD operations. This project demonstrates a simple REST API using FastAPI, Pydantic models, and in-memory storage.

## Features

- Create a new task
- List all tasks
- Retrieve a single task by ID
- Update an existing task
- Delete a task
- Automatic API documentation via FastAPI Swagger UI and ReDoc
- In-memory persistence for quick local testing

## Tech Stack

- Python 3.x
- FastAPI
- Uvicorn
- Pydantic

## Project Structure

```text
fastapi-expense-tracker/
├── main.py
├── requirements.txt
├── README.md
├── .gitignore
└── venv/
```

## Prerequisites

Before running the project, ensure you have:

- Python 3.9 or later installed
- `pip` available for installing dependencies

## Installation

1. Clone the repository:

```bash
git clone <repository-url>
cd fastapi-expense-tracker
```

2. Create and activate a virtual environment:

```bash
python -m venv venv
```

On Windows:

```bash
venv\Scripts\activate
```

On macOS/Linux:

```bash
source venv/bin/activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

## Running the Application

Start the FastAPI development server using Uvicorn:

```bash
uvicorn main:app --reload
```

Then open:

- http://127.0.0.1:8000
- http://127.0.0.1:8000/docs for Swagger UI
- http://127.0.0.1:8000/redoc for ReDoc

## API Endpoints

### Root

```http
GET /
```

Returns a welcome message.

### Get all tasks

```http
GET /tasks
```

Returns all tasks currently stored in memory.

### Create a task

```http
POST /tasks
```

Request body:

```json
{
  "title": "Buy groceries",
  "description": "Milk, bread, and eggs",
  "completed": false
}
```

### Get a single task

```http
GET /tasks/{id}
```

Returns the task with the specified ID.

### Update a task

```http
PUT /tasks/{id}
```

Request body example:

```json
{
  "title": "Buy groceries",
  "description": "Milk, bread, eggs, and fruit",
  "completed": true
}
```

### Delete a task

```http
DELETE /tasks/{id}
```

Deletes a task by ID.

## Example Task Model

```json
{
  "title": "Finish project report",
  "description": "Prepare the final summary for review",
  "completed": false
}
```

## Notes

- Data is stored in memory only, so tasks are lost when the server restarts.
- This project is ideal for learning FastAPI basics, CRUD endpoints, and request validation using Pydantic.

## License

This project is provided for educational use and does not include a formal license file.
