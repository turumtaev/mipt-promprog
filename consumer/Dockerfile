FROM python:3

WORKDIR /app

ADD . /app

RUN pip install pika pymongo

CMD ["python", "consumer.py"]
