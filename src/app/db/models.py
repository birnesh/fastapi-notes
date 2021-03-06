from .database import metadata
from sqlalchemy import (
    Table, 
    Column, 
    Integer, 
    String, 
    DateTime, 
    Boolean
)
from sqlalchemy.sql import func

users = Table(
    "users",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("email", String(320), unique=True),
    Column("password", String(127)),
    Column("first_name", String(50),nullable=True),
    Column("last_name", String(50),nullable=True),
    Column("is_super_user", Boolean, default=False )
)

notes = Table(
    "notes",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("title", String(50)),
    Column("description", String(50)),
    Column("created_date", DateTime, default=func.now(), nullable=False),
)