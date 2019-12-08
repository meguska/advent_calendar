from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Column, Date, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref

engine = create_engine('sqlite:///pernicky1.db', echo=True)
Base = declarative_base()

class pernicky1(Base):
    """"""
    __tablename__ = "artists"
 
    id = Column(Integer, primary_key=True)
    datum = Column(string)
    nazov= Column(String)
    url= Column(String)

 
    #----------------------------------------------------------------------
    def __init__(self, name):
        """"""
        self.name = name 