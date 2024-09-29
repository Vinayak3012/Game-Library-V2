from flask_security import SQLAlchemyUserDatastore

from .model import Role, User, db

ds = SQLAlchemyUserDatastore(db, User, Role)
