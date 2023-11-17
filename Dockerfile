FROM python:3.11
WORKDIR /app

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

COPY ./requirements.txt /app
RUN pip install -r requirements.txt

COPY ./treemenu /app