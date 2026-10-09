from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Final Docker practice"}

@app.get("/health")
def health():
    return {"status": "healthy"}