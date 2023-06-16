FROM python:3.9.16-slim-buster

RUN apt-get update -y && \
 	apt-get install -y make && \
 	apt-get install -y libffi-dev gcc && \
 	# for swagger
 	apt-get install -y curl

RUN pip3 install torch torchvision --no-cache-dir --index-url https://download.pytorch.org/whl/cpu

# COPY ../requirements.txt ./workspace/

#RUN pip3 install -r ./workspace/requirements.txt
