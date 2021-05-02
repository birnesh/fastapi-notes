import json
import pytest

from app.api.cruds import notes_crud

# notes post
def test_create_notes(test_app, monkeypatch):
    test_request_payload = {"title":"python rocks", "description":"hell yeah, it does"}
    test_response_payload = {"id":1, "title": "python rocks", "description": "hell yeah, it does"}

    async def mock_post(payload):
        return 1

    monkeypatch.setattr(notes_crud, "post", mock_post)

    response = test_app.post("/notes/", data=json.dumps(test_request_payload),)

    assert response.status_code == 201
    assert response.json() == test_response_payload

def test_create_note_invalid_json(test_app):
    response = test_app.post("/notes/", data=json.dumps({"title":"something"}))
    assert response.status_code == 422

# notes retrieve
def test_read_notes(test_app, monkeypatch):
    test_data = {"id": 1, "title": "Python", "description": "cool language"}

    async def mock_get(id):
        return test_data
    
    monkeypatch.setattr(notes_crud, "get", mock_get)

    response = test_app.get("/notes/1")
    assert response.status_code == 200
    assert response.json() == test_data

def test_read_note_incorrec_id(test_app, monkeypatch):
    async def mock_get(id):
        return None
    
    monkeypatch.setattr(notes_crud, "get", mock_get)

    response = test_app.get("/notes/99")
    assert response.status_code == 404
    assert response.json()["detail"] == "Note not found"

# notes read all
def test_read_all_notes(test_app, monkeypatch):
    test_data = [
        {"title": "python", "description": "cool", "id":1},
        {"title": "js", "description": "equally cool", "id":2},
    ]

    async def mock_get_all():
        return test_data
    
    monkeypatch.setattr(notes_crud, "get_all", mock_get_all)

    response = test_app.get("/notes/")
    assert response.status_code == 200
    assert response.json() == test_data

    # put notes
def test_update_notes(test_app, monkeypatch):
    test_update_data = {"title": "python", "description": "cool", "id": 1}

    async def mock_get(id):
        return True

    monkeypatch.setattr(notes_crud, "get", mock_get)

    async def mock_put(id, payload):
        return 1

    monkeypatch.setattr(notes_crud, "put", mock_put)

    response = test_app.put("/notes/1/", data=json.dumps(test_update_data))
    assert response.status_code == 200
    assert response.json() == test_update_data

@pytest.mark.parametrize(
    "id, payload, status_code",
    [
        [1, {}, 422],
        [1,{"title":"fast_api"}, 422],
        [999, {"title": "fastapi", "description": "fast"}, 404],
    ],
)
def test_update_note_invalid(test_app, monkeypatch, id, payload, status_code):
    # this function will loop three time with the values inside parameterize decorator

    async def mock_get(id):
        return None
    
    monkeypatch.setattr(notes_crud, "get", mock_get)
    response = test_app.put(f"/notes/{id}/", data=json.dumps(payload),)
    assert response.status_code == status_code

# delete notes
def test_delete_note(test_app, monkeypatch):
    test_delete_data = {"title": "python", "description": "cool", "id": 1}
    async def mock_get(id):
        return test_delete_data
    monkeypatch.setattr(notes_crud, "get", mock_get)
    async def mock_delete(id):
        return id
    monkeypatch.setattr(notes_crud, "delete", mock_delete)

    response = test_app.delete("/notes/1/")
    assert response.status_code == 200
    assert response.json() == test_delete_data

def test_delete_note_invalid(test_app, monkeypatch):
    test_delete_data = {"title": "python", "description": "cool", "id": 1}
    async def mock_get(id):
        return None
    monkeypatch.setattr(notes_crud, "get", mock_get)
    
    response = test_app.delete("/notes/888/")
    assert response.status_code == 404
    assert response.json()["detail"] == "Note not found"