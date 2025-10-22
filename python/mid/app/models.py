from pydantic import BaseModel

class Task(BaseModel):
    id: int | None = None
    title: str
    completed: bool = False