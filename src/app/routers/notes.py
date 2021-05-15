from typing import List, Any
from fastapi import APIRouter, HTTPException, Depends
from app.schemas.notes import NoteDB, NoteSchema
from app.cruds import notes as notes_crud
from app import dependencies
router = APIRouter()

@router.post("/",response_model=NoteDB, status_code=201)
async def create_note(payload: NoteSchema, user: int =Depends(dependencies.get_current_user)):
    note_id = await notes_crud.post(payload)

    response_object = {
        "id": note_id,
        "title": payload.title,
        "description": payload.description,
    }
    return response_object

@router.get("/{id}/",  response_model=NoteDB)
async def read_note(id: int, user: int =Depends(dependencies.get_current_user)):
    note = await notes_crud.get(id)
    if not note:
        raise HTTPException(status_code=404, detail="Note not found")
    return note

@router.get("/", response_model=List[NoteDB])
async def read_all_notes(user: int =Depends(dependencies.get_current_user)):
    return await notes_crud.get_all()

@router.put("/{id}/", response_model=NoteDB)
async def update_note(id: int, payload: NoteSchema,user: int =Depends(dependencies.get_current_user)):
    note = await notes_crud.get(id)
    if not note:
        raise HTTPException(status_code=404, detail="Note not found")
    note_id = await notes_crud.put(id, payload)

    response_object = {
        "id": note_id,
        "title": payload.title,
        "description": payload.description,
    }
    return response_object

@router.delete("/{id}/", response_model=NoteDB)
async def delete_note(id: int, user: int =Depends(dependencies.get_current_user)):
    note = await notes_crud.get(id)
    if not note:
        raise HTTPException(status_code=404, detail="Note not found")
    
    await notes_crud.delete(id)

    return note


