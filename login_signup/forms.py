from django import forms
from django.forms.widgets import TextInput, PasswordInput, RadioSelect
import normaluser
from normaluser.models import NormalUser


class LoginForm(forms.Form):
    username = forms.CharField(label='', widget=TextInput(attrs={'class': 'input', 'id': 'email', 'name': 'email',
                                                                 'type': 'text', 'placeholder': 'Email or Username'}))

    password = forms.CharField(label='', widget=PasswordInput(attrs={'class': 'input', 'id': 'pass', 'name': 'password',
                                                                     'type': 'password', 'placeholder': 'Password'}))


class SignupForm(forms.Form):
    CHOICES = [('Male', 'Male'), ('Female', 'Female')]
    name = forms.CharField(label='', widget=TextInput(attrs={'type': 'text',
                                                             'placeholder': 'Full name (first and last)',
                                                             'class': 'input'}))

    age = forms.IntegerField(label='', widget=TextInput(attrs={'type': 'text',
                                                               'placeholder': 'Age',
                                                               'class': 'input'}))

    email = forms.CharField(label='', widget=TextInput(attrs={'type': 'text',
                                                              'placeholder': 'Email',
                                                              'class': 'input'}))

    password = forms.CharField(label='', widget=PasswordInput(attrs={'type': 'password',
                                                                     'placeholder': 'Password',
                                                                     'class': 'input'}))

    confirm = forms.CharField(label='', widget=PasswordInput(attrs={'type': 'password',
                                                                    'placeholder': 'Confirm Password',
                                                                    'class': 'input'}))

    gender = forms.ChoiceField(label='', choices=CHOICES, widget=RadioSelect())
