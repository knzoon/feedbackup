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


@app.get("/feed/takeover")
def read_feed_starting(after: datetime = None):
    if after:
        db_rows = feedRepository.read_takeover_feed_after_specified_time(after)
    else:
        db_rows = feedRepository.read_takeover_feed_from_beginning()

    cut_off_index = get_index_of_last_unbroken_takeovertime(db_rows)
    result = []

    for (takeover_time, original_takeover) in db_rows[:cut_off_index + 1]:
        result.append(json.loads(original_takeover))

    return result


@app.get("/feed/zone")
def read_feed_starting(after: datetime = None):
    if after:
        db_rows = feedRepository.read_zone_feed_after_specified_time(after)
    else:
        db_rows = feedRepository.read_zone_feed_from_beginning()

    cut_off_index = get_index_of_last_unbroken_takeovertime(db_rows)
    result = []

    for (takeover_time, original_takeover) in db_rows[:cut_off_index + 1]:
        result.append(json.loads(original_takeover))

    return result
