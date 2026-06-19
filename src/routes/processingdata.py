# from fastapi import  APIRouter ,Depends
# from services.preprocessing import preprocessing
# from .schemas.data import ProcessRequest
# from helpers.dependencies import get_apify_client
# import logging
# # from apify_client import ApifyClient


# logger = logging.getlogger('api.preprocessing')
# processingroute = APIRouter(
#     prefix="/api/processingdata",
#     tags=["processingdata"],
# )
# @processingdata.post("/")
# async def processingdata( process_request : ProcessRequest ,client: ApifyClient = Depends(get_apify_client) ):
#     latitude =process_request.latitude 
#     longitude = process_request.longitude 
#     distance_km =process_request.distance_km 
#     search_type = process_request.search_type 
#     maxCrawledPlacesPerSearch = process_request.maxCrawledPlacesPerSearch 
#     customGeolocation_type =process_request.customGeolocation_type 
    
#     try :

#       results=preprocessing(
#       scrapped_data=scrapped_data,
#       client =  client,
#       latitude = latitude ,
#       longitude = longitude ,
#       distance_km =distance_km ,
#       search_type = search_type ,
#       maxCrawledPlacesPerSearch = maxCrawledPlacesPerSearch ,
#       customGeolocation_type =customGeolocation_type ,
#         )

#     except Exception  as e :
#       logger.error(f"Error while processing data: {e}")

#     return results 