import json
from datetime import datetime
import time
import feedRepository
import turfapi


def read_feed():
    try:
        connection = feedRepository.getConnection()
        feeedReadInfo = feedRepository.getLatestReadInfo(connection)
        lastTime, lastZoneId, lastHighestOrder = feeedReadInfo

        feed = turfapi.fetchFeedFromDateOrderedLastFirst(lastTime)
        nrofFeedItems = len(feed)
        print(datetime.now(), "Number of feed items", nrofFeedItems, flush=True)

        if nrofFeedItems > 0:
            for feedItem in feed:
                lastHighestOrder += 1
                takeoverTime = datetime.strptime(feedItem["time"], "%Y-%m-%dT%H:%M:%S+0000")
                zoneId = feedItem["zone"]["id"]
                feedRepository.insertTakever(connection, lastHighestOrder, takeoverTime, json.dumps(feedItem, ensure_ascii=False))

            feedRepository.updateLatestReadInfo(connection, takeoverTime, zoneId, lastHighestOrder)
        connection.commit()
    except Exception as e:
        print(f"Error while trying to read feed: {e}")
        connection.rollback()
    finally:
        connection.close()


def feedcreator():
    print("Starting feed reader 3:d try", flush=True)
    while True:
        read_feed()
        time.sleep(60)



if __name__ == '__main__':
    feedcreator()
