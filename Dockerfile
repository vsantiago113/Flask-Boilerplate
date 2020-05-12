FROM python:3.8-slim

WORKDIR /web_app

ENV FLASK_APP application
ENV FLASK_RUN_HOST 0.0.0.0
ENV FLASK_RUN_PORT 5000

COPY . /web_app

RUN pip install --no-cache-dir --quiet -r requirements.txt
RUN pip install -e .

CMD ["flask", "run"]
