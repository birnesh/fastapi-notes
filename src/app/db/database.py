from sqlalchemy import MetaData
from databases import Database

SQL_DATABSE_URI = "postgresql://memo_fastapi_user:memo_fastapi_user@localhost:5432/memo_fastapi"

metadata = MetaData()

# databasses query builder
database = Database(SQL_DATABSE_URI)


