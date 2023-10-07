# import urllib
import io
import os
# import zlib
import json

import redis

# import torch
# import timm
import numpy as np

from transformers import pipeline, set_seed

from fastapi import FastAPI, File, Depends
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import Response

from typing import Dict, Annotated

app = FastAPI(title="Model Server")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

GPT_MODEL = os.environ.get("TIMM_MODEL", "gpt2")
REDIS_HOST = os.environ.get("REDIS_HOST", "localhost")
REDIS_PORT = os.environ.get("REDIS_PORT", "6379")
REDIS_PASSWORD = os.environ.get("REDIS_PASSWORD", "")

@app.on_event("startup")
async def initialize():
    # initializes model, categories, redis connection
    global model
    print(f"loading model {GPT_MODEL=}...")
    model = pipeline('text-generation', model=GPT_MODEL)
    # model.eval()
    print(f"loaded model {GPT_MODEL=}")

    # global categories
    # # Download human-readable labels for ImageNet.
    # # get the classnames
    # url, filename = (
    #     "https://raw.githubusercontent.com/pytorch/hub/master/imagenet_classes.txt",
    #     "imagenet_classes.txt",
    # )
    # urllib.request.urlretrieve(url, filename)
    # with open("imagenet_classes.txt", "r") as f:
    #     categories = [s.strip() for s in f.readlines()]

    global redis_pool
    print(f"creating redis connection with {REDIS_HOST=} {REDIS_PORT=}")
    redis_pool = redis.ConnectionPool(
        host=REDIS_HOST, port=REDIS_PORT, password=REDIS_PASSWORD, db=0, decode_responses=True
    )

def get_redis():
    # Here, we re-use our connection pool
    # not creating a new one
    return redis.Redis(connection_pool=redis_pool)

def predict(inp_text: str) -> Dict[str, float]:
    # config = resolve_data_config({}, model=GPT_MODEL)
    # transform = create_transform(**config)

    # img_tensor = transform(inp_img).unsqueeze(0)  # transform and add batch dimension

    # # inference
    # with torch.no_grad():
    #     out = model(img_tensor)
    #     probabilities = torch.nn.functional.softmax(out[0], dim=0)
    #     confidences = {categories[i]: float(probabilities[i]) for i in range(1000)}

    # return confidences

    set_seed(42)
    result = model(inp_text, max_length=30, num_return_sequences=5)
    return result


# async def write_to_cache(file: File, result: Dict[str, float]) -> None:
#     cache = get_redis()

#     # hash = zlib.adler32(file)
#     cache.set(file, json.dumps(result))

@app.post("/infer")
async def infer(inpt_text):
    #img: Image.Image = Image.open(io.BytesIO(image))
    #img = img.convert("RGB")

    predictions = predict(inpt_text)

    # top10 = {
    #     k: v
    #     for k, v in list(sorted(predictions.items(), key=lambda x: x[1], reverse=True))[
    #         :10
    #     ]
    # }

    # await write_to_cache(inpt_text, predictions)

    return predictions

# uvicorn server:app --host 0.0.0.0 --port 8000 --reload