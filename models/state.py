#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.city import City
from os import getenv


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        cities = relationship('City', back_populates='state_rel',
                              cascade='all, delete-orphan')
    else:
        @property
        def cities(self):
            """property getter for the cities"""
            from models import storage
            city_objs = storage.all('City').values()
            return [city for city in city_objs if
                    city.state_id == self.id]
