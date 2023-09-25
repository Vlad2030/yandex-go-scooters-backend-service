from datetime import datetime
from pydantic import BaseModel
from schemas.responses.order import ScooterInformation


class ScooterLocation(BaseModel):
    location: list[float] = [55.765844, 37.541188]
    last_update: datetime = datetime.now()


class ScooterBattery(BaseModel):
    accumulator_id: int = 123456
    battery: int = 99
    km_left: float = 39.85


class ScooterHardware(BaseModel):
    client_id: str = "ABCDEFG_123456"
    version: str = "0.0.1"


class ScooterResponse(BaseModel):
    status: str = "SLEEP"
    scooter: ScooterInformation
    location: ScooterLocation
    battery: ScooterBattery
    hardware: ScooterHardware
