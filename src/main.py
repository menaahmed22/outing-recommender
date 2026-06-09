from fastapi import FastAPI
from routes.baseroute import base_router
from routes.searchgooglemapsroute import searchgooglemapsroute
from apify_client import ApifyClient
from helpers.config import Apify_api

app = FastAPI()
@app.on_event("startup") #must be "" no ''
async def startup_event():
    app.client = ApifyClient(Apify_api)

@app.on_event("shutdown")  
async def shutdown_event():
    pass  


#uvicorn main:app --reload --host 0.0.0.0 --port 5000
app.include_router(base_router)
app.include_router(searchgooglemapsroute)
