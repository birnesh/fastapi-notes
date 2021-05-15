from typing import List
from fastapi import APIRouter, HTTPException
from starlette import responses

from app.cruds import users as users_crud
from app.schemas.users import UserSchema, UserDB, UserPost
router = APIRouter()

@router.post("/", response_model=UserDB, status_code=201)
async def create_user(payload: UserPost):
    user_id = await users_crud.post(payload)

    response_object = {
        "id": user_id,
        "first_name": payload.first_name,
        "last_name": payload.last_name,
        "email": payload.email,
    }
    return response_object

@router.get("/{id}/", response_model=UserDB)
async def read_user(id: int):
    user = await users_crud.get(id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.get("/", response_model=List[UserDB])
async def read_all_user():
    return await users_crud.get_all()

@router.delete("/{id}/", response_model=UserDB)
async def delete_user(id: int):
    user = await users_crud.get(id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    await users_crud.delete(id)

    return user
