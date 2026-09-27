from fastapi import FastAPI
from app.api.router import api_router

app = FastAPI(
    title="AI Job Match Platform",
    version="1.0.0"
)

@app.get("/")
def root():
    return {"Message" : "AI Job Match Platform is Running...."}

@app.get("/health")
def health_check():
    return {"status" : "Healthy"}

app.include_router(api_router, prefix="/api/v1")