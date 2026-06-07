from fastapi import FastAPI
from router.baseroute import base_router
from router.searchgooglemapsroute import searchgooglemapsroute

app = FastAPI()
#uvicorn main:app --reload --host 0.0.0.0 --port 5000
app.include_router(base_router)
app.include_router(searchgooglemapsroute)
