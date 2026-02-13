from fastapi import APIRouter, Body
from models import Task

task_router =  APIRouter()
task_list : list[Task]= []

@task_router.get("/")
def get():
  return {'task': task_list}

@task_router.post("/")
def add(task: Task):
  task_list.append(task)
  return {'task': task_list}

@task_router.put("/{id}")
def update(id: int, task: Task):
    for index, li_task in enumerate(task_list):
        if li_task.id == id:
            task_list[index] = task
            break
    return {"task": task_list}

@task_router.delete("/")
def delete( id: int):
  
  for i, lista in enumerate(task_list):
    if lista.id == id :
      del task_list[i]
      break

  return {'task': task_list}