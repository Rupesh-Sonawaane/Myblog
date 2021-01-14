from django import forms
from blog.models import Post
from django.contrib.auth.models import User

class loginForm(forms.Form):
    class Meta:
        model= User
        fields = ["username", "password"]

class AddPostForm(forms.ModelForm):
    class Meta:
        model  = Post
        fields = "__all__"

class EditPostForm(forms.ModelForm):
    class Meta:
        model  = Post
        fields = "__all__"
