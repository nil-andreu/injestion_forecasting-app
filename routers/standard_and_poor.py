import json
import asyncio
import requests
import pandas as pd

from pydantic import BaseModel
from typing import List, Union


from fastapi import APIRouter, HTTPException, \
    Depends, Query

from constants import SP500_INFO
from db_models.sp500.data_price import DataPrice, BodyDataPrice
from db_models.sp500.company import Company
from services.standard_and_poor import get_sp_companies, filter_sp_companies, get_public_price

# Interesting we can request multiple financial statements
from yahoofinancials import YahooFinancials as yf


# tags_metadata = [
#     {"name": "Yahoo Fin", "description": "Accessing Yahoo Finance with Yahoo Fin library"},
#     {"name": "Yahoo Financials", "description": "Accessing Yahoo Finance with Yahoo Financials library"}
# ]


standard_and_poor_router = APIRouter(
    prefix="/standard_and_poor",
    # TODO: dependencies for auth definition
)
        

@standard_and_poor_router.get("/yahoo_fin/", tags=["S&P500 / Yahoo Fin"])
async def get_list_sp_companies() -> Union[List[Company], None]:
    """
    Get the list of all the Standard & Poors 500 companies.

    Params:

    Returns:
    - sp_companies: a list of the company informations

    """

    try:
        sp_companies: pd.DataFrame(columns=SP500_INFO) = await get_sp_companies()
        return sp_companies.to_dict("record")
    
    # If we have a value error, means we were not able to get the information from the table
    except ValueError:
        raise HTTPException(status_code=404, detail="Data of S&P500 Companies Not Found")


@standard_and_poor_router.get("/yahoo_fin/{ticker}", tags=["S&P500 / Yahoo Fin"])
async def get_sp_compny(
    ticker: str = Query(default= "", max_length=4, min_length=3)
) -> Union[Company, None]:
    """
    Based on the symbol, we get the company.

    Params:
    - ticker: this ticker is a string of length 3-4 identifying the company.

    Returns:
    - Company: The company information if it exists, else None

    """
    try:
        sp_companies: pd.DataFrame(columns=SP500_INFO) = await get_sp_companies()
        record: Company = await filter_sp_companies(sp_companies, ticker)
        return record
    
    except ValueError:
        raise HTTPException(status_code=404, detail="Data Not Found")


@standard_and_poor_router.post("/yahoo_fin/data_price/", tags=["S&P500 / Yahoo Fin"])
async def get_data_price_sp_compny(
    body_data_price: BodyDataPrice
) -> Union[List[DataPrice], None]:
    """
    Based on the symbol, we get the company.

    Params:
    - ticker: this ticker is a string of length 3-4 identifying the company.
    - interval: the interval of the records of the prices: ("1d", "1wk", "1mo", "1m")
    - start_date: how much time to look to the past prices
    - index_as_date: the returned dataframe has the date as the index

    Returns:
    - DataPrice: The data of the prices of the company for the given period.

    """
    try:
        data_prices: List[DataPrice] = await get_public_price(
            ticker=body_data_price.ticker, 
            interval=body_data_price.interval,
            start_date=body_data_price.start_date,
            index_as_date=body_data_price.index_as_date
        )

        return data_prices
    
    # If the data does not exists for a certain ticker, the function raises a KeyError
    except KeyError:
        raise HTTPException(status_code=404, detail="Data Not Found")


@standard_and_poor_router.post("/yahoo_financials/beta/{ticker}", tags=["S&P500 / Yahoo Financials"])
async def get_beta_sp_compny(
    ticker: str = Query(default= "", max_length=4, min_length=3)
) -> Union[str, None]:
    company = yf(ticker)
    beta = company.get_beta()

    # In the case there is a beta
    if beta:
        return beta

    raise HTTPException(status_code=404, detail="Data Beta Found For this Ticker")


@standard_and_poor_router.post("/yahoo_financials/capitalization/{ticker}", tags=["S&P500 / Yahoo Financials"])
async def get_beta_sp_compny(
    ticker: str = Query(default= "", max_length=4, min_length=3)
) -> Union[str, None]:
    company = yf(ticker)
    market_capitalization = company.get_market_cap()

    # In the case there is a beta
    if market_capitalization:
        return market_capitalization

    raise HTTPException(status_code=404, detail="Data Beta Found For this Ticker")
