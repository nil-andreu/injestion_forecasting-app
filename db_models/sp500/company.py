from datetime import date
from pydantic import BaseModel


class Company(BaseModel):
    symbol: str
    sec_filings: str
    gics_sector: str
    gics_sub_sector: str
    headquarters_location: str
    date_first_added: date
    founded: int

class DataPrice(BaseModel):
    date: date
    open: float
    high: float
    low: float
    close: float
    adjclose: float
    volume: int