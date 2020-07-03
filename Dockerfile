FROM python:3.8.1

WORKDIR /app
COPY . /app
COPY requirements.txt /app/requirements.txt

ENV FLASK_APP app.py
ENV FLASK_RUN_HOST 0.0.0.0

RUN pip install -r requirements.txt

CMD ["flask", "run"]