
import io
import numpy as np
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import Response
from PIL import Image
from typing import Annotated
from fastapi import File

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

from transformers import CLIPProcessor, CLIPModel
# from PIL import Image
import requests

# load model
model = CLIPModel.from_pretrained("openai/clip-vit-base-patch32")
processor = CLIPProcessor.from_pretrained("openai/clip-vit-base-patch32")

# url = "http://images.cocodataset.org/val2017/000000039769.jpg"
# image = Image.open(requests.get(url, stream=True).raw)
# inp_lst = ["a photo of a cat", "a photo of a dog"]
# inputs = processor(text=inp_lst, images=image, return_tensors="pt", padding=True)

# outputs = model(**inputs)
# logits_per_image = outputs.logits_per_image # this is the image-text similarity score
# probs = logits_per_image.softmax(dim=1) # we can take the softmax to get the label probabilities
# dict_result = {i:j for i ,j in zip(inp_lst,probs.tolist()[0])}
# print(dict_result)

@app.post("/file")
async def create_file(file: Annotated[bytes, File()], text: str):
    img = Image.open(io.BytesIO(file))
    img = img.convert("RGB")
    img_np = np.array(img)
    inp_lst = text.split(",")
    inputs = processor(text=inp_lst, images=img_np, return_tensors="pt", padding=True)
    outputs = model(**inputs)
    logits_per_image = outputs.logits_per_image # this is the image-text similarity score
    probs = logits_per_image.softmax(dim=1) # we can take the softmax to get the label probabilities
    dict_result = {i:j for i ,j in zip(inp_lst,probs.tolist()[0])}
    print(dict_result)
    print(f"shape = {img_np.shape}")
    return {
        "clip_result": dict_result
	}

@app.get("/health")
async def health():
    return {"message": "ok"}
