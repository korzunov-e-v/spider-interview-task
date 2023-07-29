FROM python:3.10.0-alpine

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /code
COPY . /code/
RUN pip install -r requirements.txt
