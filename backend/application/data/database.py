from flask_sqlalchemy import SQLAlchemy
#! ORM - object relational mapping
# > class - table
# > object - row
from sqlalchemy.ext.declarative import declarative_base

engine = None
Base = declarative_base()


#! db object - SQLAlchemy class
db = SQLAlchemy()
