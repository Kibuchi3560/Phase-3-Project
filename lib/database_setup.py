from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

Base = declarative_base()
engine = create_engine('sqlite:///bookshop.db', echo=True)
Session = sessionmaker(bind=engine)
session = Session()