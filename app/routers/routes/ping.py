from fastapi import APIRouter, status
from fastapi.responses import JSONResponse
from schemas.responses.ping import Ping

router = APIRouter(prefix="/ping")

@router.get(
    path="/",
    response_model=Ping,
    status_code=status.HTTP_200_OK,
    summary="Server health check",
    description="Ping endpoint",
    response_description="""If "ok": true, then server is running successfully""",
)
async def get_ping() -> JSONResponse:
    ping = Ping(ok=True)
    return JSONResponse(
        content=ping.dict(),
        status_code=status.HTTP_200_OK,
        )