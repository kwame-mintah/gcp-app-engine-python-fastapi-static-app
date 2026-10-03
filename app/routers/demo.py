from fastapi import APIRouter, status
from fastapi.responses import FileResponse

router = APIRouter(prefix="/demo", tags=["demo"])


@router.get(
    path="/",
    operation_id="htmlIndex",
    summary="Demonstrating returning the root page",
    status_code=status.HTTP_200_OK,
)
def home() -> FileResponse:
    return FileResponse("static/html/index.html")


@router.get(
    path="/about",
    operation_id="htmlAbout",
    summary="Demonstrating returning the about page",
    status_code=status.HTTP_200_OK,
)
def about():
    return FileResponse("static/html/about.html")


@router.get(
    path="/contact",
    operation_id="htmlContact",
    summary="Demonstrating returning the contact page",
    status_code=status.HTTP_200_OK,
)
def contact():
    return FileResponse("static/html/contact.html")
