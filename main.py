from fastapi.testclient import TestClient
from fastapi import FastAPI

app = FastAPI()

# activamos las rutas
@app.get("/")
async def read_main():
    return {"msg": "Hello World ROOT"}

@app.post("/test")
async def read_main():
    return {"msg": "Hello World Test"}

client = TestClient(app)

def test_read_main():
    response = client.get("/")
    assert response.status_code == 200

def test():
    response = client.post("/test")
    assert response.status_code == 200