# in order to avoid circular import 
from app.cruds import users as users_crud
from fastapi import Depends,HTTPException, status
from app.security import oauth2_scheme , SECRET_KEY, ALGORITHM
from jose import jwt

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