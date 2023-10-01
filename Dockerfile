FROM python:3.10-alpine
RUN pip install paho-mqtt

WORKDIR /app
COPY . .

CMD ["python", "main.py"]