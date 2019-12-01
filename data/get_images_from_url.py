"""Script for pulling images from a video stream via URL (like a Surfline cam rewind)"""

import os
import time
import requests
import ffmpeg

TIMESTAMP = int(time.time())
DATA_DIR = os.path.dirname(__file__)
URL = "https://camrewinds.cdn-surfline.com/live/wc-southoceanbeach.stream.20191125T201826428.mp4"
SPOT_ID = "20191125T201826428"

ffmpeg_fileformat = os.path.join(
    DATA_DIR, f"images/{TIMESTAMP}_{SPOT_ID}_%02d.jpg")

stream = ffmpeg.input(URL, t=30)
stream = ffmpeg.filter(stream, 'fps', fps=1, round='down')
stream = ffmpeg.output(stream, ffmpeg_fileformat)
stream.run()

print("Complete")
