"""
FastAPI application entry point.
"""

from fastapi import FastAPI

from app.api.routes import router


app = FastAPI(
    title="IT Career Agent API",
    description="Production-ready AI Career Assistant",
    version="1.0.0",
)

app.include_router(router)