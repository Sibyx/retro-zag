FROM alpine:3.17

RUN apk add --no-cache python3 py3-pip libpq postgresql-client
RUN adduser -D flask

USER flask
WORKDIR /home/flask

COPY . .
RUN pip3 install -r requirements.txt --no-cache-dir

EXPOSE 5000

USER root
RUN chmod +x conf/entrypoint.sh
RUN chown flask:flask conf/entrypoint.sh

USER flask

CMD ["conf/entrypoint.sh"]
