from fastapi import  APIRouter ,Depends
from services.searchgooglemaps import search_google_maps
from .schemas.data import ProcessRequest
from helpers.dependencies import get_apify_client
import logging
from apify_client import ApifyClient
from services.preprocessing import preprocessing
import json
from fastapi import HTTPException



logger = logging.getLogger('api.search')
searchgooglemapsroute = APIRouter(
    prefix="/api/searchgooglemaps",
    tags=["searchgooglemaps"],
)
@searchgooglemapsroute.post("/")
async def searchgooglemaps(process_request : ProcessRequest ,client: ApifyClient = Depends(get_apify_client) ):
    latitude =process_request.latitude 
    longitude = process_request.longitude 
    distance_km =process_request.distance_km 
    search_type = process_request.search_type 
    maxCrawledPlacesPerSearch = process_request.maxCrawledPlacesPerSearch 
    customGeolocation_type =process_request.customGeolocation_type 
    
    try :

      results=search_google_maps(
      client =  client,
      latitude = latitude ,
      longitude = longitude ,
      distance_km =distance_km ,
      search_type = search_type ,
      maxCrawledPlacesPerSearch = maxCrawledPlacesPerSearch ,
      customGeolocation_type =customGeolocation_type ,
        )
      final_results=preprocessing(results,process_request,client = client)  
    



    except Exception  as e :
    #   # logger.error(f"Error while creating client: {e}")
      raise HTTPException(
              status_code=500,
              detail="Internal server error"
                  )
      # logger.exception("Search API failed")
      # return {"error": str(e)}

    # try :

    # except Exception  as e :
    #   logger.error(f"Error while processing data: {e}")

    return final_results 