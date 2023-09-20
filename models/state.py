#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String
from models.city import City
from models.engine.db_storage import DBStorage
from models import storage


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)

    if type(storage) == DBStorage:
        cities = relationship("City", back_populates="state", cascade="all, delete-orphan")
    @property
    def cities(self)
    """cities in FileStorage"""
    cit = []
    for c in storage.all(City).values():
        if c.state_id == self.id:
            cit.append(c)
    return cit
