import asyncio
from operator import index
import requests
import pandas as pd

# For dates
import datetime as dt
from dateutil.relativedelta import relativedelta

from constants import SP500_INFO
from db_models.sp500.company import Company
from yahoo_fin.stock_info import get_data

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


async def filter_sp_companies(sp_companies: pd.DataFrame, ticker: str) -> Company:
    """
    Filter the dataframe of the standard & poor companies by the ticker of one company.

    Params:
    - sp_companies: the dataframe with the information of all the S&P Companies
    - ticker: the ticker identifier of the company

    Returns:
    - Company: the company information assigned of that ticker
    """

    # And now we filter by this record
    comp_condition = sp_companies["Symbol"] == ticker
    record = sp_companies.loc[comp_condition]

    # If we have dataframe and is not empty
    if isinstance(record, pd.DataFrame) and not record.empty:
        if len(record) == 1:
            return record.to_dict("records")[0]
        
        # Should have to raise an error that we have multiple companies
        raise ValueError("Multiple Company Information Found")
    
    else:
        # TODO: Should have to raise an error of data not found, but with an exception customized
        raise ValueError("Company Ticker not Found")


async def get_public_price(
    ticker: str, 
    interval: str, 
    start_date: dt.date = dt.date.today() - relativedelta(years=3),
    index_as_date: bool = True,
    ):

    public_price = get_data(
        ticker=ticker,
        interval=interval,
        start_date=start_date,
        index_as_date=index_as_date,
    )

    return public_price.to_dict("records")