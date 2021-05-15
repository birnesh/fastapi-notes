from pydantic import BaseModel, EmailStr
from typing import Optional

class UserSchema(BaseModel):
    email: EmailStr 
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    is_super_user: Optional[bool] = False

class UserPost(UserSchema):
    password: str = None


class UserDB(UserSchema):
    id: int