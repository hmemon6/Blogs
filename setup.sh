pip install -r requirements.txt
python manage.py collectstatic --no-input --clear
python manage.py makemigrations
python manage.py migrate
python -m gunicorn blog_project.wsgi:application

# copies stuff froms taticfiles generated during collecstatic command to static. If you dont have static folder
# use this command first mkdir -p static
cp -r staticfiles/* static/
