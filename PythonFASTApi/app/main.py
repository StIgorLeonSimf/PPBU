from typing import List
from urllib import request

from fastapi import FastAPI, HTTPException, Form, Request, Path
from pydantic import BaseModel, Field
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

# from dataclasses import dataclass


app = FastAPI()

templates = Jinja2Templates(directory="app/templates")
# return templates.TemplateResponse("index.html", {"request": request})

class Task(BaseModel):
    id: int
    title: str
    done: bool = False

tasks: List[Task] = []


class TaskCreate(BaseModel):
    title: str = Field(..., description="Title of the task",
                       min_length=1, max_length=100)

    done: bool = False


async def create_task_post(title: str = Form(...),
                           description: str = Form(None) ):
    pass




cities = [{'id': 1, 'city': "Moscow"},
          {'id': 2, 'city': "Piter"},
          {'id': 3, 'city': "Ufa"},
          ]

dict_cities = {i['id']: i for i in cities}




@app.get("/tasks", response_model=List[Task])
def get_tasks():
    return tasks


@app.post("/tasks", response_model=Task, status_code=201)
def create_task (task_data:TaskCreate):
    new_id = tasks[-1].id + 1 if tasks else 1
    new_task = Task(id=new_id, **task_data.model_dump())
    tasks.append(new_task)
    return new_task


@app.put("/tasks/{task_id}", response_model=Task)
def update_task(task_id:int, update_task:TaskCreate):
    for task in tasks:
        if task.id == task_id:
            task.title = update_task.title
            task.done = update_task.done
            return task
    raise HTTPException(404, "Task not found")

@app.delete("/tasks/{task_id}", status_code=204)
def delete_task(task_id:int):
    for index, task in enumerate(tasks):
        if task.id == task_id:
            tasks.pop(index)
            return
    raise HTTPException(status_code=404, detail="Task not found")


@app.get("/cities")
def read_root():
    return dict_cities


@app.get("/cities/{city_id}")
def read_root(city_id: int, q=None):
    if q:
        dict_cities[city_id]['qq'] = q
    return dict_cities[city_id]


@app.get("/")
def read_root():
    return {"Hello": "World"}





ITEMS = [
    {"name": "Book for Python", "price": 900},
    {"name": "Pen", "price": 50},
    {"name": "Notebook", "price": 120},
    {"name": "Description of Python", "price": 1500},
]

@app.get("/search", response_class=HTMLResponse)
def search(request: Request, q:str=''):
    results = ([item for item in ITEMS if q.lower() in item['name'].lower()]
               if q else [])
    return templates.TemplateResponse(
        request=request,
        name = 'search.html',
        context = {"q": q, "results": results},
    )