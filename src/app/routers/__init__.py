from fastapi import APIRouter

from . import notes, users, login

api_rounter = APIRouter()
api_rounter.include_router(login.router, tags=['login'])
api_rounter.include_router(notes.router, tags=['notes'], prefix="/notes")
api_rounter.include_router(users.router, tags=['users'], prefix="/users")