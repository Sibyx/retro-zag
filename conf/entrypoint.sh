#!/bin/sh

until psql -Atx "$POSTGRES_CONNECTION" -c '\q'; do
  >&2 echo "Postgres is unavailable - sleeping"
  sleep 1
done

python -m flask db upgrade
python -m flask run --host=0.0.0.0
