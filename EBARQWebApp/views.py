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

def logout_view(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect('/login')
    else:
        return redirect('/login')

@require_http_methods(["GET", "POST"])
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            print (user.is_active)
            ###############################################################
            # verification commented out for testing purposes
            ###############################################################
            # if user.is_active == True:
            # We have found our user (Login Success!)
            login(request, user)
            # return render(request, 'dashboard.html')
            profile = User.objects.get(id=request.user.id)
            horse_owner = HorseOwner.objects.get(user_id=profile)
            horse = Horse.objects.filter(horse_owner=horse_owner)
            if not horse:
                return redirect('/horse_add')
            return redirect('/dashboard')

        else:
            # Failed login attempt - needs adding to html
            return render(request, 'login.html', {'error_message': "Sorry, you've entered incorrect username/password"})

    else:
        if request.user.is_authenticated:
            return redirect('/dashboard')
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
            data = form.cleaned_data
            user = form.save()
            user.refresh_from_db()

            ###############################################################
            # verification commented out for testing purposes
            ###############################################################
            # user.is_active = False
            user.save()
            horse_owner = HorseOwner(user_id=user, first_name=data.get('first_name'), last_name=data.get('last_name'), contact_number=data.get('contact_number'))
            horse_owner.save()
            ###############################################################
            # verification commented out for testing purposes
            ###############################################################
            # current_site = get_current_site(request)
            # message = render_to_string('acc_active_email.html', {
            #     'user': user,
            #     'domain': current_site.domain,
            #     'uid': urlsafe_base64_encode(force_bytes(user.pk)).decode,
            #     'token': account_activation_token.make_token(user),
            # })
            # mail_subject = 'Activate your EBARQ account.'
            # to_email = form.cleaned_data.get('email')
            # email = EmailMessage(mail_subject, message, to=[to_email])
            # email.send()
            # return HttpResponse('Please confirm your email address to complete the registration')


            login(request, user)
            # return render(request, 'dashboard.html')
            return redirect('/horse_add')
        else:
            return render(request, 'signup.html', {'form': form})

    form = HorseOwnerSignUpForm()
    return render(request, 'signup.html', {'form': form})


def dashboard(request):
    if request.user.is_authenticated:
        profile = User.objects.get(id=request.user.id)
        horse_owner = HorseOwner.objects.get(user_id=profile)
        horse = Horse.objects.filter(horse_owner=horse_owner)
        if not horse:
            return redirect('/horse_add')
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
        if not horse:
            return redirect('/horse_add')
        return render(request, 'ebarqdashboard.html', {'horses': horse})


def addperformance(request, horse_id):
    if request.user.is_authenticated:
        horse = Horse.objects.get(id=horse_id)
        if request.method == "POST":
            form = AddPerformanceForm(request.POST)
            if form.is_valid():
                data = form.cleaned_data
                event = data.get('event')
                time = data.get('time')
                duration = data.get('duration')
                print(duration)

                notes = data.get('notes')
                p = AddPerformance(horse = horse, event = event, time = time, duration = duration, additional = notes )
                p.save()
                return redirect('/dashboard', {'message': 'Performance Successfully Created!'})
            else:
                return render(request, 'addRecord.html', {'horse': horse, 'form':form})
        else:
            form = AddPerformanceForm()
            return render(request, 'addRecord.html', {'horse': horse, 'form':form})

    return redirect('/login')

    # return render(request, 'addRecord.html')


def addreminder(request, horse_id):
    if request.user.is_authenticated:
        horse = Horse.objects.get(id=horse_id)
        if request.method == "POST":
            form = AddReminderForm(request.POST)
            if form.is_valid():
                data = form.cleaned_data
                date = data.get('date')
                time = data.get('time')
                event = data.get('event')
                notes = data.get('notes')
                r = AddReminder(horse = horse, date = date, time = time, event = event, notes = notes )
                r.save()
                return redirect('/dashboard', {'message': 'Horse Successfully Created!'})
            else:
                return render(request, 'addReminder.html', {'horse': horse, 'form':form})
        else:
            form = AddReminderForm()
            return render(request, 'addReminder.html', {'horse': horse, 'form':form})

    return redirect('/login')


    # return render(request, 'addReminder.html')


def horseReminders(request):
    if request.user.is_authenticated:
        profile = User.objects.get(id=request.user.id)
        horse_owner = HorseOwner.objects.get(user_id=profile)
        horses = Horse.objects.filter(horse_owner=horse_owner)
        if not horses:
            return redirect('/horse_add')

        reminders = []
        performance = []
        for h in horses:
            r = AddReminder.objects.filter(horse=h)
            p = AddPerformance.objects.filter(horse=h)
            reminders.append(r)
            performance.append(p)

        print(len(reminders))
        print(reminders[0])
        print(len(performance))

        return render(request, 'horseReminders.html', {'horses':horses, 'user':horse_owner})
    else:
        return redirect('/login')

    # return render(request, 'horseReminders.html')


def userprofile(request):
    if request.user.is_authenticated:
        profile = User.objects.get(id=request.user.id)
        horse_owner = HorseOwner.objects.get(user_id=profile)
        return render(request, 'userprofile.html',{'owner':horse_owner,'profile':profile})


def editprofile(request):
    return render(request, 'editprofile.html')


def horseprofile(request):
    if request.user.is_authenticated:
        # if request.method == 'POST':
        #
        profile = User.objects.get(id=request.user.id)
        horse_owner = HorseOwner.objects.get(user_id=profile)
        horse = Horse.objects.filter(horse_owner=horse_owner)
        if not horse:
            return redirect('/horse_add')
        return render(request, 'horseProfile.html', {'horses': horse})


def horse_inDepth(request, horse_id):
    # template_name = 'horse_inDepth.html'
    if request.user.is_authenticated:
        now = timezone.now()
        horse = Horse.objects.get(id = horse_id)
        reminders = AddReminder.objects.filter(horse = horse).order_by('date')[:5]
        performances = AddPerformance.objects.filter(horse = horse)
        return render(request, 'horse_inDepth.html', {'horse': horse, 'reminders':reminders, 'performances': performances})


def setting(request):
    return render(request, 'setting.html')

def graph(request):
    return render(request, 'ebarqgraph.html')
