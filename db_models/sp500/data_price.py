from datetime import date
from pydantic import BaseModel

class DataPrice(BaseModel):
    date: date
    open: float
    high: float
    low: float
    close: float
    adjclose: float
    volume: int