from .database import Base, engine
from . import models 
from fastapi import FastAPI

Base.metadata.create_all(bind=engine)
app = FastAPI()


"""
http://127.0.0.1:8000
"""