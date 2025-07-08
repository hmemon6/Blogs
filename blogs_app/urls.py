from django.urls import path, include
from . import views

app_name ='blogs_app'

urlpatterns = [
 
path('',views.index, name='index'), 
path('blogs/',views.blogs, name='blogs'), 
path('blog/<int:blog_id>/',views.blog, name='blog'), 
path('blog/edit/<int:blog_id>/',views.edit_blog, name='edit_blog'),
path('new_blog/',views.new_blog, name='new_blog'),
path('post/<int:post_id>/',views.post, name='post'),
path('new_post/<int:blog_id>/',views.new_post, name='new_post'),

]
