import json
import asyncio
import requests
import pandas as pd
from typing import List, Union

from fastapi import APIRouter, HTTPException, \
    Depends, Query

from constants import SP500_INFO
from db_models.sp500.company import Company
from services.standard_and_poor import get_sp_companies, filter_sp_companies

standard_and_poor_router = APIRouter(
    prefix="/standard_and_poor",
    tags=["financials"]
    # TODO: dependencies for auth definition
)
        

@standard_and_poor_router.get("/")
async def get_list_sp_companies() -> List[Company]:
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


@standard_and_poor_router.get("/{ticker}")
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
    
    
    