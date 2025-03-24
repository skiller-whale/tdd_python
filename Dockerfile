FROM python:3.13-alpine

RUN pip install pytest pytest-watch

WORKDIR /exercises

CMD tail -f /dev/null # Keep the container open
