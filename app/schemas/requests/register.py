from pydantic import BaseModel, validator


class Register(BaseModel):
    first_name: str
    last_name: str
    phone_number: str
