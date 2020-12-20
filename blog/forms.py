from .models import Comment,Post
from django import forms
from django.contrib.auth.models import User

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'slug', 'content','category')

class SignupForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password', 'email','first_name','last_name']
        
        