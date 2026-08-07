from fastapi import FastAPI
from time import perf_counter

from fastapi import FastAPI, Request
from fastapi.responses import Response
from prometheus_client import CONTENT_TYPE_LATEST, generate_latest

from app.metrics import REQUEST_COUNT, REQUEST_LATENCY
from app.services import get_health, get_metrics, get_service_info

app = FastAPI(title="Infrastructure Monitoring Service", version="1.0.0")


@app.middleware("http")
async def metrics_middleware(request: Request, call_next):
    start = perf_counter()

    response = await call_next(request)

    REQUEST_COUNT.inc()
    REQUEST_LATENCY.observe(perf_counter() - start)

    return response


@app.get("/")
def root():
    return get_service_info()


@app.get("/metrics")
def metrics():
    return Response(
        generate_latest(),
        media_type=CONTENT_TYPE_LATEST,
    )


@app.get("/health")
def health():
    return get_health()


@app.get("/metrics")
def metrics():
    return get_metrics()
