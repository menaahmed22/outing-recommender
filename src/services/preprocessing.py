from routes.schemas.data import ProcessRequest
from .preprocessingsteps.validation import validate_scrapped_data , validate_scrapped_data_distance
from .preprocessingsteps.cleaning import remove_closed_places,drop_duplicates_data,drop_unneeded_columns ,replace_unknown_values
from .preprocessingsteps.calculating_distance import seperate_lat_lan ,calculate_distance_km
from .preprocessingsteps.ranking import create_ranks
import pandas as pd
from apify_client import ApifyClient
import json 


def preprocessing (scrapped_data : pd.DataFrame ,
                           process_request : ProcessRequest ,client : ApifyClient ) -> pd.DataFrame  :

    final_output =validate_scrapped_data(scrapped_data,process_request)
    final_output =remove_closed_places (final_output)
    final_output =drop_duplicates_data (final_output)
    final_output = drop_unneeded_columns(final_output)
    final_output =seperate_lat_lan(final_output)
    final_output =calculate_distance_km(final_output,process_request)
    final_output =validate_scrapped_data_distance(final_output,process_request)
    final_output =create_ranks(final_output,process_request)
    final_output =replace_unknown_values(final_output)
    final_output = final_output.sort_values(by="OverallRank",ascending=False)
    final_output = final_output.nlargest(process_request.count_of_results, 'OverallRank')
    final_output = final_output.astype(object).where(pd.notnull(final_output), None)
    final_output = final_output.to_dict(orient="records")
    return final_output