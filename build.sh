#!/usr/bin/env bash
# install dependencies
pip install -r requirements.txt

# collect static files
python manage.py collectstatic --noinput

# apply migrations before migrate the new fields
python manage.py makemigrations

# apply database migrations
python manage.py migrate
