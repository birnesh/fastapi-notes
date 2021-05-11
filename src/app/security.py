from fastapi.param_functions import Depends
from fastapi.security import OAuth2PasswordBearer
from fastapi import status, HTTPException
from passlib.context import CryptContext
from jose import jwt
from datetime import datetime, timedelta

# JWT
ALGORITHM = 'HS256'
SECRET_KEY = 'c1e6f2c509627e1f0617e8f0f06ae812e379dd28d9db1fe5e2fc7e14b6765143'
ACCESS_TOKEN_EXPIRE_MINUTES = 30
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


def create_access_token(
    user_id: int , expires_delta: timedelta = None
) -> str:
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(
            minutes=ACCESS_TOKEN_EXPIRE_MINUTES
        )
    to_encode = {"id": user_id}
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

# password hashing
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)

# in order to avoid circular import 
from app.api.cruds import users_crud

async def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    user_id = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    user = await users_crud.get(user_id["id"])
    if not user:
        raise credentials_exception
    return user