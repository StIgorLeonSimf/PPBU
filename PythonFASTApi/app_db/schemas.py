from pydantic import BaseModel
from typing import Optional


class TaskBase(BaseModel):
    title: str
    description: Optional[str] = None


class TaskCreate(TaskBase):
    pass


class TaskUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    completed: Optional[bool] = None


class TaskinDBBase(TaskBase):
    id: int
    completed: bool
    class Config:
        orm_mode = True


class TaskOut(TaskinDBBase):
    pass