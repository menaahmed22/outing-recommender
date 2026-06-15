import numpy as np
import pandas as pd 
import math 
from routes.schemas.data import ProcessRequest

def remove_closed_places(scrapped_data : pd.DataFrame ) -> pd.DataFrame  :

    cleaned_data = scrapped_data[~scrapped_data[['permanentlyClosed', 'temporarilyClosed']].any(axis=1)].copy()

    return cleaned_data

    
def drop_duplicates_data(scrapped_data : pd.DataFrame ) -> pd.DataFrame :

    cleaned_data=scrapped_data.drop_duplicates(subset=["placeId"])

    return cleaned_data


def drop_unneeded_columns(scrapped_data : pd.DataFrame ,
                           ) -> pd.DataFrame  :    

        cleaned_data= scrapped_data [['title',
                                  'categoryName',
                                  'categories',
                                  'totalScore',
                                  'address',
                                  'location',
                                  'phone',
                                  'floor',
                                  'menu',
                                  'placeId',
                                  'reviewsCount',
                                  'scrapedAt',
                                  'reserveTableUrl',
                                  'googleFoodUrl',
                                  'openingHours',
                                  'additionalInfo',
                                  'url',
                                  'rank',
                                  'searchString']]    
        return cleaned_data   


def replace_unknown_values(scrapped_data : pd.DataFrame ,
                           ) -> pd.DataFrame  : 

    cleaned_data=scrapped_data.copy()
    cleaned_data['googleFoodUrl'] = cleaned_data['googleFoodUrl'].replace([np.nan], ["Not Available"])
    cleaned_data['floor'] = cleaned_data['floor'].replace([np.nan], ["Not Available"])
    cleaned_data['menu'] = cleaned_data['menu'].replace([np.nan], ["Not Available"])
    cleaned_data['reserveTableUrl'] = cleaned_data['reserveTableUrl'].replace([np.nan], ["Not Available"])
    cleaned_data['openingHours'] = cleaned_data['openingHours'].replace([np.nan], ["Not Available"])
    cleaned_data['additionalInfo'] = cleaned_data['additionalInfo'].replace([np.nan], ["Not Available"]) 
    
    return cleaned_data                       



