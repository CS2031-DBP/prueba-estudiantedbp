# Importamos las librerías necesarias
from fastapi.testclient import TestClient
import pytest
from homework import app  # Asegúrate de que la ruta a tu archivo sea correcta

# Creamos una instancia de TestClient
client = TestClient(app)

# Definimos las pruebas
def test_read_root():
    # Hacemos una petición GET al endpoint "/"
    response = client.get("/")
    # Verificamos que la respuesta sea 200 OK
    assert response.status_code == 200
    # Verificamos que el contenido de la respuesta sea el esperado
    assert response.json() == {"Hello": "World"}

def test_read_item():
    # Hacemos una petición GET al endpoint "/items/5"
    response = client.get("/items/5")
    # Verificamos que la respuesta sea 200 OKp
    assert response.status_code == 200
    # Verificamos que el contenido de la respuesta sea el esperado
    assert response.json() == {"item_id": 5}

# Para correr las pruebas ejecuta el siguiente comando
# pytest test.py