from django.contrib.auth.forms import UserCreationForm
from django import forms


class AuthorForm(UserCreationForm):
    email = forms.EmailField()
    age = forms.IntegerField()

    class Meta:
        model = User
        fields = ('username', 'first_name',
                  'last_name', 'password1', 'password2')
