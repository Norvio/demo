import os
import socket

from fastapi import FastAPI
from prometheus_client import Counter, make_asgi_app

VERSION = os.environ.get("APP_VERSION", "dev")
HELLOS = Counter("hello_requests_total", "Hello requests served")

app = FastAPI()
app.mount("/metrics", make_asgi_app())

@app.get("/")
def hello():
    HELLOS.inc()
    return {"message": "hello from norvio", "version": VERSION, "pod": socket.gethostname()}

@app.get("/healthz")
def healthz():
    return {"status": "ok"}

@app.get("/readyz")
def readyz():
    return {"status": "ready"}