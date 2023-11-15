from .base_repo import BaseRepo

class UserRepo(BaseRepo):
    
    def get_by_username(self, username: str):
        """ Get a record by username """
        return self.db.query(self.model).filter(self.model.username == username).first()