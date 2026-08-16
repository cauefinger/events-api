

from ..database import Base
from sqlalchemy import Column, Integer, String

class User(Base):
    __tablename__ = "users"

    #TODO: Fix unique 
    id = Column(Integer,unique=True, primary_key=True, index=True)
    first_name = Column(String, index=True)
    last_name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
