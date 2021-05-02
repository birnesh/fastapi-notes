from sqlalchemy import (
    Table, 
    Column, 
    Integer, 
    String, 
    DateTime, 
    create_engine, 
    MetaData
)
from sqlalchemy.sql import func
from databases import Database
import os

SQL_DATABSE_URI = "postgresql://memo_fastapi_user:memo_fastapi_user@localhost:5432/memo_fastapi"

engine = create_engine(SQL_DATABSE_URI)
metadata = MetaData()

notes = Table(
    "notes",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("title", String(50)),
    Column("description", String(50)),
    Column("created_date", DateTime, default=func.now(), nullable=False),
)

# databasses query builder
database = Database(SQL_DATABSE_URI)


