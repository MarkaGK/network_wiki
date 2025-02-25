FROM python:3.12

RUN mkdir "app"

COPY requirements.txt /app

RUN pip install --upgrade pip

RUN pip install -r /app/requirements.txt

COPY ./src /app/

WORKDIR /app