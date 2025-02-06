import json
from datetime import datetime
import time
import feedRepository
import turfapi


def read_feed():
    try:
        connection = feedRepository.get_connection()
        feeed_read_info = feedRepository.get_latest_read_info(connection)
        last_time, last_zone_id = feeed_read_info

        feed = turfapi.fetch_feed_from_date_ordered_last_first(last_time)
        nrof_feed_items = len(feed)
        print(datetime.now(), "Number of feed items", nrof_feed_items, flush=True)

        if nrof_feed_items > 0:
            for feed_item in feed:
                takeover_time = datetime.strptime(feed_item["time"], "%Y-%m-%dT%H:%M:%S+0000")
                zone_id = feed_item["zone"]["id"]
                feedRepository.insert_takeover(connection, zone_id, takeover_time, json.dumps(feed_item, ensure_ascii=False))

            feedRepository.update_latest_read_info(connection, takeover_time, zone_id)
        connection.commit()
    except Exception as e:
        print(f"Error while trying to read feed: {e}")
        connection.rollback()
    finally:
        connection.close()


def feedcreator():
    print("Starting feed reader", flush=True)
    while True:
        read_feed()
        time.sleep(60)


if __name__ == '__main__':
    feedcreator()
