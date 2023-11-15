from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class UserCreateSchema(BaseModel):
    """ Create User Schema """
    username: str
    password: str
    email: str
    first_name: str
    last_name: str

class UserSchema(UserCreateSchema):
    """ User Schema """
    id: int

    class Config:
        orm_mode = True

class UserWithoutPasswordSchema(BaseModel):
    id: int
    username: str
    email: str
    first_name: str
    last_name: str

    class Config:
        orm_mode = True

class UserAuditSchema(UserSchema):
    """ User Audit Schema """
    created_at: Optional[datetime]
    updated_at: Optional[datetime]
    deleted_at: Optional[datetime]
    created_by_id: Optional[int]
    updated_by_id: Optional[int]
    deleted_by_id: Optional[int]

    class Config:
        orm_mode = True