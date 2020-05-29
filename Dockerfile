FROM python:3.8-slim

WORKDIR /web_app

COPY . /web_app

RUN pip install --no-cache-dir --quiet -r requirements.txt
