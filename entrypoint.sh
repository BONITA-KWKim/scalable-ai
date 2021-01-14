#!/bin/sh

# Variables
PROJECT_NAME=scalable_ai

# start gunicorn and django
echo "start flask framework"
gunicorn --chdir /usr/src/app/cervix --workers=2 --bind 0.0.0.0:5000 wsgi:app
