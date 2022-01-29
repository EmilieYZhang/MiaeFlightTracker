import requests
from api.config import settings

ROOT_URL = settings.ROOT_URL
# environment variable


def states_accessor():
    # Go through the doc api examples!
    url = f"{ROOT_URL}/states/all"
    r = requests.get(url)
    # json is a dictionary
    if not r.ok:
        # raise error if not found
        raise RuntimeError(r.json())
    print(r.json())


def tracks_accessor():
    url = f"{ROOT_URL}/tracks/all?icao24=3c4b26&time=0"
    # not updated because open source api, so doesn't work
    r = requests.get(url)
    # json is a dictionary
    if not r.ok:
        # raise error if not found
        raise RuntimeError(r.json())
    print(r.json())

