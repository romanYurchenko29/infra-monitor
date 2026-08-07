from prometheus_client import Counter, Histogram

REQUEST_COUNT = Counter(
    "http_requests_total",
    "Total HTTP requests",
)

REQUEST_LATENCY = Histogram(
    "http_request_duration_seconds",
    "Request latency",
)
