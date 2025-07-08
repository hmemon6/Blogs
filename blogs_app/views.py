from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import Http404
from .models import Blog, Post
from .forms import BlogForm, PostForm
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required as django_login_required
from functools import wraps

# Create your views here.

def index(request):
        
    blog_list = Blog.objects.filter(public_blog=True).order_by('date_added')
    paginator = Paginator(blog_list, 10)  # Show 5 blogs per page (change as needed)
    page_number = request.GET.get('page')
    blogs = paginator.get_page(page_number)

    context = {'blogs': blogs}
    return render(request, 'blogs_app/index.html', context)

@login_required
def new_blog(request):
    
    blogs = Blog.objects.filter(user=request.user).order_by('date_modified')
    

    if request.method != 'POST':
        form = BlogForm()
    else:
        form = BlogForm(data=request.POST)
        if form.is_valid():
            new_blog = form.save(commit=False)
            new_blog.user = request.user
            new_blog.save()
            return redirect('blogs_app:blogs')
    
    context = {'blogs':blogs, 'form': form}
    return render(request, 'blogs_app/new_blog.html', context)    


@login_required
def blogs(request):
    blog_list = Blog.objects.filter(user=request.user).order_by('date_modified')
    
    paginator = Paginator(blog_list, 10)  # Show 5 blogs per page (change as needed)
    page_number = request.GET.get('page')
    blogs = paginator.get_page(page_number)
    
    context = {'blogs': blogs}
    return render(request, 'blogs_app/blogs.html', context)



def login_required_if_private(view_func):
    @wraps(view_func)
    def _wrapped_view(request, blog_id, *args, **kwargs):
        try:
            blog = Blog.objects.get(id=blog_id)
        except Blog.DoesNotExist:
            raise Http404
        if blog.public_blog:
            return view_func(request, blog_id, *args, **kwargs)
        else:
            return django_login_required(view_func)(request, blog_id, *args, **kwargs)
    return _wrapped_view

@login_required_if_private
def blog(request, blog_id):
    
    blog = Blog.objects.get(id=blog_id)
    posts_list = Post.objects.filter(blog=blog).order_by('-date_added')
    paginator = Paginator(posts_list, 5)  # Show 5 posts per page (change as needed)
    page_number = request.GET.get('page')
    posts = paginator.get_page(page_number)
    # posts = Post.objects.filter(blog=blog).order_by('-date_added')
    
    if not blog.public_blog:
        if blog.user != request.user:
            raise Http404
        context = {'blog': blog, 'posts': posts}    
        return render(request, 'blogs_app/blog.html', context)
    else:
        context = {'blog': blog, 'posts': posts}    
        return render(request, 'blogs_app/blog.html', context)


@login_required
def edit_blog(request, blog_id):
    blog= Blog.objects.get(id=blog_id)
    
    if blog.user != request.user:
        raise Http404
    
    if request.method != 'POST':
        form = BlogForm(instance=blog)
    else:
        form = BlogForm(instance=blog, data=request.POST)
        action = request.POST.get('action')
        if action == 'delete':
            blog.delete()
            return redirect('blogs_app:blogs')
        elif action =='save':
            if form.is_valid:
                new_blog=form.save(commit=False)
                new_blog.user = request.user
                new_blog.save()
                return redirect('blogs_app:blog', blog_id=blog_id)
        
    context = {'blog': blog, 'form': form}
    return render(request, 'blogs_app/edit_blog.html', context)
    

@login_required
def posts(request, blog_id):
    
    try:
        blog = Blog.objects.get(id=blog_id, user=request.user)
    except Blog.DoesNotExist:
        raise Http404("Blog not found.")

    posts = Post.objects.filter(blog=blog).order_by('-date_added')
    context = {'blog': blog, 'posts': posts}
    return render(request, 'blogs_app/posts.html', context)
    
@login_required
def new_post(request, blog_id):
    
    # dont do this if you want to access the id because filter brings in the query set
    # blog = Blog.objects.filter(id=blog_id) 
    blog = Blog.objects.get(id=blog_id)
    if request.method != "POST":
        form = PostForm()
    else:
        form = PostForm(data=request.POST)
        if form.is_valid:        
            new_post = form.save(commit=False)
            new_post.blog = blog
            new_post.save()
            return redirect('blogs_app:blog', blog_id = blog.id)
        
    context = {'form': form, 'blog': blog }
    return render(request, 'blogs_app/new_post.html', context)

@login_required
def post(request, post_id):
    post = Post.objects.get(id=post_id)
    blog = post.blog
    
    if post.blog.user != request.user:
        raise Http404
    
    if request.method != 'POST':
        form = PostForm(instance=post)
    else:   
        try:
            form = PostForm(instance=post, data=request.POST)
            action = request.POST.get('action')
            if action == 'delete':
                post.delete()
                return redirect('blogs_app:blog', blog_id = blog.id)
            elif action == 'save':
                if form.is_valid():
                    new_post = form.save(commit=False)
                    new_post.post = post
                    new_post.save()
                    return redirect('blogs_app:blog', blog_id = blog.id)
        except Post.DoesNotExist:
            raise Http404("Post not found.")
        
    context = {'form': form, 'post': post, 'blog': blog }
    return render(request, 'blogs_app/post.html', context)
