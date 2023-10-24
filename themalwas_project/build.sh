#!/usr/bin/env bash
# exit on error
set -o errexit
curl --create-dirs -o $HOME/.postgresql/root.crt 'https://cockroachlabs.cloud/clusters/1d87007b-9a15-465c-8ea0-070c2556faec/cert'
ls -lrt $HOME/.postgresql/root.crt
pip install -r requirements.txt
python manage.py collectstatic --no-input
python manage.py migrate