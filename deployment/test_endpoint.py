
import requests
import ast

request_cnt = 100

def test_gpt_endpoint():


    url = "http://0.0.0.0:80/infer"

    
    headers = {
    'Content-Type': 'application/x-www-form-urlencoded'
    }

    text = "Harry-Potter"
    for i in range(request_cnt):
        payload = f'text={text}'
        response = requests.request("GET", url, headers=headers, data=payload)
        text = response.text


def test_vit_endpoint():


    url = "http://0.0.0.0:80/infer"

    
    headers = {
    'Content-Type': 'application/x-www-form-urlencoded'
    }

    text = "Harry-Potter"
    for i in range(request_cnt):
        payload = f'text={text}'
        response = requests.request("GET", url, headers=headers, data=payload)
        text = response.text


import requests

url = "http://0.0.0.0:80/infer"

payload = {}

for i in range(request_cnt):
    files=[
    ('image',('photo-1559268950-2d7ceb2efa3a.jpeg',open('deployment/photo-1606567595334-d39972c85dbe.jpeg','rb'),'image/jpeg'))
    ]
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload, files=files)

    assert len(ast.literal_eval(response.text).keys())==10 # cifar10 number of labels i.e 10