import pandas as pd
import numpy as np
from math import radians, sin, cos, sqrt, atan2
from routes.schemas.data import ProcessRequest

def seperate_lat_lan(scrapped_data : pd.DataFrame ,
                           ) -> pd.DataFrame  : 

    cleaned_data= scrapped_data.copy()   
    cleaned_data['latitude'] = cleaned_data['location'].apply(lambda x: x.get('lat') if isinstance(x, dict) else None)
    cleaned_data['longitude'] = cleaned_data['location'].apply(lambda x: x.get('lng') if isinstance(x, dict) else None)
    return cleaned_data


def haversine_distance(lat1, lon1, lat2, lon2): #the Haversine formula. It computes the shortest distance over the Earth's curved surface
    R = 6371  # Radius of Earth in kilometers

    lat1_rad = radians(lat1)
    lon1_rad = radians(lon1)
    lat2_rad = radians(lat2)
    lon2_rad = radians(lon2)

    dlon = lon2_rad - lon1_rad
    dlat = lat2_rad - lat1_rad

    a = sin(dlat / 2)**2 + cos(lat1_rad) * cos(lat2_rad) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    distance = R * c
    return distance


def calculate_distance_km(scrapped_data : pd.DataFrame ,
                           process_request : ProcessRequest ) ->  pd.DataFrame  :
    cleaned_data= scrapped_data.copy() 
    cleaned_data['distance_km'] = cleaned_data.apply(lambda row: haversine_distance(
        process_request.latitude, process_request.longitude,
        row['latitude'], row['longitude']
    ), axis=1)    

    return cleaned_data