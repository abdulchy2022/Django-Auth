from dataclasses import field
from django import forms
from django.contrib.auth.models import User
from .models import Profile
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms

class RegisterUserForm(UserCreationForm):
    class Meta:
        model = User
        fields =  ["username","email","password1","password2" ]
        
        
class Userinfoform(ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'

        
