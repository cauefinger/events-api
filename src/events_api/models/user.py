

from ..database import Base
from sqlalchemy import Column, Integer, String

class User(Base):
    __tablename__ = "users"

    #TODO: Fix unique 
    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String, unique=True, index=True)
    last_name = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)

    def __init__(self, first_name: str, last_name: str, email: str):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
    