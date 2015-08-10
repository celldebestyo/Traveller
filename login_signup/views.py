from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.http.response import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from login_signup.forms import SignupForm, LoginForm
from normaluser.models import NormalUser
import datetime


def log_in(request):
    if request.method == 'GET':
        return render(request, 'sign-in.html', {'form': LoginForm})

    else:
        form = LoginForm(request.POST)

        if form.is_valid():
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])

            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse('timeline'))

            else:
                form.add_error(None, 'Entered username or password is wrong')
                return render(request, 'sign-in.html', {'form': form})

        else:
            return render(request, 'sign-in.html', {'form': form})


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            newUser = NormalUser()

            try:
                _newUser = User.objects.create_user(username=form.cleaned_data['email'],
                                                    password=form.cleaned_data['password'],
                                                    first_name=form.cleaned_data['name'],
                                                    email=form.cleaned_data['email'])
            except:
                form.add_error(None, 'Email "' + request.POST['email'] + '" already existed')
                return render(request, 'sign-up.html', {'signupForm': form})

            newUser.user = _newUser
            newUser.age = form.cleaned_data['age']
            # newUser.birthDate.year = (datetime.datetime.now().year - form.cleaned_data['age'])
            newUser.gender = form.cleaned_data['gender']
            newUser.save()

            return HttpResponseRedirect(reverse('login'))

        else:
            return render(request, 'sign-up.html', {'signupForm': form})

    else:
        form = SignupForm()
        return render(request, 'sign-up.html', {'signupForm': form})



@login_required
def timeline(request):
    return render(request, 'timeline.html', {}  )


def log_out(request):
    logout(request)
    return HttpResponseRedirect(reverse('login'))
