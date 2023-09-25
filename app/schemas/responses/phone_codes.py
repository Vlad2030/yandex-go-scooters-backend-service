from pydantic import BaseModel


class PhoneCode(BaseModel):
    country_code: str = "+7"
    region: str = "RU"
    number_codes: list[str] = ["982", "986", "912", "934"]


class PhoneCodesResponse(BaseModel):
    count: int
    phone_codes: list[PhoneCode]
