from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from fastapi.requests import Request
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()

@app.exception_handler(HTTPException)
async def custom_http_exception_handler(request: Request, exc: HTTPException):
    return JSONResponse(status_code=exc.status_code, content={"error": exc.detail})

class Task(BaseModel):
    id: int
    title: str
    done: bool = False

class TaskCreate(BaseModel):
    title: Optional[str] = None

tasks: List[Task] = [
    Task(id=1, title="Buy milk", done=False),
    Task(id=2, title="Write README", done=False),
    Task(id=3, title="Learn FastAPI", done=True),
]
next_id = 4

@app.get("/")
def read_root():
    return {"name": "Task API", "version": "1.0", "endpoints": ["/tasks"]}

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.get("/tasks")
def get_tasks():
    return tasks

@app.get("/tasks/{task_id}")
def get_task(task_id: int):
    for t in tasks:
        if t.id == task_id:
            return t
    raise HTTPException(status_code=404, detail=f"Task {task_id} not found")

@app.post("/tasks", status_code=201)
def create_task(payload: TaskCreate):
    global next_id
    if not payload.title or not payload.title.strip():
        raise HTTPException(status_code=400, detail="title is required and cannot be empty")

    new_task = Task(id=next_id, title=payload.title, done=False)
    tasks.append(new_task)
    next_id += 1
    return new_task
