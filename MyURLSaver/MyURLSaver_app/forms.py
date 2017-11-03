from django import forms
from django.contrib.auth.forms import UserCreationForm
from MyURLSaver_app.models import User


class SignUpForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', )
