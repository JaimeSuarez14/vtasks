from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def saludar():
  return { "saludo": "Hola mundo desde fastapi" }

@app.get('/post/{id}')
def add(id: int):
  return{ "id" : id}

@app.post('/post/{id}')
def create(id: int):
  return{ "id" : id}

@app.put('/post/{id}')
def modificar(id: int):
  return{ "id" : id}

@app.patch('/post/{id}')
def modificarNombre(id: int):
  return{ "id" : id}

@app.delete('/post/{id}')
def eliminar(id: int):
  return{ "id" : id}