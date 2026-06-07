from fastapi import FastAPI , APIRouter
from services.searchgooglemaps import search_google_maps

searchgooglemapsroute = APIRouter(
    prefix="/api/searchgooglemapsroute",
    tags=["searchgooglemapsroute"],
)
@searchgooglemapsroute.post("/")
async def searchgooglemaps():
    results=search_google_maps()

    return results