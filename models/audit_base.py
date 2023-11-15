from configs.database import Base
from sqlalchemy.ext.declarative import declared_attr
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime

class AuditBase(Base):
    __abstract__ = True

    created_by_id = Column(Integer, ForeignKey("user.id"))
    updated_by_id = Column(Integer, ForeignKey("user.id"))
    deleted_by_id = Column(Integer, ForeignKey("user.id"))
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow)
    deleted_at = Column(DateTime, default=datetime.utcnow)

    @declared_attr
    def created_by(cls):
        return relationship("UserModel", foreign_keys=[cls.created_by_id])
    
    @declared_attr
    def updated_by(cls):
        return relationship("UserModel", foreign_keys=[cls.updated_by_id])

    @declared_attr
    def deleted_by(cls):
        return relationship("UserModel", foreign_keys=[cls.deleted_by_id])