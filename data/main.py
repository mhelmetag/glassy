"""Script for pulling frames from Surfline surfcams"""

import os
import time
import requests
import ffmpeg

SPOT_IDS = [
    "5842041f4e65fad6a7708966",  # Sandspit
    "584204204e65fad6a770904d",  # Mondos
    "584204214e65fad6a7709cfd",  # Ventura Point
    "584204214e65fad6a7709cfc",  # County Line
    "5cbde6df477f8600012f498d"  # Malibu
]

TIMESTAMP = int(time.time())
DATA_DIR = os.path.dirname(__file__)

for spot_id in SPOT_IDS:
    overview_url = f"https://services.surfline.com/kbyg/regions/overview?spotId={spot_id}"
    overview_response = requests.get(overview_url)
    json_overview_response = overview_response.json()

    spots_json = json_overview_response["data"]["spots"]
    spot = [s for s in spots_json if s["_id"] == spot_id][0]
    stream_url = spot["cameras"][0]["streamUrl"]

    ffmpeg_fileformat = os.path.join(
        DATA_DIR, f"stills/{TIMESTAMP}_{spot_id}_%02d.jpg")

    stream = ffmpeg.input(stream_url, t=30)
    stream = ffmpeg.filter(stream, 'fps', fps=1, round='down')
    stream = ffmpeg.output(stream, ffmpeg_fileformat)
    stream.run()

    print(f"Grabbed frames for spot {spot_id}")

print("Complete")
