from fastapi import FastAPI
from app.services import get_health, get_metrics, get_service_info

app = FastAPI(title="Infrastructure Monitoring Service", version="1.0.0")


@app.get("/")
def root():
    return get_service_info()


@app.get("/health")
def health():
    return get_health()


@app.get("/metrics")
def metrics():
    return get_metrics()
