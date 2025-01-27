from datetime import datetime
from fastapi import FastAPI

app = FastAPI()


@app.get("/feed/")
def read_feed_starting(start_time: datetime = None):
    if start_time:
        return {"takeovers": f"Takeovers after {start_time}"}
    return {"takeovers": "All takeovers"}