from pathlib import Path

from fastapi import APIRouter, status
from fastapi.responses import FileResponse

router = APIRouter(prefix="/demo", tags=["demo"])

STATIC_HTML_DIR = Path(__file__).resolve().parent.parent / "static" / "html"


@router.get(
    path="/",
    operation_id="htmlIndex",
    summary="Demonstrating returning the root page",
    status_code=status.HTTP_200_OK,
)
def home() -> FileResponse:
    return FileResponse(STATIC_HTML_DIR / "index.html")


@router.get(
    path="/about",
    operation_id="htmlAbout",
    summary="Demonstrating returning the about page",
    status_code=status.HTTP_200_OK,
)
def about() -> FileResponse:
    return FileResponse(STATIC_HTML_DIR / "about.html")


@router.get(
    path="/docs",
    operation_id="htmlDocs",
    summary="Demonstrating returning the docs page",
    status_code=status.HTTP_200_OK,
)
def docs() -> FileResponse:
    return FileResponse(STATIC_HTML_DIR / "docs.html")


@router.get(
    path="/credits",
    operation_id="htmlCredits",
    summary="Demonstrating returning the credits page",
    status_code=status.HTTP_200_OK,
)
def credits() -> FileResponse:
    return FileResponse(STATIC_HTML_DIR / "credits.html")
