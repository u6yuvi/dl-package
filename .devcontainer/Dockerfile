#FROM mcr.microsoft.com/devcontainers/python:0-3.9
FROM u6yuvi/devcontainer_py39

# # RUN apt-get update -y && \
# #  	apt-get install -y make && \
# #  	apt-get install -y libffi-dev gcc && \
# # 	apt-get install -y python3-dev &&\
# #  	# for swagger
# #  	apt-get install -y curl &&\
# # 	apt-get install -y python3-pip

RUN pip3 install --upgrade pip

WORKDIR /workspace
#RUN pip3 install torch torchvision --no-cache-dir --index-url https://download.pytorch.org/whl/cpu

# #COPY . .
#COPY requirements.txt .

COPY ../ /workspace/

RUN pip3 install -r /workspace/requirements.txt

RUN pip3 install -e /workspace/.

#RUN pip install hydra_colorlog
#  python train.py --resume

