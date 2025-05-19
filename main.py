# This file will teach you basic about the Flask_api and you will build a basic app.

"""
API interact with four method.
CRUD

CREAT
    -> POST - to create something, teliing the system to create
    
READ
    -> GET - to ask something from api.
    
UPDATE
    -> PUT - To update something in data.
    
DELETE
    -> DELETE - to delete the data.
    
json is used to parsed data.
    made of object similar to dict
    array - list

FastAPI
    - convert python object to and from json
    - validate different requewts
    - ensure the correct data is provided

"""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import List, Optional, Dict
from uuid import UUID, uuid4


app = FastAPI()

# class Task(BaseModel):
#     id: UUID = None
#     title: str
#     description: Optional[str] = None
#     completed: bool = False

class Task(BaseModel):
    title: str
    description: Optional[str] = None
    completed: Optional[bool] = False
    
tasks = {}

@app.post("/task/", response_model=Task)
def creat_task(task: Task):
    id = uuid4()
    tasks[id] = task
    return tasks[id]

@app.get("/tasks/", response_model=Dict[UUID, Task])
def read_tasks():
    return tasks

@app.get("/tasks/{task_id}", response_model=Task)
def read_task(task_id: UUID):
    if task_id in tasks:
        return tasks[task_id]
    
    raise HTTPException(status_code=404, detail="Task not found")

@app.put("/task/{task_id}", response_model=Task)
def update_task(task_id: UUID, task_update: Task):
    if task_id in tasks:
        tasks[task_id].update(task_update)
        return tasks[task_id]
    
    raise HTTPException(status_code=404, detail="Task not found")

@app.delete("/tasks/{task_id}", response_model=Task)
def delete_task(task_id: UUID):
    if task_id in tasks:
        tasks.pop(task_id)
    
    raise HTTPException(status_code=404, detail="Task not found")

if __name__ == "__main__":
    import uvicorn
    
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)