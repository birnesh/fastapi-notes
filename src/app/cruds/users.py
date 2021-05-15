from pydantic.networks import EmailStr
from app.schemas.users import UserPost
from app.db.models import users
from app.db.database import database
from app.security import get_password_hash, verify_password

async def post(payload: UserPost):
    hashed_password = get_password_hash(payload.password)
    query = users.insert().values(
        email=payload.email,
        password = hashed_password,
        first_name=payload.first_name, 
        last_name=payload.last_name,
        is_super_user = payload.is_super_user
        )
    return await database.execute(query=query)

async def get(id: int):
    query = users.select().where(id == users.c.id)
    return await database.fetch_one(query=query)

async def get_all():
    query = users.select()
    return await database.fetch_all(query=query)

async def delete(id: int):
    query = users.delete().where(id == users.c.id)
    return await database.execute(query=query)

async def authenticate(email: EmailStr, password: str):
    query = users.select().where(email == users.c.email)
    user =  await database.fetch_one(query=query)
    if not user:
        return None
    if not verify_password(password, user["password"]):
        return None
    print(user)
    return user
    
