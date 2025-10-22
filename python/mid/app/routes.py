from fastapi import APIRouter, HTTPException
from app.models import Task
from app.database import tasks

router = APIRouter()

@router.get("/tasks")
def get_tasks():
    return tasks

@router.get("/tasks/{task_id}")
def get_task(task_id: int):
    return tasks[task_id]

@router.post("/tasks")
def create_task(task: Task):
    new_id = len(tasks)
    tasks.append({"id": new_id, "title": task.title, "completed": task.completed})
    return {"status": "ok", "task": task}

@router.put("/tasks/{task_id}")
def update_task(task_id: int, task: Task):
    tasks[task_id] = task.dict()
    return {"message": "updated"}

@router.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    del tasks[task_id]
    return "ok"