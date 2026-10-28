from typing import List
from urllib import request

from fastapi import FastAPI, HTTPException, Form, Request, Path
from pydantic import BaseModel, Field
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse


app = FastAPI()
templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
def show_login_form(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="form.html",
    )

@app.post("/login", response_class=HTMLResponse)
def process_login(request: Request,
                  username: str = Form(...),
                  password: str = Form(..., min_length=8)):
    if username == "admin" and password == "secret_service":
        message = f"Welcome {username}!"
        color = 'green'
    else:
        message = f"DATA not found!"
        color = 'red'

    return templates.TemplateResponse(
        request=request,
        name="form.html",
        context={'message': message, 'color': color},
    )


@app.get("/survey", response_class=HTMLResponse)
def show_survey(request: Request):
    questions = ['Ваше имя', 'Ваш возраст','Ваш город']
    return templates.TemplateResponse(
        request=request,
        name="survey.html",
        context={'questions': questions}
    )
