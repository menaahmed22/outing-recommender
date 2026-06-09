from pydantic import BaseModel , Field
from typing import Optional, List

class ProcessRequest(BaseModel):
    latitude: float = Field(..., ge=-90, le=90)
    longitude: float = Field(..., ge=-180, le=180)
    distance_km: float = Field(..., ge=.5, le=10)
    search_type :str
    maxCrawledPlacesPerSearch: Optional[int] = Field(..., ge=1, le=10)
    customGeolocation_type :Optional[str] = "Polygon"
