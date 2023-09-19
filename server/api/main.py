from .database import engine
from api import models, host, cpu_data, rxpkt, metrics

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

models.Base.metadata.create_all(bind=engine)

gateway = FastAPI()

origins = [
    "http://localhost:5173",
]

gateway.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

gateway.include_router(host.router, tags=["Host"], prefix="/hosts")
gateway.include_router(cpu_data.router, tags=["CPU Data"], prefix="/cpu-data")
gateway.include_router(rxpkt.router, tags=["RXPkt"], prefix="/rxpkt")
gateway.include_router(metrics.router, tags=["Metrics"], prefix="/metrics")

@gateway.get("/")
def root() -> dict:
    return { "message": "Hello, World!" }
