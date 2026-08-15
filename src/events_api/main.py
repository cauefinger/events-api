from .database import Base, engine
from . import models 
from fastapi import FastAPI
from .routers.event_router import event_router

Base.metadata.create_all(bind=engine)
app = FastAPI()

app.include_router(event_router)

"""
http://127.0.0.1:8000
"""