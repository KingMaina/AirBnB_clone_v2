#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel
from models import HBNB_TYPE_STORAGE

if HBNB_TYPE_STORAGE == 'db':
    from sqlalchemy import Column, String, ForeignKey
    from sqlalchemy.orm import relationship
    from models.base_model import Base

    class City(BaseModel, Base):
        """ The city class, contains state ID and name """

        __tablename__ = 'cities'
        name = Column(
            String(length=128),
            nullable=False
        )
        state_id = Column(
            String(length=60),
            ForeignKey('states.id'),
            nullable=False
        )
        places = relationship(
            'Place',
            backref='cities'
        )
else:

    class City(BaseModel):
        """ The city class, contains state ID and name """

        name = ""
        state_id = ""
