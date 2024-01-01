#!/usr/bin/python3

"""Database storage module

    Connects to MySQLAlchemy for storage
"""
from os import getenv
from models.base_model import Base
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.state import State
from models.review import Review
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker


class DBStorage():
    """Database storage class"""
    __engine = None
    __session = None
    __classes = {
        "User": User,
        "State": State,
        "Amenity": Amenity,
        "Place": Place,
        "City": City,
        "Review": Review,
    }

    def __init__(self):
        """Initializes the storage engine"""
        HBNB_MYSQL_DB = getenv('HBNB_MYSQL_DB')
        HBNB_MYSQL_HOST = getenv('HBNB_MYSQL_HOST')
        HBNB_MYSQL_USER = getenv('HBNB_MYSQL_USER')
        HBNB_MYSQL_PWD = getenv('HBNB_MYSQL_PWD')
        HBNB_ENV = getenv('HBNB_ENV')
        self.__engine = create_engine(
            'mysql+mysqldb://{}:{}@{}:3306/{}'.format(
                HBNB_MYSQL_USER, HBNB_MYSQL_PWD,
                HBNB_MYSQL_HOST, HBNB_MYSQL_DB
            ), pool_pre_ping=True
        )
        if HBNB_ENV == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Query all objects of a certain class"""
        new_dict = {}
        if cls is None:
            for _class in self.__classes:
                query = self.__session.query(
                    self.__classes[_class]
                ).all()
                for obj in query:
                    key = obj.__class__.__name__ + '.' + obj.id
                    new_dict[key] = obj.to_dict()
                    if new_dict[key].get('__class__', None) is not None:
                        del new_dict[key]['__class__']
            return new_dict
        elif cls.__name__ in self.__classes:
            query = self.__session.query(
                self.__classes[cls.__name__]
            ).all()
            for obj in query:
                key = obj.__class__.__name__ + '.' + obj.id
                new_dict[key] = obj.to_dict()
            return new_dict

    def new(self, obj):
        """Add a new object to the database"""
        self.__session.add(obj)

    def save(self):
        """Commit all changes to the database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete from the current db session"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """Create all tables in the database and the session"""
        Base.metadata.create_all(self.__engine)
        sessionFactory = sessionmaker(
            bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(sessionFactory)
        self.__session = Session

    def close(self):
        """Close"""
        self.__session.remove()
