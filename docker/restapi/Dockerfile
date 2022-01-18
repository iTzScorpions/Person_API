FROM python:3.8

COPY Person_API ./Person_API

COPY dump.sql ./docker-entrypoint-initdb.d

RUN pip install -r Person_API/requirements.txt

CMD ["python3", "Person_API/rest.py"]
