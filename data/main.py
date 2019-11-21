"Script for pulling frames from Surfline surfcams"
# pull still rewindClip (later shift to camera stream from streamUrl as it's shorter, less space)
# only pull stills from cams with nighttime is false && status.isDown is false

import os
import time
import requests
import cv2

SPOT_IDS = [
    "5842041f4e65fad6a7708966",  # Sandspit
    "5842041f4e65fad6a770896c",  # Campus Point
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
    rewind_url = spot["cameras"][0]["rewindClip"]

    vidcap = vidcap = cv2.VideoCapture(rewind_url)
    success, image = vidcap.read()
    filepath = os.path.join(
        DATA_DIR, f"stills/{TIMESTAMP}_{spot_id}_001.jpg")
    cv2.imwrite(filepath, image)

    print(f"Grabbed frame for spot {spot_id}")
