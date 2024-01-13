FROM python:3.9-slim as builder


WORKDIR /app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt


COPY . ./

RUN pytest


FROM python:3.9-slim

RUN useradd -m myuser


USER myuser


WORKDIR /app


COPY --from=builder /app /app

EXPOSE 5000


ENV FLASK_APP=app.py
ENV FLASK_ENV=production


CMD ["gunicorn", "-b", "0.0.0.0:5000", "app:app"]
