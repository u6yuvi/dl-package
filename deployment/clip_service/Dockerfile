FROM python:3.9

WORKDIR /code

RUN pip3 install torch torchvision  --no-cache-dir --index-url https://download.pytorch.org/whl/cpu \
    && rm -rf /root/.cache/pip

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./clip_fastapi.py /code/

CMD ["uvicorn", "clip_fastapi:app", "--host", "0.0.0.0", "--port", "80"]