from django import forms
from .models import Posts

# Create your models here.
class PostsForm(forms.ModelForm):
    class Meta:
        model = Posts
        fields = ["title", "body"]
