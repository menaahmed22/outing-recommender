from fastapi import FastAPI , APIRouter ,Depends
from services.searchgooglemaps import search_google_maps
from .schemas.data import ProcessRequest
from helpers.dependencies import get_apify_client

from apify_client import ApifyClient

searchgooglemapsroute = APIRouter(
    prefix="/api/searchgooglemapsroute",
    tags=["searchgooglemapsroute"],
)
@searchgooglemapsroute.post("/")
async def searchgooglemaps(process_request : ProcessRequest ,client: ApifyClient = Depends(get_apify_client) ):
    latitude =process_request.latitude 
    longitude = process_request.longitude 
    distance_km =process_request.distance_km 
    search_type = process_request.search_type 
    maxCrawledPlacesPerSearch = process_request.maxCrawledPlacesPerSearch 
    customGeolocation_type =process_request.customGeolocation_type 
    


    results=search_google_maps(
    client =  client,
    latitude = latitude ,
    longitude = longitude ,
    distance_km =distance_km ,
    search_type = search_type ,
    maxCrawledPlacesPerSearch = maxCrawledPlacesPerSearch ,
    customGeolocation_type =customGeolocation_type ,
      )

    return results 