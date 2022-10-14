from datetime import date
from pydantic import BaseModel

# For dates
import datetime as dt
from dateutil.relativedelta import relativedelta

class DataPrice(BaseModel):
    date: date
    open: float
    high: float
    low: float
    close: float
    adjclose: float
    volume: int


class BodyDataPrice(BaseModel):
    ticker: str
    interval: str 
    start_date: dt.date = dt.date.today() - relativedelta(years=3)
    index_as_date: bool = True