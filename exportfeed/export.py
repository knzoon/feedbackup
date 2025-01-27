from datetime import datetime
from fastapi import FastAPI
import feedRepository
import json

app = FastAPI()


@app.get("/feed/")
def read_feed_starting(start_time: datetime = None):
    if start_time:
        return {"takeovers": f"Takeovers after {start_time}"}

    db_rows = feedRepository.read_feed_from()
    result = []

    for (takeover_time, original_takeover) in db_rows:
        result.append(json.loads(original_takeover))

    return result
