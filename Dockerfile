FROM python:3.8-slim

WORKDIR /app

ADD requirements.txt .
ADD main.py .
ADD test.py .

RUN pip install --upgrade pip && \
    pip install -r requirements.txt

ENTRYPOINT ["python", "main.py"]