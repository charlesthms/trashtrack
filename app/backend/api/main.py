from typing import Union
from fastapi import APIRouter
from api.routes import trashes


api_router = APIRouter()
api_router.include_router(trashes.router, prefix="/trashes", tags=["Trashes routes"])
