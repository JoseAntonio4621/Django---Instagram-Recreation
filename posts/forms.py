# Posts forms

# Django
from django import forms 

# Models
from posts.models import Post

class PostForm(forms.ModelForm):
    # post Model Form
    class Meta:
        # Form settings
        model = Post
        fields = ('user', 'profile', 'title', 'photo')