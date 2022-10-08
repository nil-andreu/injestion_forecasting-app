from fastapi import APIRouter

yahoo_finance_router = APIRouter(
    prefix="/yahoo_finance",
    tags=["financials"]
    # TODO: dependencies for auth definition
)

