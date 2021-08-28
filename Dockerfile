# Set the base image and keep tag version as an argument

ARG BASE_VERSION=3.10-rc-bullseye
FROM python:${BASE_VERSION}

# Set labels for defining metadata of the image

LABEL version="1.x.x"
LABEL author="Supriyo Debnath"
LABEL title="Purchase Management API"
LABEL description="Puchase Management API with MySQL as backend"

# Enable Python buffers/output to be sent to container logs

ENV PYTHONUNBUFFERED=1

# Install required packages non-interactively

ARG DEBIAN_FRONTEND=noninteractive
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
            default-libmysqlclient-dev \
            build-essential \
            tar

# Set Workdirectory and pull the files from host
# The build source is expected to have the Dockerfile and the app archive which contains the manage.py & requirements.txt 

RUN mkdir /workspace
WORKDIR /workspace
ARG APP_LABEL=puchase_mysql_api
COPY ${APP_LABEL}.tar.gz ./
RUN tar -xzvf ${APP_LABEL}.tar.gz
WORKDIR /workspace/source
RUN pwd && ls

# Install dependencies & run management commands

RUN pip install -r requirements.txt
RUN python3 manage.py check
RUN python3 manage.py collectstatic
RUN mkdir media

# Expose application port

EXPOSE 8000

# Persist media folder

VOLUME /workspace/source/media

# Run Django App

ENTRYPOINT ["python3", "manage.py"]
CMD ["runserver", "0.0.0.0:8000", "--noreload"]

