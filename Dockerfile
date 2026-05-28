FROM python:3.12-slim

WORKDIR /app

RUN apt-get update && apt-get install -y \
    build-essential \
    libjpeg-dev \
    zlib1g-dev

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

RUN DJANGO_SECRET_KEY=dummy python manage.py collectstatic --noinput

EXPOSE 8000

CMD gunicorn knu_games.wsgi:application --bind 0.0.0.0:8000