import numpy as np
import pandas as pd 
import math 
from routes.schemas.data import ProcessRequest


def validate_scrapped_data(scrapped_data : pd.DataFrame ,
                           process_request : ProcessRequest ) -> pd.DataFrame  :

    validated_data=scrapped_data.dropna(subset=["title"]) #drop all empty resonses
    validated_data = validated_data[validated_data['searchString'].isin([process_request.search_type])] # validate that all scrapped places match the requested search type
   
    return validated_data

def validate_scrapped_data_distance(scrapped_data : pd.DataFrame ,
                           process_request : ProcessRequest ) -> pd.DataFrame  :

    validated_data=scrapped_data[scrapped_data['distance_km'] < process_request.distance_km]
   
    return validated_data    



