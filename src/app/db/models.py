from .database import metadata
from sqlalchemy import (
    Table, 
    Column, 
    Integer, 
    String, 
    DateTime, 
)
from sqlalchemy.sql import func

notes = Table(
    "notes",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("title", String(50)),
    Column("description", String(50)),
    Column("created_date", DateTime, default=func.now(), nullable=False),
)