pip install -r requirements.txt
python manage.py collectstatic --no-input --clear
python manage.py makemigrations
python manage.py migrate
python -m gunicorn blog_project.wsgi:application
