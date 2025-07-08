#!/bin/bash
pip install -r requirements.txt
python manage.py collectstatic --no-input
# copies stuff froms taticfiles generated during collecstatic command to static. If you dont have static folder
# use this command first mkdir -p static

# cp -r staticfiles/* static/


python manage.py makemigrations
python manage.py migrate
python -m gunicorn blog_project.wsgi:application
