FROM alpine:latest

RUN apk add --no-cache python3

WORKDIR /app

COPY flag.txt flag.txt
COPY app.py app.py

CMD ["python", "app.py"]
