FROM python:3.11
WORKDIR /app

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

COPY ./requirements.txt /app
RUN pip install -r requirements.txt

COPY ./treemenu /app
COPY entrypoint.sh /app/entrypoint.sh
RUN chmod +x entrypoint.sh

ENTRYPOINT ["sh", "/app/entrypoint.sh"]
