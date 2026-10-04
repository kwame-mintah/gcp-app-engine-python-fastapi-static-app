from pathlib import Path

import uvicorn
from fastapi import FastAPI, status
from fastapi.staticfiles import StaticFiles

from app.internal import versions
from app.routers import demo

# Provide meta data for API.
# https://fastapi.tiangolo.com/tutorial/metadata/#metadata-for-api
app = FastAPI(
    title="Google Cloud Platform (GCP) App Engine Python Static Appe",
    description="This demonstrates how to use FastAPI to serve static files in your application.",
    contact={
        "name": "gcp-app-engine-python-fastapi-static-app",
        "url": "https://github.com/kwame-mintah/gcp-app-engine-python-fastapi-static-app",
        "email": "email@email.com",
    },
    license_info={
        "name": "Example License",
        "url": "https://choosealicense.com/",
    },
)
static_dir = Path(__file__).resolve().parent / "static"
app.mount(path="/static", app=StaticFiles(directory=static_dir), name="static")
app.include_router(demo.router)
app.include_router(versions.router)


@app.get(path="/", tags=["root"], status_code=status.HTTP_200_OK)
async def root() -> dict:
    """
    Example response, when accessing root e.g. `http://localhost:8000/`
    :return: response
    """
    return {"message": "What a wonderful kind of day."}


if __name__ == "__main__":
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000)
