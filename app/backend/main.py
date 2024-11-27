from typing import Union
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from core import config
from api.main import api_router

app = FastAPI(title=config.PROJECT_NAME, docs_url="/api/docs")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(api_router, prefix=config.API_V1_STR)
