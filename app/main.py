from fastapi import FastAPI
from prometheus_fastapi_instrumentator import Instrumentator

app = FastAPI()

Instrumentator().instrument(app).expose(app)


@app.get("/work")
def work():
    return {"ok": True}

@app.get("/health")
def health():
    return {"status": "ok", "version": "1.1"}
