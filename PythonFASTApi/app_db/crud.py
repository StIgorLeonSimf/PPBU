from sqlalchemy.orm import Session
from . import models, schemas
from typing import Optional, List


def get_task(db: Session, task_id: int) -> Optional[models.Task]:
    return db.query(models.Task).filter(models.Task.id == task_id).first()


def get_tasks(db: Session, skip: int = 0, limit: int = 100) -> List[models.Task]:
    return db.query(models.Task).offset(skip).limit(limit).all()


def create_task(db: Session, task_in: schemas.TaskCreate) -> models.Task:
    task = models.Task(title=task_in.title, description=task_in.description)
    db.add(task)
    db.commit()
    db.refresh(task)
    return task


def update_task(db: Session, task: models.Task,
                task_in: schemas.TaskUpdate) -> models.Task:
    if task_in.title is not None:
        task.title = task_in.title

    if task_in.description is not None:
        task.description = task_in.description

    if task_in.completed is not None:
        task.completed = task_in.completed

    db.add(task)
    db.commit()
    db.refresh(task)
    return task


def delete_task(db: Session, task: models.Task) -> None:
    db.delete(task)
    db.commit()




