from fastapi import FastAPI

app = FastAPI()

@app.get("/healthz")
def health():
    return {"status": "ok"}

@app.get("/")
def root():
    return {
        "message": "Vigan's SRE Lab is running ✅",
        "stack": ["FastAPI", "Docker", "AWS ECS Fargate (soon)"]
    }
