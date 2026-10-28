from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from . import models, schemas, crud
from .db import SessionLocal, engine, Base
from typing import List

app = FastAPI(title='TaskAPI')

# Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/tasks/", response_model=schemas.TaskOut)
def create_task_endpoint(task_in:schemas.TaskCreate,
                         db: Session = Depends(get_db)):

    return crud.create_task(db=db, task_in=task_in)

@app.get("/tasks/", response_model=List[schemas.TaskOut])
def list_tasks(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_tasks(db=db, skip=skip, limit=limit)

@app.get("/tasks/{task_id}", response_model=schemas.TaskOut)
# async def read_task(task_id: int, db: Session = Depends(get_db)):
def read_task(task_id: int, db: Session = Depends(get_db)):
    task = crud.get_task(db=db, task_id=task_id)
    # task = await repository.get_task(db=db, task_id=task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

@app.patch("/tasks/{task_id}", response_model=schemas.TaskOut)
def update_task_endpoint(task_id: int, task_in: schemas.TaskUpdate,
                         db: Session = Depends(get_db)):
    task = crud.get_task(db=db, task_id=task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return crud.update_task(db=db, task=task, task_in=task_in )

@app.delete("/tasks/{task_id}", status_code=204)
def delete_task_endpoint(task_id: int, db: Session = Depends(get_db)):
    task = crud.get_task(db=db, task_id=task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    crud.delete_task(db=db, task=task)
    return None

