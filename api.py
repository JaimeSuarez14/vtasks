from fastapi import FastAPI, APIRouter, Query
from task import task_router

app = FastAPI()
router = APIRouter()

@router.get('/hello')
def saludar():
  return { "saludo": "Hola mundo desde fastapi" }

@router.get('/post/{id}')
def add(id: int, page: int =Query(1, gt=1, lt=20)):
  return{ "id" : id, "page": page}


app.include_router(router)
app.include_router(task_router, prefix="/tasks")
