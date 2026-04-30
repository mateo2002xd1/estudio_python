from tests.conftest import client

def test_crear_usuario(client):
    response = client.post("/api/usuarios/", json={
        "id": 1001577455,
        "edad": 25,
        "nombre": "mateo"
        })
    assert response.status_code == 200

def test_registro_usuario(client):
    response = client.patch("/auth/usuarios/1001577455/registro/", json={
        "password": "1234"
        })
    assert response.status_code == 200

def test_login_usuario(client):
    response = client.post("/auth/usuarios/1001577451/login/", json={
        "password": "123a"
        })
    assert response.status_code == 200