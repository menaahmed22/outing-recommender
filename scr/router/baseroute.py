from fastapi import FastAPI , APIRouter


base_router = APIRouter(
    prefix="/api/baseroute",
    tags=["baseroute"],
)
@base_router.get("/")
async def welcome():
    app_name = "Outing Recommender API"
    app_version = "1.0.0"

    return {
        "app_name": app_name,
        "app_version": app_version,
    }