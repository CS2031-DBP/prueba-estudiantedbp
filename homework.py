# Importamos la librería de fastapi

from fastapi import FastAPI

# Creamos una instancia de FastAPI con 2 endpoints basicos uno que diga hola mundo,

app = FastAPI()

@app.get("/items/{item_id}")
def read_item(item_id: int):
    return {"item_id": item_id}

# Para correr el servidor de fastapi ejecutamos el siguiente comando
# uvicorn homework:app --reload