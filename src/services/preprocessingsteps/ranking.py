import pandas as pd 
import numpy as np
import math
from routes.schemas.data import ProcessRequest

def create_ranks(scrapped_data : pd.DataFrame ,
                 process_request : ProcessRequest ,) -> pd.DataFrame  :

    max_distance = process_request.distance_km
    cleaned_data=scrapped_data.copy()
    # Fill None values in 'reviewsCount' with 0 and convert to numeric
    cleaned_data['reviewsCount'] = pd.to_numeric(cleaned_data['reviewsCount'].fillna(0), errors='coerce')
    max_reviews = cleaned_data["reviewsCount"].max()

    #calculate scores
    cleaned_data["DistanceScore"] = 1 - (cleaned_data["distance_km"] / max_distance)

    # Fill None values in 'totalScore' with 0 and convert to numeric
    cleaned_data['totalScore'] = pd.to_numeric(cleaned_data['totalScore'].fillna(0), errors='coerce')
    cleaned_data["RatingScore"] = cleaned_data["totalScore"] / 5

    cleaned_data["ReviewScore"] = (
        np.log1p(cleaned_data["reviewsCount"])
        / np.log1p(max_reviews + 1e-9) # Add a small epsilon to avoid log(0) if max_reviews is 0
    )

    cleaned_data["OverallRank"] = round((
        0.5 * cleaned_data["DistanceScore"]
        + 0.3 * cleaned_data["RatingScore"]
        + 0.2 * cleaned_data["ReviewScore"]
    )*10 ,2)

    return cleaned_data