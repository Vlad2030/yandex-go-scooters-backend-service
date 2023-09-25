from pydantic import BaseModel


class RolesResponse(BaseModel):
    roles: list[str] = ["buyer", "tester", "worker"]
