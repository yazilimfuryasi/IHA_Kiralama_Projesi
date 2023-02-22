FROM python:3.10

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /ihakirala

COPY requirements.txt /ihakirala/

RUN pip install -r requirements.txt

COPY . .