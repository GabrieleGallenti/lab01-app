from fastapi import FastAPI, HTTPException
from prometheus_fastapi_instrumentator import Instrumentator

app = FastAPI()

Instrumentator().instrument(app).expose(app)


@app.get("/work")
def work():
    return {"ok": True}

@app.get("/health")
def health():
    return {"status": "ok", "version": "1.1"}

@app.get("/fail")
def fail():
    raise HTTPException(status_code=500, detail="errore di prova")