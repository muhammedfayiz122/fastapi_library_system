from sqlalchemy import Column,Integer,String
from app.database import Base

class Book(Base):
    __tablename__ ="books"

    id = Column(Integer,primary_key=True,index =True)
    title = Column(String,nullable=False)
    author = Column(String,nullable=False)
    published_year = Column(Integer)
    isbn = Column(String,unique = True,nullable=False)
    available_copies = Column(Integer,default =1)