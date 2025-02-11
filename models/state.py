#!/usr/bin/python3
""" State Module for HBNB project """
from os import getenv
from models.base_model import BaseModel
from models.city import City


if getenv('HBNB_TYPE_STORAGE') == 'db':
    from sqlalchemy import Column, String
    from sqlalchemy.orm import relationship
    from models.base_model import Base

    class State(BaseModel, Base):
        """ State class """

        __tablename__ = 'states'
        name = Column(
            String(length=128),
            nullable=False
        )
        cities = relationship(
            'City',
            cascade='all, delete-orphan',
            backref='state'
        )

else:
    from models import storage

    class State(BaseModel):
        """ State class """

        name = ''

        @property
        def cities(self):
            """Gets a list of city instances related to a state"""
            cities = []
            all_cities = storage.all(City)
            for city in all_cities.values():
                if city.state_id == self.id:
                    cities.append(city)
            return cities
