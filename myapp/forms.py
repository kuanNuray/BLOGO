# blog/myapp/forms.py

from django import forms
from .models import Posts

class PostForm(forms.ModelForm):
    class Meta:
        model = Posts
        fields = ['title', 'content', 'is_published', 'photo', 'categotia', 'slug']

#Jjajajjajjjaj proverkaaa