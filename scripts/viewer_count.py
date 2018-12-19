import json
import os
import time
from sys import exit
from datetime import datetime

import requests

from private import TWITCH_CLIENT_ID
from private import TWITTER_CONSUMER_KEY, TWITTER_CONSUMER_SECRET
from private import TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_SECRET

TWITCH_API_VERSION = "v3"
TARGET_ACCOUNT = "worldsofzzt"
SCRIPT_DIR = os.path.dirname(os.path.realpath(__file__))
VIEWER_FILE = os.path.join(SCRIPT_DIR, "viewer.txt")


def main():
    while True:
        try:
            headers = {"Client-ID": TWITCH_CLIENT_ID,
                       "Accept": "application/vnd.twitchtv." +
                       TWITCH_API_VERSION + "+json"}
            r = requests.get("https://api.twitch.tv/kraken/streams/" + TARGET_ACCOUNT,
                             headers=headers)
            data = json.loads(r.text)
        except Exception as e:
            print(e)
            exit()

        if data.get("stream") is not None:
            viewers = data["stream"]["viewers"]
        else:
            viewers = "-"

        with open(VIEWER_FILE, "w") as fh:
            fh.write(str(viewers))
            print(str(datetime.now())[11:19], viewers)

        time.sleep(30)

    return True

if __name__ == "__main__":
    main()
