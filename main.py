
"""Simple task management API built with FastAPI.

This module demonstrates a minimal REST API using:
- FastAPI for routing and HTTP handling
- Pydantic for request validation
- an in-memory dictionary for local data storage

Best practices used here:
- Clear route naming and separation of concerns
- Request validation via a Pydantic model
- Explicit HTTP error handling for missing resources
- Simple, readable endpoints for learning and demos
"""

from typing import Optional

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

# Application metadata: useful for docs and API discovery.
app = FastAPI(
    title="Task Manager API",
    description="A simple FastAPI CRUD project",
    version="1.0.0",
)


class Task(BaseModel):
    """Schema for a task record.

    Best practice: keep the request model explicit so FastAPI validates
    incoming JSON automatically and returns 422 for invalid payloads.
    """

    title: str
    description: Optional[str] = None
    completed: bool = False


# In-memory database for demo purposes.
# Best practice: use a real database in production; this dictionary is fine
# for learning and local testing because data is reset when the app restarts.
tasks: dict[int, Task] = {}

# Simple auto-incrementing ID to mimic a database primary key.
task_id: int = 1


@app.get("/")
def home() -> dict[str, str]:
    """Health/info endpoint for the API root."""
    return {"message": "Welcome to Task Manager API"}


@app.get("/tasks")
def get_tasks() -> dict[int, Task]:
    """Return all stored tasks.

    Best practice: keep endpoint names descriptive and easy to understand.
    """
    return tasks


@app.post("/tasks")
def create_task(task: Task) -> dict[str, object]:
    """Create a new task and return it with its generated ID."""
    global task_id

    # Store the new task under the next available ID.
    tasks[task_id] = task

    # Return the created resource with the generated ID included.
    response = {"id": task_id, **task.model_dump()}
    task_id += 1
    return response


@app.get("/tasks/{id}")
def get_task(id: int) -> dict[str, object]:
    """Fetch a single task by its unique ID."""
    if id not in tasks:
        raise HTTPException(status_code=404, detail="Task not found")

    return {"id": id, **tasks[id].model_dump()}


@app.put("/tasks/{id}")
def update_task(id: int, task: Task) -> dict[str, object]:
    """Replace an existing task with the provided payload."""
    if id not in tasks:
        raise HTTPException(status_code=404, detail="Task not found")

    # Update the existing record in place.
    tasks[id] = task
    return {"id": id, **task.model_dump()}


@app.delete("/tasks/{id}")
def delete_task(id: int) -> dict[str, str]:
    """Delete a task by ID."""
    if id not in tasks:
        raise HTTPException(status_code=404, detail="Task not found")

    del tasks[id]
    return {"message": "Task deleted successfully"}
