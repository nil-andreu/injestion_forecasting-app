import json
import asyncio
import requests
import pandas as pd
from typing import List

from fastapi import APIRouter, HTTPException, Depends

from db_models.sp500.company import Company

yahoo_finance_router = APIRouter(
    prefix="/yahoo_finance",
    tags=["financials"]
    # TODO: dependencies for auth definition
)

    

@yahoo_finance_router.get("/sp500")
async def get_list_sp500_companies() -> List[Company]:
    wiki_url = "https://en.wikipedia.org/wiki/List_of_S%26P_500_companies"

    # TODO: Try-except for this request, and define fastapi error
    loop = asyncio.get_event_loop()
    future = loop.run_in_executor(None, requests.get, wiki_url)
    res = await future

    sp_companies = pd.read_html(
        res.text, 
        header=0, 
        )[0]
    
    sp_companies = sp_companies.drop(["Security", "CIK"], axis=1)
    sp_companies = sp_companies.fillna('')
    
    
    return sp_companies.to_dict("record")