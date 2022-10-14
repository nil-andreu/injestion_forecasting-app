import requests
import asyncio

import pandas as pd
import uvicorn as uvicorn
from fastapi import FastAPI

from routers.standard_and_poor import standard_and_poor_router
from proto import sp500_pb2_grpc, sp500_pb2
# TODO: Async routers
# from kafka.kafka_consumer import consume 

# Get the loop of the actual event
loop = asyncio.get_event_loop()

# Create the application
def create_app() -> FastAPI:
    current_app = FastAPI(
        title="Injestion Service FastAPI",
        description="API for injesting on the data on live as well as on demand",
        version="1.0.0"
    )

    return current_app

app = create_app()
app.include_router(standard_and_poor_router)

# And now we start the consumer on the event of the application
# @app.on_event("startup")
# async def startup_event():

#     # We create a loop of the consume worker of kafka
#     loop.create_task(consume())


# Define the gRPC service
class UserListSP(sp500_pb2_grpc.ListSearchSPServicer):
    # When compiling, it will create a Service 
    def ListSP(self, request, context):
        # We obtain the list of the companies from wiki
        wiki_url = "https://en.wikipedia.org/wiki/List_of_S%26P_500_companies"

        res = requests.get(wiki_url)

        sp_companies = pd.read_html(
            res.text, 
            header=0, 
            )[0]
        
        # And generate an array for all the Companies
        companies_sp500 = [sp500_pb2_grpc.Company(
            ticker = company["ticker"],
            sector = sp500_pb2_grpc.Company.Sector(
                principal = company["GICS Sector"],
                secondary = company["GICS Sub-Industry"]
            ),
            first_added = company["Date first added"],
            year_foundation = company["Founded"]
        ) for company in sp_companies.to_dict(orient="records")]
            


@app.get("/")
async def root():
    # We will serve this gRPC
    

    return sp500_pb2_grpc.ListSearchSP

if __name__ == '__main__':
    # If we call the file, we run from the main file the app, on port 9000, with reloading on every change.
    uvicorn.run("main:app", port=9000, reload=True)