FROM ubuntu:14.04
RUN apt-get update && apt-get install -y \
    python3 \
    python3-dev \
    python3-pip \
    python3-psycopg2 \
    install python3-scipy \
    libpq-dev \
    libgdal-dev

RUN mkdir /code
WORKDIR /code
ADD . .
RUN pip3 install -r requirements.txt