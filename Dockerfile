FROM python:3.7-alpine
WORKDIR /
ENV FLASK_APP app.py
ENV FLASK_RUN_HOST 0.0.0.0
ENV FLASK_RUN_PORT 8080
RUN apk add --no-cache gcc musl-dev linux-headers
RUN apk --no-cache add --virtual builds-deps build-base python
RUN apk add py-pip python-dev libffi-dev openssl-dev gcc libc-dev make
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .
CMD ["flask", "run"]
