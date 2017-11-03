from django import forms
from django.contrib.auth.forms import UserCreationForm
from MyURLSaver_app.models import User, URL


class SignUpForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', )

class AddUrlsForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('urls', )
 
class AddUrlsForm():
    url = forms.CharField(max_length=300)

