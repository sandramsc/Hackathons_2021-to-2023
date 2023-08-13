FROM python:3.9.4-slim-buster

LABEL org.opencontainers.image.source="https://github.com/talha-altair/tva"

ADD requirements.txt /app/requirements.txt

RUN pip install -r /app/requirements.txt

RUN python -m spacy download en_core_web_sm

EXPOSE 5000

ADD . /app

WORKDIR /app

ENTRYPOINT ["python3"]

CMD ["app.py"]
