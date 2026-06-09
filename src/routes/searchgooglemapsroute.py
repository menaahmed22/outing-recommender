from fastapi import FastAPI , APIRouter
from services.searchgooglemaps import search_google_maps
from .schemas.data import ProcessRequest

searchgooglemapsroute = APIRouter(
    prefix="/api/searchgooglemapsroute",
    tags=["searchgooglemapsroute"],
)
@searchgooglemapsroute.post("/")
async def searchgooglemaps(process_request : ProcessRequest):

    latitude =process_request.latitude 
    longitude = process_request.longitude 
    distance_km =process_request.distance_km 
    search_type = process_request.search_type 
    maxCrawledPlacesPerSearch = process_request.maxCrawledPlacesPerSearch 
    customGeolocation_type =process_request.customGeolocation_type 


    results=search_google_maps(latitude = latitude ,
    longitude = longitude ,
    distance_km =distance_km ,
    search_type = search_type ,
    maxCrawledPlacesPerSearch = maxCrawledPlacesPerSearch ,
    customGeolocation_type =customGeolocation_type ,
      )

    return results