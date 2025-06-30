from django import forms
from .models import Blog, Post

class BlogForm(forms.ModelForm):
    
    class Meta:
        model = Blog
        fields = ['blog_topic', 'description', 'public_blog']
        # To style/customize the form use widgets and send in class whiic you can acces on the html page
        widgets = {
            'blog_topic': forms.TextInput(attrs={'class': 'form-control theme-input'}),
            'description': forms.Textarea(attrs={'class': 'form-control theme-input', 'rows': 4}),
        }
        

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['post_title', 'description']