from datetime import datetime
from fastapi import FastAPI
import feedRepository
import json

app = FastAPI()


def get_index_of_last_unbroken_takeovertime(takeovers):
    if takeovers:
        i = len(takeovers) - 1
        last_takeover_time = takeovers[i][0]

        while (i >= 0):
            if takeovers[i][0] < last_takeover_time:
                return i
            i -= 1
        return -1
    return -1


@app.get("/feed")
def read_feed_starting(start_time: datetime = None):
    if start_time:
        db_rows = feedRepository.read_feed_after_specified_time(start_time)
    else:
        db_rows = feedRepository.read_feed_from_beginning()

    cut_off_index = get_index_of_last_unbroken_takeovertime(db_rows)
    result = []

    for (takeover_time, original_takeover) in db_rows[:cut_off_index + 1]:
        result.append(json.loads(original_takeover))

    return result
