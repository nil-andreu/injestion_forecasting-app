import json
import asyncio
import requests
import pandas as pd
from typing import List, Union

from fastapi import APIRouter, HTTPException, \
    Depends, Query

from db_models.sp500.company import Company

SP500_INFO = ['Symbol', 'Security', 'SEC filings', 'GICS Sector', 'GICS Sub-Industry',
       'Headquarters Location', 'Date first added', 'Founded']

yahoo_finance_router = APIRouter(
    prefix="/yahoo_finance",
    tags=["financials"]
    # TODO: dependencies for auth definition
)


async def get_sp_companies() -> pd.DataFrame(columns = SP500_INFO):
    """
    Get the company information for all the 500 companies.
    """

    wiki_url = "https://en.wikipedia.org/wiki/List_of_S%26P_500_companies"

    loop = asyncio.get_event_loop()
    future = loop.run_in_executor(None, requests.get, wiki_url)
    res = await future

    sp_companies = pd.read_html(
        res.text, 
        header=0, 
        )[0]
    
    sp_companies = sp_companies.drop(["CIK"], axis=1)
    sp_companies = sp_companies.fillna('')

    return sp_companies
    

@yahoo_finance_router.get("/sp500")
async def get_list_sp500_companies() -> List[Company]:
    try:
        sp_companies = await get_sp_companies()
        return sp_companies.to_dict("record")
    
    except KeyError:
        raise HTTPException(status_code=404, detail="Data Not Found")
    

@yahoo_finance_router.get("/sp500/{symbol}")
async def get_sp500_compny(symbol: str) -> Union[Company, None]:
    """
    Based on the symbol, we get the company.

    Params:
    - Symbol. This symbol is a string of length 3 identifying the company.


    Returns:
    - Company: The company information if it exists, else None

    """
    try:

        sp_companies = await get_sp_companies()

        # And now we filter by this record
        comp_condition = sp_companies["Symbol"] == symbol
        record = sp_companies.loc[comp_condition]

        return record
    
    except KeyError:
        raise HTTPException(status_code=404, detail="Data Not Found")
    
    
    