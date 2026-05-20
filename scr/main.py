from fastapi import FastAPI
from .router.baseroute import base_router

app = FastAPI()
#uvicorn main:app --reload --host 0.0.0.0 --port 5000
app.include_router(base_router)

