from starlette.applications import Starlette
from starlette.responses import JSONResponse
from fastai.vision import (
    open_image,
    load_learner
)
from pathlib import Path
from io import BytesIO
import requests
import os

path = Path("ml/images")
learn = load_learner(path)
app = Starlette()


@app.route("/classify-url", methods=["GET"])
async def classify_url(request):
    bytes = get_bytes(request.query_params["url"])
    return predict_image_from_bytes(bytes)


def get_bytes(url):
    response = requests.get(url)
    return response.content


def predict_image_from_bytes(bytes):
    img = open_image(BytesIO(bytes))
    _, _, losses = learn.predict(img)
    return JSONResponse({
        "predictions": sorted(
            zip(learn.data.classes, map(float, losses)),
            key=lambda p: p[1],
            reverse=True
        )
    })
