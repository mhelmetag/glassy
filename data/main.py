"Script for pulling frames from Surfline surfcams for machine learing"
# using region overview
# filter to spot
# pull still rewindClip (later shift to camera stream from streamUrl as it's shorter, less space)
# only pull stills from cams with nighttime is false && status.isDown is false

import requests
import cv2

# https://www.surfline.com/surf-report/sandspit/5842041f4e65fad6a7708966
SPOT_IDS = ["5842041f4e65fad6a7708966"]

for spot_id in SPOT_IDS:
    overview_response = requests.get(
        f"https://services.surfline.com/kbyg/regions/overview?spotId={spot_id}")
    json_overview_response = overview_response.json()

    spots_json = json_overview_response["data"]["spots"]
    spot = [s for s in spots_json if s["_id"] == spot_id][0]

    print(spot)

    rewind_url = spot["cameras"][0]["rewindClip"]
    stream_file = open("/Users/max/Downloads/test.mp4", "wb")
    stream_response = requests.get(rewind_url)
    stream_file.write(stream_response.content)
    stream_file.close()

    vidcap = vidcap = cv2.VideoCapture(stream_file.name)
    success, image = vidcap.read()
    cv2.imwrite("/Users/max/Downloads/test.jpg", image)
