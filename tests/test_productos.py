from tests.conftest import client

def test_buscar_productos(client):
    response = client.get("api/productos/")

    assert response.status_code == 200

def test_insertar_productos(client):
    login = client.post("/auth/usuarios/1001577451/login/", json={
        "password": "123a"
        })

    token = login.json()["access_token"]

    response = client.post("api/productos/", json={
        "codigo": 13,
        "nombre": "materero",
        "precio": 1
        },
        headers={"Authorization": f"Bearer {token}"}
        )
    
    assert response.status_code == 200