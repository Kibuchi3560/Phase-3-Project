from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker, declarative_base

Base = declarative_base()
engine = create_engine('sqlite:///bookshop.db', echo=False)  
Session = sessionmaker(bind=engine)
session = Session()
