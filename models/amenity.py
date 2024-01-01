#!/usr/bin/python3
""" State Module for HBNB project """
from os import getenv

if getenv('HBNB_TYPE_STORAGE') == 'db':
    from sqlalchemy import Column, String
    from models.base_model import BaseModel, Base

    class Amenity(BaseModel, Base):
        """An amenity"""
        __tablename__ = 'amenities'
        name = Column(
            String(length=128),
            nullable=False
        )

else:
    from models.base_model import BaseModel

    class Amenity(BaseModel):
        """An amenity"""
        name = ""
