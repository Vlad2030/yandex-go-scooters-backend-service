from pydantic import BaseModel
from schemas.responses.order import ScooterInformation


class Order(BaseModel):
    token: str = "qwertyuiopasdfghjklzxcvbnm123456"
    scooter: ScooterInformation
