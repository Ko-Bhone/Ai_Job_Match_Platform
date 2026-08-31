from fastapi import FastAPI

app = FastAPI(
    title="AI Job Match & Career Intelligence Platform",
    version = "1.0.0")

@app.get("/")
def root():
    return {"Message": "AI Job Match & Create API is Running..."}

@app.get("/health")
def health():
    return {"Message": "healthy" }