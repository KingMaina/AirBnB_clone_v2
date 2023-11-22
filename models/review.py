#!/usr/bin/python3
""" Review module for the HBNB project """
from models import HBNB_TYPE_STORAGE


if HBNB_TYPE_STORAGE == 'db':
    from sqlalchemy import Column, String, ForeignKey
    from models.base_model import BaseModel, Base

    class Review(BaseModel, Base):
        """ Review class to store review information """
        __tablename__ = 'reviews'
        text = Column(
            String(length=1024),
            nullable=False
        )
        place_id = Column(
            String(length=60),
            ForeignKey('places.id'),
            nullable=False,
        )
        user_id = Column(
            String(length=60),
            ForeignKey('users.id'),
            nullable=False,
        )
else:
    from models.base_model import BaseModel

    class Review(BaseModel):
        """ Review classto store review information """
        place_id = ""
        user_id = ""
        text = ""
