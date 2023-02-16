FROM alpine:3.17

RUN apk add --no-cache python3 py3-pip
RUN adduser -D flask

USER flask

WORKDIR /home/flask

COPY . .
RUN pip3 install -r requirements.txt --no-cache-dir

EXPOSE 5000

CMD python -m flask run --host=0.0.0.0
