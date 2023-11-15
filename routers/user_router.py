from fastapi import APIRouter, Depends
from configs.database import get_db
from services.user_service import UserService
from schemas.user_schema import UserWithoutPasswordSchema, UserCreateSchema
from utils.auth import get_current_user

router = APIRouter(
    prefix="/users",
    tags=["users"],
    responses={404: {"description": "Not found"}},
)

@router.get("/", response_model=list[UserWithoutPasswordSchema], summary="Get all records")
async def get_all(db=Depends(get_db), current_user: str = Depends(get_current_user)):
    """ Get all records """
    return UserService(db).get_all()

@router.get("/{id}", response_model=UserWithoutPasswordSchema, summary="Get a record by id")
async def get_by_id(id: int, db=Depends(get_db)):
    """ Get a record by id """
    return UserService(db).get_by_id(id)

@router.post("/", response_model=UserWithoutPasswordSchema, summary="Create a record")
async def create(obj_in: UserCreateSchema, db=Depends(get_db)):
    """ Create a record """
    return UserService(db).create(obj_in)

@router.put("/{id}", response_model=UserWithoutPasswordSchema, summary="Update a record")
async def update(id: int, obj_in: UserCreateSchema, db=Depends(get_db)):
    """ Update a record """
    return UserService(db).update(obj_in, id)

@router.delete("/{id}", summary="Delete a record")
async def delete(id: int, db=Depends(get_db)):
    """ Delete a record """
    return UserService(db).soft_delete(id)
