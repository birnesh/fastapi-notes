from fastapi import APIRouter

from .endpoints import notes

api_rounter = APIRouter()
api_rounter.include_router(notes.router, tags=['notes'], prefix="/notes")