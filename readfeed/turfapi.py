import requests
import urllib.parse
from urllib.error import HTTPError


def fetch_feed_from_date_ordered_last_first(last_datetime):
    datetime_string = last_datetime.strftime("%Y-%m-%dT%H:%M:%S+0000")
    encoded_request_str = ('https://api.turfgame.com/v5/feeds?afterDate='
                           + urllib.parse.quote(datetime_string))
    try:
        response = requests.get(encoded_request_str)
        response.raise_for_status()
    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')  # Python 3.6
        return []
    except Exception as err:
        print(f'Other error occurred: {err}')  # Python 3.6
        return []
    else:
        feed_from_api = response.json()
        sorted_feed = sorted(feed_from_api, key=lambda fi: fi["time"])
        return sorted_feed
