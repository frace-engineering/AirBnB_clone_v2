from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from os import getenv
from models.base_model import Base


class DBStorage:
    __engine = None
    __session = None

    def __init__(self):
        user = getenv("HBNB_MYSQL_USER")
        pwd = getenv("HBNB_MYSQL_PWD")
        host = getenv("hbnb_mysql_host")
        db = getenv("HBNB_MYSQL_DB")
        db_path = f'mysql+mysqldb://{user}:{pwd)}@{host)}/{db}'
        self.__engine = create_engine(db_path, pool_pre_ping=True)
        if getenv("HBNB_ENV") == 'test':
            Base.metadata.drop_all(self.__engine)
        Base.metadata.create_all(self.__engine)
        self.__session = scoped_session(sessionmaker(bind=self.__engine,
                                        expire_on_commit=False))

    def all(self, cls=None):
        objects_dict = {}
        if cls:
            objects = self.__session.query(cls).all()
        else:
            classes = [User, State, City, Amenity, Place, Review]
            objects = []
            for c in classes:
                objects.extend(self.__session.query(c).all())
        for obj in objects:
            key = "{}.{}".format(type(obj).__name__, obj.id)
            objects_dict[key] = obj
        return objects_dict

    def new(self, obj):
        """Add the session to the object """
        self.__sesson.add(obj)

    def save(self):
        """Commit all changes to the current database """
        self.__session.commit()

    def deleete(self, obj=None):
        """Delete obj if exists"""
        if obj:
            self.__session.delte(obj)

    def reload(self):
        """Reload the session """
        Base.metadata.create_all(self.__engine)
        Session = scoped_session(sessionmaker(bind=self.__engine,
                                 expire_on_comit=False))
        self.__session = Session()

    def close(self):
        """ Call remove() on the __session """
        self.__session.remove()
