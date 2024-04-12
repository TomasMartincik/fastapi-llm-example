from app.dependencies import get_llm_provider
from app.main import app


def test_health_endpoint(client):
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_pokemon_empty_description(client):
    response = client.post("/pokemon/identify", json={"pokemon_description": ""})
    assert response.status_code == 400
    assert response.json() == {"detail": "Pokemon description must not be empty"}


def test_pokemon_description_too_long(client):
    response = client.post("/pokemon/identify", json={"pokemon_description": "." * 501})
    assert response.status_code == 400
    assert response.json() == {
        "detail": "Pokemon description must not exceed 500 characters"
    }


def test_pokemon_success_pikachu(client, mock_llm_provider_success):
    app.dependency_overrides[get_llm_provider] = lambda: mock_llm_provider_success
    response = client.post("/pokemon/identify", json={"pokemon_description": "Pikachu"})
    assert response.status_code == 200
    assert response.json() == {
        "id": 25,
        "name": "Pikachu",
        "height": 16,
        "weight": 13.2,
        "category": "Mouse Pokemon",
        "types": ["Electric"],
        "weaknesses": ["Ground"],
        "abilities": ["Static", "Lightning Rod"],
        "stats": {
            "hp": 35,
            "attack": 55,
            "defense": 40,
            "special_attack": 50,
            "special_defense": 50,
            "speed": 90,
        },
    }
    app.dependency_overrides.clear()


def test_pokemon_internal_server_error(client, mock_llm_provider_exception):
    app.dependency_overrides[get_llm_provider] = lambda: mock_llm_provider_exception
    response = client.post("/pokemon/identify", json={"pokemon_description": "Pikachu"})
    assert response.status_code == 500
    assert response.json() == {"detail": "Internal server error"}
    app.dependency_overrides.clear()


def test_pokemon_unidentified(client, mock_llm_provider_none):
    app.dependency_overrides[get_llm_provider] = lambda: mock_llm_provider_none
    response = client.post(
        "/pokemon/identify", json={"pokemon_description": "Unknown creature"}
    )
    assert response.status_code == 404
    assert response.json() == {
        "detail": "Could not identify a pokemon from the description"
    }
    app.dependency_overrides.clear()
