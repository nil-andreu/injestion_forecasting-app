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

standard_and_poor_router = APIRouter(
    prefix="/standard_and_poor",
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
    
    except KeyError:
        raise HTTPException(status_code=404, detail="Data Not Found")


async def filter_sp_companies(sp_companies: pd.DataFrame, ticker: str) -> Company:
    """
    Filter the dataframe of the standard & poor companies by the ticker of one company.

    Params:
    - sp_companies: the dataframe with the information of all the S&P Companies
    - ticker: the ticker identifier of the company

    Returns:
    - Company: the company information assigned of that ticker
    """

    # TODO: Define the await processes
    # And now we filter by this record
    comp_condition = sp_companies["Symbol"] == ticker
    record = sp_companies.loc[comp_condition]

    # If we have data and is not empty
    if not record and not record.empty:
        if len(record) == 1:
            return record.to_dict("records")[0]
        # TODO: Should have to raise an error that we have multiple companies
    
    else:
        # TODO: Should have to raise an error of data not found, but with an exception customized
        raise KeyError



@standard_and_poor_router.get("/{symbol}")
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
    
    except KeyError:
        raise HTTPException(status_code=404, detail="Data Not Found")
    
    
    