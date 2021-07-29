FROM python:2-alpine

COPY . /src

RUN pip install -r /src/requirements.txt

EXPOSE 5000

ENTRYPOINT ["python", "/src/main.py"]