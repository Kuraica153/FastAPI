from sqlalchemy.orm import Session
from datetime import datetime

class BaseRepo(object):

    def __init__(self, model: object, db: Session):
        self.model = model
        self.db = db

    def get_by_id(self, id: int):
        """ Get a record by id """
        return self.db.query(self.model).filter(self.model.id == id).first()
    
    def get_all(self):
        """ Get all records """
        return self.db.query(self.model).all()
    
    def create(self, obj_in):
        """ Create a record """
        obj = self.model(**obj_in.dict())
        self.db.add(obj)
        self.db.commit()
        self.db.refresh(obj)
        return obj
    
    def update(self, obj_in, obj):
        """ Update a record """
        for field in obj_in.dict(exclude_unset=True):
            setattr(obj, field, getattr(obj_in, field))
        obj.updated_at = datetime.now()
        self.db.commit()
        self.db.refresh(obj)
        return obj
    
    def delete(self, id: int):
        """ Delete a record """
        obj = self.get_by_id(id)
        self.db.delete(obj)
        self.db.commit()
        return True
    
    def soft_delete(self, obj):
        """ Soft delete a record """
        obj.deleted_at = datetime.now()
        self.db.commit()
        self.db.refresh(obj)
        return obj