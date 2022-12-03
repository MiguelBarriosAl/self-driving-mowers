from fastapi import APIRouter
from starlette.responses import JSONResponse
from api_v1.schemas import Input
from api_v1.services import movements

__version__ = "0.1.0"


router = APIRouter()


@router.get("/", status_code=200)
def main_page():
    response = {
        "HealthCheck": "Ok",
        "Version": __version__}
    return JSONResponse(content=response, media_type="application/json")


@router.post("/mower/")
def post(payload: Input):
    global top
    if payload.top is not None:
        top = payload.top
    position = payload.position
    instructions = payload.instructions
    output = movements(top, position, instructions)
    return output


