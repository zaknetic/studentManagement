from django import forms
from . import models
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class StudentForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = models.Student
        exclude = ['user']
        labels = {
            'name': 'Full Name',
        }
        help_texts = {
            'email': 'Enter a valid email address',
        }

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    
