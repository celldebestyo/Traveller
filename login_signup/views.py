import random
from random import randint
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.core.mail import send_mail
from django.core.urlresolvers import reverse
from django.core.validators import validate_email
from django.http.response import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

# Create your views here.
from login_signup.forms import SignupForm, LoginForm
from normaluser.models import NormalUser, VerificationCode
import datetime


def log_in(request):
    if request.method == 'GET':
        return render(request, 'sign-in.html', {'form': LoginForm})

    else:
        form = LoginForm(request.POST)

        if form.is_valid():
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])

            if user is not None:
                if user.is_active == False:
                    return render(request, 'verification-code.html', {'error': 'Your account is not enable!'})

                else:
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

            _newUser.is_active = False

            newUser.user = _newUser
            newUser.age = form.cleaned_data['age']
            # newUser.birthDate.year = (datetime.datetime.now().year - form.cleaned_data['age'])
            newUser.gender = form.cleaned_data['gender']
            newUser.save()

            code = generate_verification_code()

            verifCode = VerificationCode()
            verifCode.code = code
            verifCode.user = _newUser
            verifCode.save()

            send_mail('Traveler', 'Hello ' + newUser.user.first_name + '\n\n Your verification code is ' + code +
                      '.\n click on the link below to verify your email address: \n\n' +
                      reverse('verification', args=[newUser.user.email])
                      , 'travellerbot@gmail.com', recipient_list=[newUser.user.email])

            return HttpResponseRedirect(reverse('verification', args=[newUser.user.email]))

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


def verify(request, email):
    if request.method == 'GET':
        return render(request, 'verification-code.html', {})

    else:
        try:
            validate_email(email)

        except:
            raise ValidationError('Wrong URL!')


        currUser = get_object_or_404(User, email=email)
        code = get_object_or_404(VerificationCode, user=currUser)

        if request.POST['verifier'] == code.code:
            currUser.is_active = True
            return HttpResponseRedirect(reverse('login'))

        else:
            return render(request, 'verification-code.html', {'error': 'Wrong verification code!'})



def generate_verification_code():
    code = ''
    
    for i in range(0,12):
        code += str(randint(0, 9))

    return code
