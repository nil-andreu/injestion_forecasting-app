import uvicorn as uvicorn
from fastapi import FastAPI

def create_app() -> FastAPI:
    current_app = FastAPI(
        title="Injestion Service FastAPI",
        description="API for injesting on the data on live as well as on demand",
        version="1.0.0"
    )

    return current_app

app = create_app()

if __name__ == '__main__':
    # If we call the file, we run from the main file the app, on port 9000, with reloading on every change.
    uvicorn.run("main:app", port=9000, reload=True)