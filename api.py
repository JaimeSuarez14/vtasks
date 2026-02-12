from fastapi import FastAPI, APIRouter

app = FastAPI()
router = APIRouter()

@router.get('/')
def saludar():
  return { "saludo": "Hola mundo desde fastapi" }

@router.get('/post/{id}')
def add(id: int):
  return{ "id" : id}


app.include_router(router)
