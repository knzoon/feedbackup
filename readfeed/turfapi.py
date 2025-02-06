import requests
import urllib.parse
from urllib.error import HTTPError

def fetchFeedFromDateOrderedLastFirst(lastDatetime):
    datetimeString = lastDatetime.strftime("%Y-%m-%dT%H:%M:%S+0000")
    encodedRequestStr = 'https://api.turfgame.com/unstable/feeds/takeover?afterDate=' + urllib.parse.quote(datetimeString)
    try:
        response = requests.get(encodedRequestStr)
        response.raise_for_status()
    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')  # Python 3.6
        return []
    except Exception as err:
        print(f'Other error occurred: {err}')  # Python 3.6
        return []
    else:
        feedFromApi = response.json()
        sortedFeed = sorted(feedFromApi, key=lambda fi: fi["time"])
        return sortedFeed
    
    

    