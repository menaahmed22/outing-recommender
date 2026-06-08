from apify_client import ApifyClient
import pandas as pd
import numpy as np
from helpers.config import Apify_api
import math
from typing import List

def bounding_box(latitude :float , longitude :float , distance_km :float =5):
    half = distance_km / 2

    delta_lat = half / 111  # 111 Km = 1 degree of latitude
    delta_lon = half / (111 * math.cos(math.radians(latitude))) # 111 Km = 1 degree of longitude at the equator, adjusted for latitude

    return {
        "min_lat": latitude - delta_lat,
        "max_lat": latitude + delta_lat,
        "min_lon": longitude - delta_lon,
        "max_lon": longitude + delta_lon,
    }
# bbox = bounding_box(latitude,longitude)
#30.4652, 31.1869, 3
# polygon = [
#         [
#             [bbox["min_lon"], bbox["min_lat"]],
#             [bbox["max_lon"], bbox["min_lat"]],
#             [bbox["max_lon"], bbox["max_lat"]],
#             [bbox["min_lon"], bbox["max_lat"]],
#             [bbox["min_lon"], bbox["min_lat"]],
#         ]
#     ]
def search_google_maps( 
    latitude : float ,
    longitude : float ,
    distance_km : float = 5 ,
    search_type : str = "restaurant" ,
    maxCrawledPlacesPerSearch : int = 5  ,
    customGeolocation_type : str = 'Polygon' ,

    ) :

    client = ApifyClient(Apify_api)
    bbox = bounding_box(latitude,longitude,distance_km)
    polygon = [
        [
            [bbox["min_lon"], bbox["min_lat"]],
            [bbox["max_lon"], bbox["min_lat"]],
            [bbox["max_lon"], bbox["max_lat"]],
            [bbox["min_lon"], bbox["max_lat"]],
            [bbox["min_lon"], bbox["min_lat"]],
        ]
    ]
    run_input = {
        "searchStringsArray": [search_type],
        # "locationQuery": "Benha , Egypt",
        "maxCrawledPlacesPerSearch": maxCrawledPlacesPerSearch,
       
        "customGeolocation": {
            "type": customGeolocation_type,
            "coordinates": polygon
        }

    }

    # Run the Actor and wait for it to finish
    run = client.actor("compass/crawler-google-places").call(run_input=run_input)
    dataset_id = run.default_dataset_id
    data = list(
            client.dataset(dataset_id).iterate_items()
        )


    scrapped=pd.DataFrame(data)
    # scrapped = scrapped.where(pd.notnull(scrapped), None)  #to replace all NAN 
    scrapped = scrapped.astype(object)
    scrapped = scrapped.replace([np.nan], [None])
    import json

    json.dumps(scrapped.to_dict(orient="records"), allow_nan=False)
    # print(scrapped.to_dict(orient="records")[0])
    return scrapped.to_dict(orient="records")