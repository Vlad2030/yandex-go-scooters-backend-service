from datetime import datetime
from pydantic import BaseModel


class ScooterInformation(BaseModel):
    scooter_id: int = 123456
    scooter_name: str = "NineBot MAX PLUS Yndx"


class TimeInformation(BaseModel):
    start_time: datetime = datetime(year="2023",
                                    month="1",
                                    day="1",
                                    hour="10",
                                    minute="00")
    end_time: datetime = datetime(year="2023",
                                    month="1",
                                    day="1",
                                    hour="12",
                                    minute="00")


class AddressInformation(BaseModel):
    start_address: list[float] = [55.770719, 37.504146]
    end_address: list[float] = [55.765844, 37.541188]


class OrderResponse(BaseModel):
    token: str = "qwertyuiopasdfghjklzxcvbnm123456"
    scooter: ScooterInformation
    time: TimeInformation
    address: AddressInformation
    total_price: float
