from django.shortcuts import render, redirect, HttpResponseRedirect
from django.http import HttpResponse
from django.urls import reverse
from django.template import loader
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from EBARQWebApp.forms import *
from EBARQWebApp.models import *

from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.contrib.auth.models import User
from django.core.mail import EmailMessage
from django.views.decorators.http import require_http_methods


# Create your views here.
def index(request):
    return redirect('login')


@require_http_methods(["GET", "POST"])
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            print (user.is_active)
            if user.is_active == True:
                # We have found our user (Login Success!)
                login(request, user)
                # return render(request, 'dashboard.html')
                return redirect('/dashboard')

        else:
            # Failed login attempt - needs adding to html
            return render(request, 'login.html', {'error_message': "Sorry, you've entered incorrect username/password"})

    else:
        return render(request, 'login.html')

    # We need this section for later on just commenting it out for now for convenience
    # elif request.method == 'GET':
    #     if request.user.is_authenticated:
    #         return redirect('/dashboard')
    #     else:
    #         return render(request, 'login.html')


@require_http_methods(["GET", "POST"])
def signup(request):
    if request.method == 'POST':
        form = HorseOwnerSignUpForm(request.POST)
        if form.is_valid():
            form = HorseOwnerSignUpForm(request.POST)
            data = form.cleaned_data
            user = form.save()
            user.refresh_from_db()
            user.is_active = False
            user.save()
            horse_owner = HorseOwner(user_id=user, first_name = data.get('first_name'), last_name = data.get('last_name'))
            horse_owner.save()
            current_site = get_current_site(request)
            message = render_to_string('acc_active_email.html', {
                'user':user,
                'domain':current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)).decode,
                'token': account_activation_token.make_token(user),
            })

            mail_subject = 'Activate your EBARQ account.'
            to_email = form.cleaned_data.get('email')
            email = EmailMessage(mail_subject, message, to=[to_email])
            email.send()
            return HttpResponse('Please confirm your email address to complete the registration')
        else:
            return render(request, 'signup.html', {'form': form})

    form = HorseOwnerSignUpForm()    
    return render(request, 'signup.html', {'form': form})


def dashboard(request):
    if request.user.is_authenticated:
        profile = User.objects.get(id=request.user.id)
        horse_owner = HorseOwner.objects.get(user_id=profile)
        horse = Horse.objects.filter(horse_owner=horse_owner)
        return render(request, 'dashboard.html', {'user': horse_owner, 'horses': horse})
    else:
        return HttpResponseRedirect('/login')


def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        # return redirect('home')
        return HttpResponse('Thank you for your email confirmation. Now you can login your account.')
    else:
        return HttpResponse('Activation link is invalid!')


@require_http_methods(["GET", "POST"])
def horse_add_view(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = HorseSignupForm(request.POST, request.FILES)
            if form.is_valid():
                data = form.cleaned_data
                name = data.get('name')
                age = data.get('age')
                gender = data.get('gender')
                date_of_birth = data.get('date_of_birth')
                weight = data.get('weight')
                height = data.get('height')
                whorl = data.get('whorl')
                side_face = data.get('side_face')
                full_side = data.get('full_side')

                h = Horse(name=name, age=age, gender=gender, date_of_birth=date_of_birth,
                          weight=weight, height=height, whorl=whorl, side_face=side_face,
                          full_side=full_side, horse_owner=HorseOwner.objects.get(user_id=request.user))

                h.save()
                return redirect('/dashboard', {'message': 'Horse Successfully Created!'})
            else:
                form = HorseSignupForm()
                return redirect('/horse_add', {'message': 'One or more fields invalid, please correct these fields'})
        form = HorseSignupForm()
        return render(request, 'horse_add.html', {'form': form})


def horse_add_view_new(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = HorseSignupForm(request.POST, request.FILES)
            if form.is_valid():
                data = form.cleaned_data
                name = data.get('name')
                age = data.get('age')
                gender = data.get('gender')
                date_of_birth = data.get('date_of_birth')
                weight = data.get('weight')
                height = data.get('height')
                whorl = data.get('whorl')
                side_face = data.get('side_face')
                full_side = data.get('full_side')

                h = Horse(name=name, age=age, gender=gender, date_of_birth=date_of_birth,
                          weight=weight, height=height, whorl=whorl, side_face=side_face,
                          full_side=full_side, horse_owner=HorseOwner.objects.get(user_id=request.user))

                h.save()
                return redirect('/dashboard', {'message': 'Horse Successfully Created!'})
            # Redirect to ebarq
            else:
                form = HorseSignupForm()
                return redirect('/horse_add',
                                {'message': 'One or more fields invalid, please correct these fields'})
        form = HorseSignupForm()
        return render(request, 'horse_add.html', {'form': form})


def ebarqdashboard(request):
    if request.user.is_authenticated:
        profile = User.objects.get(id=request.user.id)
        horse_owner = HorseOwner.objects.get(user_id=profile)
        horse = Horse.objects.filter(horse_owner=horse_owner)
        return render(request, 'ebarqdashboard.html', {'horses': horse})


def addperformance(request):
    return render(request, 'addRecord.html')


def addreminder(request):
    return render(request, 'addReminder.html')


def horseReminders(request):
    return render(request, 'horseReminders.html')


def userprofile(request):
    return render(request, 'userprofile.html')


def editprofile(request):
    return render(request, 'editprofile.html')


def horseprofile(request):
    if request.user.is_authenticated:
        profile = User.objects.get(id=request.user.id)
        horse_owner = HorseOwner.objects.get(user_id=profile)
        horse = Horse.objects.filter(horse_owner=horse_owner)
        return render(request, 'horseProfile.html', {'horses': horse})
def horse_inDepth(request):
    # if request.user.is_authenticated:
    #     profile = User.objects.get(id=request.user.id)
    #     horse_owner = HorseOwner.objects.get(user_id=profile)
    #     horse = Horse.objects.filter(horse_owner=horse_owner)
    #     return render(request, 'horse_inDepth.html', {'horses': horse})
    return render(request,'horse_inDepth.html')



def setting(request):
    return render(request, 'setting.html')