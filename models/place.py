#!/usr/bin/python3
""" Place Module for HBNB project """
from os import getenv


if getenv('HBNB_TYPE_STORAGE') == 'db':
    from sqlalchemy import Table
    from sqlalchemy.orm import relationship
    from sqlalchemy import (
        Column,
        String,
        ForeignKey,
        Integer,
        Float
    )
    from models.base_model import BaseModel, Base
    from models.amenity import Amenity
    from models.review import Review

    # Create association table for Many-to-Many
    place_amenity = Table(
        'place_amenity',
        Base.metadata,
        Column(
            'place_id',
            String(length=60),
            ForeignKey('places.id'),
            primary_key=True,
            nullable=False
        ),
        Column(
            'amenity_id',
            String(length=60),
            ForeignKey('amenities.id'),
            primary_key=True,
            nullable=False
        )
    )

    class Place(BaseModel, Base):
        """ A place to stay """

        __tablename__ = 'places'
        city_id = Column(
            String(length=60),
            ForeignKey('cities.id'),
            nullable=False
        )
        user_id = Column(
            String(length=60),
            ForeignKey('users.id'),
            nullable=False
        )
        name = Column(String(length=128), nullable=False)
        description = Column(String(length=1024), nullable=True)
        number_rooms = Column(Integer, nullable=False, default=0)
        number_bathrooms = Column(Integer, nullable=False, default=0)
        max_guest = Column(Integer, nullable=False, default=0)
        price_by_night = Column(Integer, nullable=False, default=0)
        latitude = Column(Float, nullable=True)
        longitude = Column(Float, nullable=True)
        amenities = relationship(
            'Amenity',
            secondary=place_amenity,
            backref='place_amenities',
            viewonly=False
        )
        reviews = relationship(
            'Review',
            backref='place',
            cascade='all, delete-orphan'
        )

else:
    from models.base_model import BaseModel
    from models.amenity import Amenity
    from models import storage

    class Place(BaseModel):
        """ A place to stay """

        __classes = {
            "Amenity": Amenity
        }
        city_id = ""
        user_id = ""
        name = ""
        description = ""
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0
        amenity_ids = []

    @property
    def amenities(self):
        """Gets a list of amenities"""
        amenity_list = []
        all_amenities = storage.all(Place.__classes['Amenity'])
        for amenity in all_amenities:
            if amenity.place_id == self.id:
                amenity_list.append(amenity)
        return amenity_list

    @amenities.setter
    def amenities(self, amenity=None):
        """Adds an amenity"""
        if isinstance(amenity, Place.__classes['Amenity']):
            Place.amenity_ids.append(amenity.id)

    @property
    def reviews(self):
        """Returns a list of reviews for a place"""
        review_list = []
        all_reviews = storage.all(Place.__classes['Review'])
        for review in all_reviews:
            if review.place_id == self.id:
                review_list.append(review)
        return review_list
