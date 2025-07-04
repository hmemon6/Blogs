 19-1. Blog: Start a new Django project called Blog. Create an app called
 blogs, with one model that represents an overall blog, and one model that
 represents an individual blog post. Give each model an appropriate set of
 fields. Create a superuser for the project, and use the admin site to make
 a blog and a couple of short posts. Make a home page that shows all posts
 in an appropriate order.
 Create pages for making a blog, for making new posts, and for editing ex
isting posts. Use your pages to make sure they work.





"""

creating a virtual env for a new project
# python -m venv environment_name

to activate env
# environement_name\Scripts\activate

Now you can install any packages of your interest
for example, you want to upgrade pip since it comes by default with python installation
#python.exe -m pip install --upgrade pip

install Django for the project
# pip install django


To create a project in django
# django-admin startproject projectname .

NOTE: make sure to add . at the end of the name




In an active virtual environment, use the command 
python to run
 manage.py commands, even if you use something different, like
 python3 , to run other programs. In a virtual environment, the
 command 
python refers to the version of Python that was used to
 create the virtual environment.
 

so django is 0used to create a web application,
and the manage.py file is used to manage the application.
For full stack app you need to run the server, so you can use the command:
Note: first time use will create a sqlite database file

#python manage.py runserver


Open a new terminal window and run the command:
When the new file of sqlite is created its not migrated or commited in the dfefualt settings like users etc in the database, to commit it to database use the line below
#python manage.py migrate

 To create a front end of the app do the following
# python manage.py startapp app_name_of_your_choice

for front end app
 So now you should be running a Django web application with a
learning_logs app with backend and front end.


for database, you need to make models in models.py on front end side. See documentation on django

You will also need to modify settings.py on back end, and include your front end app in installed apps otherwise it won't communicate

 we need to tell Django to modify the database so it can store infor
mation related to the model 
Topic .

# python manage.py makemigrations app_name


to commit changes to django you need to use the below

# python manage.py migrate

Django feature, you can create super users by entering the code line below in terminal in active env ofcourse where django is recognized

# python manage.py createsuperuser

"""


You can use Django Shell for troubleshooting

# Python manage.py shell

you can search more about it on django

model.object.all() --> gets all objects for that model
i.e Topic.objects.all()

you can assign  a variable to it so you can use it in shell in a for loop etc

i.w topics = Topic.objects.all()

if you know the id of an object in a model then you can simply use model.objects.get(id=whatever number the object is on)

you can assign it to some variable then you can access individual attributes of that object
i.e t = Topic.objects.get(id=1)

print(t.attribute1)
t.attribute2   ....etc




to get foreign key related info

CurrentModel.objects.get(id=1).FK_attribute_or_FK_lowercaseModekName_set.all()

in current example since Topic.objects.get(id=1) = t

t.entry_set.all()  where entry is the other model that has the primary key and same attribute named is in Topic model

This will show all entries under object with id=1 in Topic so Topic.Chess has whatever number of entries


For example, say you have the models  
Topping is related to 
Pizza and 
Topping , and
Pizza through a foreign key. If your object is called
my_pizza , representing a single pizza, you can get all of the pizza’s top
pings using the code 
my_pizza.topping_set.all().


 Each time you modify your models, you’ll need to restart the shell to see
 the effects of those changes. To exit a shell session, press CTRL-D; on
 Windows, press CTRL-Z and then press ENTER.



If you want to run uvicorn, use the following:

#python -m uvicorn blog_project.asgi:application

for wsgi

#python -m gunicorn blog_project.wsgi:application

please note wsgi is not supported on windows and will need linux vm or wsl to work, 
I set it up because vercel supports wsgi and not asgi so running the command on windows wont work
but vercel will manage to make it work


