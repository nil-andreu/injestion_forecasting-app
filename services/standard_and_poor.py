import asyncio
import requests
import pandas as pd

from constants import SP500_INFO
from db_models.sp500.company import Company

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