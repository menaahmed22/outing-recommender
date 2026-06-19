from fastapi import FastAPI
from routes.baseroute import base_router
from routes.searchgooglemapsroute import searchgooglemapsroute
from apify_client import ApifyClient
from helpers.config import Apify_api
import logging   
import json

logger = logging.getLogger("client.error")
app = FastAPI()
@app.on_event("startup") #must be "" no ''
async def startup_event():
    try:
        app.client = ApifyClient(Apify_api)
    except Exception as e :
        logger.error(f"problem in running client {e}")
@app.on_event("shutdown")  
async def shutdown_event():
    pass  


#uvicorn main:app --reload --host 0.0.0.0 --port 5000
app.include_router(base_router)
app.include_router(searchgooglemapsroute)
