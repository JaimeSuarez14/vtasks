from fastapi import FastAPI, APIRouter
from task import task_router

app = FastAPI()
router = APIRouter()

@router.get('/hello')
def saludar():
  return { "saludo": "Hola mundo desde fastapi" }

@router.get('/post/{id}')
def add(id: int):
  return{ "id" : id}


app.include_router(router)
app.include_router(task_router, prefix="/tasks")
