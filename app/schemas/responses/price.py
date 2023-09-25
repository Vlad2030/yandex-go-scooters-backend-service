import time
from pydantic import BaseModel


class Prices(BaseModel):
    rent_price: float = 7.00
    insurance_price: float = 1.00


class PriceResponse(BaseModel):
    prices: Prices
    time: int = time.time() * 1000
