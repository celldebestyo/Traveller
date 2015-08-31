from random import randint
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.core.mail import send_mail
from django.core.urlresolvers import reverse
from django.core.validators import validate_email
from django.http.response import HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404
from login_signup.forms import SignupForm, LoginForm, forgot1, forgot2
from normaluser.models import NormalUser, VerificationCode

# Create your views here.

def log_in(request):
    if request.method == 'GET':
        return render(request, 'sign-in.html', {'form': LoginForm})

    else:
        form = LoginForm(request.POST)

        if form.is_valid():
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])

            if user is not None:
                if user.is_active == False:
                    return HttpResponseRedirect(reverse('verification', args=[user.email]))

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
            code.delete()
            return HttpResponseRedirect(reverse('login'))

        else:
            return render(request, 'verification-code.html', {'error': 'Wrong verification code!'})


def forgot_password_1(request):
    if request.method == 'GET':
        return render(request, 'fpw_1.html', {'form': forgot1()})

    else:
        form = forgot1(request.POST)

        if form.is_valid():
            email = form.cleaned_data['email']

            try:
                currUser = User.objects.get(email=email)
            except:
                return render(request, 'fpw_1.html', {'form': form, 'error': 'No such email exist'})

        else:
            return render(request, 'fpw_1.html', {'form': form, 'error': 'Entered email is not valid'})


        if currUser.is_active:
            try:
                tmpVerifCode = VerificationCode.objects.get(user=currUser)
            except:
                tmpVerifCode = None

            if tmpVerifCode is not None:
                tmpVerifCode.delete()

            verifCode = VerificationCode()
            verifCode.user = currUser
            verifCode.code = generate_verification_code()
            verifCode.save()

            send_mail('Traveler', 'Hello ' + currUser.first_name + '\n\n You can reset your password by clicking on '
                                           + 'link below: \n\n http://127.0.0.1:8000' +
                      reverse('fpw2', args=[email, verifCode.code]),
                      'travellerbot', [email])

            return render(request, 'fpw_1.html', {'form': form, 'success': 'Check your email address, an email ' +
                                                                           'containing a link to change your password '
                                                                           + 'has sent to you '})
        else:
            return render(request, 'fpw_1.html', {'form': form, 'error': 'Your account is not enable yet!'})


def forgot_password_2(request, email, code):
    if request.method == 'GET':
        return render(request, 'fpw_2.html', {'form': forgot2})

    else:
        form = forgot2(request.POST)

        if form.is_valid():
            try:
                currUser = User.objects.get(email=email)
            except:
                raise Http404

        else:
            return render(request, 'fpw_2.html', {'form': form, 'error': 'Entered password do not match'})


        verifCode = get_object_or_404(VerificationCode, user=currUser)

        if verifCode.code == code:
            currUser.set_password(request.POST['new_password'])
            currUser.save()
            verifCode.delete()
            return HttpResponseRedirect(reverse('login'))

        else:
            raise ValidationError("It seems that you're cheating or something! :D")




# extra functions

def generate_verification_code():
    code = ''
    
    for i in range(0,12):
        code += str(randint(0, 9))

    return code

