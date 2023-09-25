from pydantic import BaseModel


class PingResponse(BaseModel):
    ok: bool = True
