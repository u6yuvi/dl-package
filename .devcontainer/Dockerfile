FROM mcr.microsoft.com/devcontainers/python:0-3.9

# RUN apt-get update -y && \
#  	apt-get install -y make && \
#  	apt-get install -y libffi-dev gcc && \
# 	apt-get install -y python3-dev &&\
#  	# for swagger
#  	apt-get install -y curl &&\
# 	apt-get install -y python3-pip


# Install Docker CE CLI
# RUN apt-get update \
#   && apt-get install -y apt-transport-https ca-certificates curl gnupg2 lsb-release \
#   && curl -fsSL https://download.docker.com/linux/$(lsb_release -is | tr '[:upper:]' '[:lower:]')/gpg | apt-key add - 2>/dev/null \
#   && echo "deb [arch=amd64] https://download.docker.com/linux/$(lsb_release -is | tr '[:upper:]' '[:lower:]') $(lsb_release -cs) stable" | tee /​etc​/apt/sources.list.d/docker.list \
#   && apt-get update \
#   && apt-get install -y docker-ce-cli

# Install Docker Compose
# RUN export LATEST_COMPOSE_VERSION=$(curl -sSL "https://api.github.com/repos/docker/compose/releases/latest" | grep -o -P '(?<="tag_name": ").+(?=")') \
#   && curl -sSL "https://github.com/docker/compose/releases/download/${LATEST_COMPOSE_VERSION}/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose \
#   && chmod +x /usr/local/bin/docker-compose

WORKDIR /workspace
#RUN pip3 install torch torchvision --no-cache-dir --index-url https://download.pytorch.org/whl/cpu

#COPY . .
# COPY ../requirements.txt ./workspace/

# RUN pip3 install -r ./workspace/requirements.txt
