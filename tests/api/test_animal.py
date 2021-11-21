from fastapi.testclient import TestClient

from tests.utils.animais import create_animais_extintos, create_animais_nao_extintos, create_random_animais_valido, create_random_animal_invalido, create_random_animais_valido_update

def test_get_animais_sem_dados(client: TestClient) -> None:
    response = client.get("/animais")
    content = response.json()

    assert response.status_code == 404
    assert content["detail"] == 'Não encontrado.'

def test_get_animais_com_dados(client: TestClient) -> None:
    body = create_random_animais_valido()
    client.post("/animais", json=body)

    response = client.get("/animais")
    content = response.json()

    assert response.status_code == 200
    assert len(content) == 1

def test_get_animal_filtrado_por_nome(client: TestClient) -> None:
    body = create_random_animais_valido()
    responsePost = client.post("/animais", json=body)
    contentPost = responsePost.json()
    nome = contentPost["nome"]

    responseGet = client.get("/animais?nome=" + str(nome))
    contentGet = responseGet.json()
    
    assert responseGet.status_code == 200
    assert contentPost["nome"] == contentGet[0]["nome"]

def test_get_animal_extincao(client: TestClient) -> None:
    quantidade_extintos = 3
    quantidade_nao_extintos = 2

    for i in range(quantidade_extintos):
        body = create_animais_extintos()
        response = client.post("/animais", json=body)
        content = response.json()

        assert response.status_code == 201
        assert content["nome"] == body["nome"]

    for i in range(quantidade_nao_extintos):
        body = create_animais_nao_extintos()
        response = client.post("/animais", json=body)
        content = response.json()

        assert response.status_code == 201
        assert content["nome"] == body["nome"]

    response = client.get("/animais/extincao")
    content = response.json()

    assert response.status_code == 200
    assert content["extintos"]["total"] == quantidade_extintos
    assert content["nao_extintos"]["total"] == quantidade_nao_extintos

def test_post_animal(client: TestClient) -> None:
    body = create_random_animais_valido()
    response = client.post("/animais", json=body)
    content = response.json()

    assert response.status_code == 201
    assert content["nome"] == body["nome"]

def test_post_animal_invalido(client: TestClient) -> None:
    body = create_random_animal_invalido()
    response = client.post("/animais", json=body)
    content = response.json()

    assert response.status_code == 422
    assert content["detail"] == "Nome de animal inválido, mínino de 3 caracteres."

def test_post_animais(client: TestClient) -> None:
    quantidade = 10

    for i in range(quantidade):
        body = create_random_animais_valido()
        response = client.post("/animais", json=body)
        content = response.json()

        assert response.status_code == 201
        assert content["nome"] == body["nome"]

    response = client.get("/animais")
    content = response.json()

    assert response.status_code == 200
    assert len(content) == quantidade

def test_delete_animal(client: TestClient) -> None:
    body = create_random_animais_valido()
    responsePost = client.post("/animais", json=body)
    contentPost = responsePost.json()
    id = contentPost["id"]

    responseDelete = client.delete("/animais/" + str(id))

    assert responseDelete.status_code == 204

def test_update_animal(client: TestClient) -> None:
    body = create_random_animais_valido()
    responsePost = client.post("/animais", json=body)
    contentPost = responsePost.json()
    id = contentPost["id"]

    bodyUpdate = create_random_animais_valido_update()
    responseUpdate = client.patch("/animais/" + str(id), json=bodyUpdate)
    contentUpdate = responseUpdate.json()

    assert responseUpdate.status_code == 200
    assert contentUpdate["id"] == id

def test_get_animal_by_id(client: TestClient) -> None:
    body = create_random_animais_valido()
    responsePost = client.post("/animais", json=body)
    contentPost = responsePost.json()
    id = contentPost["id"]

    responseGet = client.get("/animais/" + str(id))
    contentGet = responseGet.json()

    assert responseGet.status_code == 200
    assert contentPost["nome"] == contentGet["nome"]