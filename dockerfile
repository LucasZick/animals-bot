FROM python:alpine

WORKDIR /animals_bot

COPY . .

RUN pip3 install --no-cache -r requirements.txt

# Usado para manter o log do python
ENV PYTHONUNBUFFERED 1

ENV API_KEY ''
ENV API_SECRET_KEY ''
ENV ACCESS_KEY ''
ENV ACCESS_SECRET ''

ENV REDIS_URL 'redis://172.17.0.1:6379'

ENV LOOKUP_TIMEOUT '30'
ENV LOGLEVEL 'INFO'
ENV PORT '3030'
ENV TEST ''


CMD [ "python3", "app.py" ]
