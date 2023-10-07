FROM python:3.9

WORKDIR /code

# RUN pip3 install torch torchvision==0.15.2 torchaudio --extra-index-url https://download.pytorch.org/whl/cpu

RUN pip install 'transformers[torch]'

RUN rm -rf /root/.cache/pip

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./server.py /code/

CMD ["uvicorn", "server:app", "--host", "0.0.0.0", "--port", "90"]  