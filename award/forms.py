from django import forms
from django.contrib.auth import get_user_model
from . models import *

User = get_user_model()

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ["username", "email"]

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["prof_pic"]        