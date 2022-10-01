import uvicorn as uvicorn
from fastapi import FastAPI

def create_app() -> FastAPI:
    current_app = FastAPI(
        title="Injestion Service FastAPI",
        description="API for injesting on the data on live as well as on demand",
        version="1.0.0"
    )

    return current_app