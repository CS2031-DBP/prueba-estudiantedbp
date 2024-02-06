# Importamos la librería de fastapi

from fastapi import FastAPI

# Creamos una instancia de FastAPI con 2 endpoints basicos uno que diga hola mundo, otro que en base a el endpoint /items/{item_id} nos regrese el item_id

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int):
    return {"item_id": item_id}

# Para correr el servidor de fastapi ejecutamos el siguiente comando
# uvicorn homework:app --reload