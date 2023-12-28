FROM python:3.12-alpine

WORKDIR /usr/src

COPY . . 

RUN pip3 install --no-cache-dir -r requirements.txt

EXPOSE 5000

ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0

CMD ["flask", "run"]
