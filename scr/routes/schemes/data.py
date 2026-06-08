from pydantic import BaseModel
from typing import Optional, List

class ProcessRequest(BaseModel):
    latitude: float
    longitude: float
    distance_km: float = 5 
    search_type :str
    maxCrawledPlacesPerSearch: Optional[int] = 5
    customGeolocation_type :Optional[str] = "Polygon"
