from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def saludar():
  return { "saludo": "Hola mundo desde fastapi" }

@app.get('/post/{id}')
def add(id: int):
  return{ "id" : id}

@app.get('/post/{id}')
def add(id: int):
  return{ "id" : id}
