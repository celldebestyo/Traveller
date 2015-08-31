from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.forms.widgets import TextInput, PasswordInput, RadioSelect

class LoginForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        for name, field in self.fields.items():
            if 'required' in field.error_messages:
                field.error_messages['required'] = 'Please fill this field!'

    username = forms.CharField(label='', widget=TextInput(attrs={'class': 'input', 'id': 'email', 'name': 'email',
                                                                 'type': 'text', 'placeholder': 'Email or Username'}))

    password = forms.CharField(label='', widget=PasswordInput(attrs={'class': 'input', 'id': 'pass', 'name': 'password',
                                                                     'type': 'password', 'placeholder': 'Password'}))


class SignupForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(SignupForm, self).__init__(*args, **kwargs)
        for name, field in self.fields.items():
            if name != 'gender':
                if 'required' in field.error_messages:
                    field.error_messages['required'] = 'Please fill this field!'

    CHOICES = [('Male', 'Male'), ('Female', 'Female')]
    name = forms.CharField(label='', widget=TextInput(attrs={'type': 'text',
                                                             'placeholder': 'Full name (first and last)',
                                                             'class': 'input'}))

    age = forms.IntegerField(label='', widget=TextInput(attrs={'type': 'text',
                                                               'placeholder': 'Age',
                                                               'class': 'input'}),
                             error_messages={'invalid': 'This field should be number?!'})

    email = forms.CharField(label='', widget=TextInput(attrs={'type': 'text',
                                                              'placeholder': 'Email',
                                                              'class': 'input'}))

    password = forms.CharField(label='', widget=PasswordInput(attrs={'type': 'password',
                                                                     'placeholder': 'Password',
                                                                     'class': 'input'}))

    confirm = forms.CharField(label='', widget=PasswordInput(attrs={'type': 'password',
                                                                    'placeholder': 'Confirm Password',
                                                                    'class': 'input'}))

    gender = forms.ChoiceField(label='', choices=CHOICES, widget=RadioSelect(), error_messages={
                                                                           'required': 'Please select your gender!'})

    def clean_email(self):
        try:
            validate_email(self.cleaned_data['email'])
        except:
            raise ValidationError('Entered email is not valid!')

        return self.cleaned_data['email']

    def clean_age(self):
        value = self.cleaned_data['age']

        if value < 10 or value > 200:
            raise ValidationError('Age should be between 10 and 120!')

        return self.cleaned_data['age']

    def clean(self):
        if self.data['password'] != self.data['confirm']:
            raise ValidationError('Entered passwords do not match')

        return self.cleaned_data


class forgot1(forms.Form):
    email = forms.EmailField(label='', widget=TextInput(attrs={'placeholder': 'Email', 'type': 'text',
                                                               'class': 'input'}))


class forgot2(forms.Form):
    new_password = forms.CharField(label='', widget=PasswordInput(attrs={'placeholder': 'New password',
                                                                         'class': 'input'}))
    confirm_password = forms.CharField(label='', widget=PasswordInput(attrs={'placeholder': 'Confirm Password',
                                                                             'class': 'input'}))

    def clean(self):
        if self.data['new_password'] != self.data['confirm_password']:
            raise ValidationError('Entered passwords do not match!')

        return self.cleaned_data