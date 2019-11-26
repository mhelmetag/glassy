FROM python:3.7

WORKDIR /app

RUN useradd -m web
USER web

COPY requirements.txt /app
RUN pip install -r requirements.txt

COPY . /app

RUN pip install /app

EXPOSE 8000

CMD uvicorn web:app -p $PORT
