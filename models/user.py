#!/usr/bin/python3
"""This module defines a class User"""
from os import getenv


if getenv('HBNB_TYPE_STORAGE') == 'db':
    from models.base_model import BaseModel, Base
    from models.review import Review
    from models.place import Place
    from sqlalchemy.orm import relationship
    from sqlalchemy import (
        Column, String,
    )

    class User(BaseModel, Base):
        """This class defines a user by various attributes"""
        __tablename__ = 'users'
        first_name = Column(
            String(length=128),
            nullable=True
        )
        last_name = Column(
            String(length=128),
            nullable=True
        )
        email = Column(
            String(length=128),
            nullable=False
        )
        password = Column(
            String(length=128),
            nullable=False
        )
        places = relationship(
            'Place',
            backref='user',
            cascade='all, delete-orphan'
        )
        reviews = relationship(
            'Review',
            cascade='all, delete-orphan',
            backref='user'
        )
else:
    from models.base_model import BaseModel

    class User(BaseModel):
        """This class defines a user by various attributes"""
        email = ''
        password = ''
        first_name = ''
        last_name = ''
