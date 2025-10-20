from fastapi import FastAPI

app = FastAPI(
    title="Right Time Campaigner API",
    description="Backend for the Right Time Campaigner system.",
    version="0.1.0"
)

@app.get("/api")
async def root():
    """
    Root endpoint for API health check.
    """
    return {"message": "Right Time Campaigner API is running."}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)