from datetime import datetime
from pydantic import BaseModel


class BaseUserInformation(BaseModel):
    profile_picture: str | None = None
    first_name: str = "Ivan"
    last_name: str = "Ivanov"
    age: datetime | None = datetime(year="2000", month="01", day="01")
    plus: bool = True
    username: str | None = "iivanov"


class PrivateUserInformation(BaseModel):
    phone_number: str = "+79001234567"
    email: str | None = "iivanov@yandex.ru"


class UserResponse(BaseModel):
    id: int = 1
    base_information: BaseUserInformation
    private_information: PrivateUserInformation
    role: str = "buyer"
    rating: float = 4.00
    created_at: datetime = datetime.now()
