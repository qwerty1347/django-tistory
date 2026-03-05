from fastapi import FastAPI

from app.api import api_router
from app.core.logging import setup_logging


setup_logging()

app = FastAPI()
app.include_router(api_router)


@app.get('/')
def index():
    return {"message": "Hello FastAPI"}