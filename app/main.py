from fastapi import FastAPI

from app.api import api_router

from . import models
from .database import engine

app = FastAPI()

models.Base.metadata.create_all(bind=engine)


@app.get("/health", include_in_schema=False)
def get_health():
    return "Ok"


app.include_router(api_router)
