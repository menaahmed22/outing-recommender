import pandas as pd
import numpy as np
import math
from typing import List
import json
from apify_client import ApifyClient
from helpers.config import Apify_api



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


def search_google_maps( 
    client : ApifyClient ,
    latitude : float ,
    longitude : float ,
    distance_km : float = 5 ,
    search_type : str = "restaurant" ,
    maxCrawledPlacesPerSearch : int = 5  ,
    customGeolocation_type : str = 'Polygon' ,
    
    ) :

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


    scrapped_data=pd.DataFrame(data)
    scrapped_data = scrapped_data.astype(object)
    scrapped_data = scrapped_data.replace([np.nan], [None])

    json.dumps(scrapped_data.to_dict(orient="records"), allow_nan=False)
    return scrapped_data.to_dict(orient="records")