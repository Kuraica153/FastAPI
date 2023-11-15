from sqlalchemy.orm import Session
from repositories.user_repo import UserRepo
from models.user_model import UserModel
from utils.app_exceptions import AppException

class UserService(object):

    def __init__(self, db: Session):
        self.db = db
        self.repo = UserRepo(UserModel, db)

    def get_by_id(self, id: int):
        """ Get a record by id """
        response = self.repo.get_by_id(id)
        if not response:
            raise AppException.NotFound(f"User with id {id} does not exist")
        return response
    
    def get_all(self):
        """ Get all records """
        return self.repo.get_all()
    
    def create(self, obj_in):
        """ Create a record """
        return self.repo.create(obj_in)
    
    def update(self, obj_in, id: int):
        """ Update a record """
        obj = self.get_by_id(id)
        return self.repo.update(obj_in, obj)
    
    def delete(self, id: int):
        """ Delete a record """
        return self.repo.delete(id)
    
    def soft_delete(self, id: int):
        """ Soft delete a record """
        obj = self.get_by_id(id)
        return self.repo.soft_delete(obj)