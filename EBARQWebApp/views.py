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
from django.contrib import messages
import requests
import redex

def index(request):
    return redirect('login')


def logout_view(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect('/login')
    else:
        return redirect('/login')


@require_http_methods(["GET", "POST"])
# Log user in when there is a valid input
def login_view(request):
    # user can only login when there is a post request i.e. when they press the login button
    if request.method == 'POST':
        # get username and password data from input
        username = request.POST['username']
        password = request.POST['password']
        # try authenticating the user using the entered username and password
        user = authenticate(request, username=username, password=password)

        if user is not None:
            if user.is_active == True:
                # We have found our user (Login Success!)
                login(request, user)
                profile = User.objects.get(id=request.user.id)
                horse_owner = HorseOwner.objects.get(user_id=profile)
                horse = Horse.objects.filter(horse_owner=horse_owner)
                # check if the user has already registered a horse
                # User should have atleast one horse registered before site functionaltiy is availability
                if not horse:
                    return redirect('/PIS')
                return redirect('/dashboard')
            else:
                return redirect('/login')

        else:
            messages.error(request, 'username or password not correct')
            return redirect('/login')
    else:
        return render(request, 'login.html')


@require_http_methods(["GET", "POST"])
# Register a new user for the system that is a horse owner
def signup(request):
    if request.method == 'POST':
        # get a form for signup from forms.py
        form = HorseOwnerSignUpForm(request.POST)
        # check if the input in from by user is valid
        if form.is_valid():
            # get data from form
            data = form.cleaned_data
            user = form.save()
            user.refresh_from_db()

            ###############################################################
            # verification commented out for testing purposes
            ###############################################################
            user.is_active = False
            user.save()
            # save data entered to HowseOwner table
            horse_owner = HorseOwner(user_id=user, first_name=data.get('first_name'), last_name=data.get('last_name'),
                                     contact_number=data.get('contact_number'))
            horse_owner.save()
            ###############################################################
            # verification commented out for testing purposes
            ###############################################################
            current_site = get_current_site(request)
            message = render_to_string('acc_active_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)).decode,
                'token': account_activation_token.make_token(user),
            })
            mail_subject = 'Activate your EBARQ account.'
            to_email = form.cleaned_data.get('email')
            email = EmailMessage(mail_subject, message, to=[to_email])
            email.send()
            return HttpResponse('Please confirm your email address to complete the registration')
            # return render(request, 'dashboard.html')

            # return redirect('/horse_add')
        else:
            return render(request, 'signup.html', {'form': form})
    form = HorseOwnerSignUpForm()
    return render(request, 'signup.html', {'form': form})


# the main dashboard view of a horse owner
def dashboard(request):
    # check for authentication
    if request.user.is_authenticated:
        # get the data for logged in user
        profile = User.objects.get(id=request.user.id)
        horse_owner = HorseOwner.objects.get(user_id=profile)
        # get horse data of logged in user
        horse = Horse.objects.filter(horse_owner=horse_owner)
        # if the user has no registered horse user is first asked to add a new horse
        if not horse:
            return redirect('/horse_add')
        return render(request, 'dashboard.html', {'user': horse_owner, 'horses': horse})
    else:
        return HttpResponseRedirect('/login')


# Activate user when activation is linked
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
        return redirect('/login', {'message': 'Successfully Activated'})
    else:
        return HttpResponse('Activation link is invalid!')


@require_http_methods(["GET", "POST"])
def horse_add_view(request):
    if request.user.is_authenticated:
        profile = User.objects.get(id=request.user.id)
        horse_owner = HorseOwner.objects.get(user_id=profile)
        horse = Horse.objects.filter(horse_owner=horse_owner)
        horseBool = 0
        if not horse:
            horseBool = 1
        if request.method == 'POST':
            form = HorseSignupForm(request.POST, request.FILES)
            if form.is_valid():
                data = form.cleaned_data
                name = data.get('name')
                age = data.get('age')
                whorl = data.get('whorl')
                side_face = data.get('side_face')
                full_side = data.get('full_side')

                h = Horse(name=name, age=age, whorl=whorl, side_face=side_face,
                          full_side=full_side, horse_owner=HorseOwner.objects.get(user_id=request.user))

                h.save()
                if horseBool:
                    return redirect('/ebarqdashboard', {'message': 'Horse Successfully Created!'})
                return redirect('/dashboard', {'message': 'Horse Successfully Created!'})
            else:
                if not horse:
                    return render(request, 'horse_add_new.html', {'form': form})
                return render(request, 'horse_add.html', {'form': form})
        form = HorseSignupForm()
        if not horse:
            return render(request, 'horse_add_new.html', {'form': form})
        return render(request, 'horse_add.html', {'form': form})

    return redirect('/login')

# def temp_record_view(request):


def ebarqdashboard(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            # Call API
            # data = {
            #     'token': 'F6CF0866B9B26D6B44661F25D09F51E5',
            #     'content': 'generateNextRecordName'
            # }
            #
            # r = requests.post('https://redcap.sydney.edu.au/api/', data=data)
            # buf = r.content
            # b = buf.decode('utf-8')
            # record = int(b)
            # print(record)

            #rec = EbarqRecord()
            return redirect('https://redcap.sydney.edu.au/surveys/?s=78DX9TCWJW')

        else:
            profile = User.objects.get(id=request.user.id)
            horse_owner = HorseOwner.objects.get(user_id=profile)
            horse = Horse.objects.filter(horse_owner=horse_owner)
            if not horse:
                return redirect('/horse_add')
            return render(request, 'ebarqdashboard.html', {'horses': horse})
    else:
        return redirect('/login')

def survey_complete_view(request, email, record_id, horse_id):
    if request.user.is_authenticated:
        horse = Horse.objects.get(id = horse_id)
        horse.questionare_required = False
        horse.save()
        record = EbarqRecord(record_id = record_id, horse = horse)
        record.save()
        return redirect('/dashboard')
    else:
        return redirect('/login')


def addperformance(request, horse_id):

    if request.user.is_authenticated:
        profile = User.objects.get(id=request.user.id)
        horse_owner = HorseOwner.objects.get(user_id=profile)
        horse = Horse.objects.get(id=horse_id)
        if request.method == "POST":
            form = AddPerformanceForm(request.POST)
            if form.is_valid():
                data = form.cleaned_data
                event = data.get('event')
                time = data.get('time')
                duration = data.get('duration')
                notes = data.get('notes')
                p = AddPerformance(horse=horse, owner_id = horse_owner.id, event=event, time=time, duration=duration, additional=notes)
                p.save()
                return HttpResponseRedirect('/horse_inDepth/' + str(horse.id) + '/')
            else:
                return render(request, 'addRecord.html', {'horse': horse, 'form': form})
        else:
            form = AddPerformanceForm()
            return render(request, 'addRecord.html', {'horse': horse, 'form': form})

    return redirect('/login')

    # return render(request, 'addRecord.html')


def addreminder(request, horse_id):
    if request.user.is_authenticated:
        profile = User.objects.get(id=request.user.id)
        horse_owner = HorseOwner.objects.get(user_id=profile)
        horse = Horse.objects.get(id=horse_id)
        if request.method == "POST":
            form = AddReminderForm(request.POST)
            if form.is_valid():
                data = form.cleaned_data
                date = data.get('date')
                time = data.get('time')
                event = data.get('event')
                notes = data.get('notes')
                r = AddReminder(horse=horse, owner_id = horse_owner.id, date=date, time=time, event=event, notes=notes)
                r.save()
                return HttpResponseRedirect('/horse_inDepth/' + str(horse.id) + '/')
            else:
                return render(request, 'addReminder.html', {'horse': horse, 'form': form})
        else:
            form = AddReminderForm()
            return render(request, 'addReminder.html', {'horse': horse, 'form': form})

    return redirect('/login')

    # return render(request, 'addReminder.html')


def horseReminders(request):
    if request.user.is_authenticated:
        profile = User.objects.get(id=request.user.id)
        horse_owner = HorseOwner.objects.get(user_id=profile)
        horses = Horse.objects.filter(horse_owner=horse_owner)
        # reminder = AddReminder.objects.
        if not horses:
            return redirect('/horse_add')

        reminders = AddReminder.objects.filter(owner_id = horse_owner.id).order_by('date')
        performances = AddPerformance.objects.filter(owner_id = horse_owner.id)

        # reminders = []
        # performance= []
        # for h in horses:
        #     r = AddReminder.objects.filter(horse=h).values
        #     print (r)
        #     p = AddPerformance.objects.filter(horse=h)
        #     reminders.append(r)
        #     performance.append(p)


        # print(len(reminders))
        # print(reminders[0][2])
        # print(len(performance))

        return render(request, 'horseReminders.html', {'reminders': reminders, 'performances':performances})
    else:
        return redirect('/login')

    # return render(request, 'horseReminders.html')


def userprofile(request):
    if request.user.is_authenticated:
        profile = User.objects.get(id=request.user.id)
        horse_owner = HorseOwner.objects.get(user_id=profile)
        print(horse_owner.display_image)
        return render(request, 'userprofile.html', {'owner': horse_owner, 'profile': profile})
    else:
        return redirect('/login')


def editprofile(request):
    if request.user.is_authenticated:
        profile = User.objects.get(id=request.user.id)
        horse_owner = HorseOwner.objects.get(user_id=profile)
        if request.method == 'POST':
            form = UpdateUserForm(request.POST, request.FILES, instance=horse_owner)
            if form.is_valid():
                data = form.cleaned_data
                first_name = data.get('first_name')
                last_name = data.get('last_name')
                contact_number = data.get('contact_number')
                display_image = data.get('display_image')

                if (len(first_name) > 1):
                    horse_owner.first_name = first_name
                if (len(last_name) > 1):
                    horse_owner.last_name = last_name
                if (len(contact_number) > 9):
                    horse_owner.contact_number = contact_number
                horse_owner.display_image = display_image

                horse_owner.save()
                return redirect('/userprofile', {'message': 'Horse Successfully Created!'})
            else:
                form = UpdateUserForm()
                return redirect('/editprofile',
                                {'message': 'One or more fields invalid, please correct these fields', 'form': form})
        form = UpdateUserForm(instance=horse_owner)
        return render(request, 'editprofile.html', {'form': form,'horse_owner':horse_owner})
    else:
        return redirect('/login')


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
    else:
        return redirect('/login')


def horse_inDepth(request, horse_id):
    if request.user.is_authenticated:
        now = timezone.now()
        horse = Horse.objects.get(id=horse_id)
        reminders = AddReminder.objects.filter(horse=horse).order_by('date')
        performances = AddPerformance.objects.filter(horse=horse)
        return render(request, 'horse_inDepth.html',
                      {'horse': horse, 'reminders': reminders, 'performances': performances})
    else:
        return redirect('/login')


# Delete a reminder record for a horse
def delete_reminder(request, reminder_id):
    if request.user.is_authenticated:
        # Find the reminder that needs to be deleted in the database and delete
        reminder = AddReminder.objects.get(pk=reminder_id)
        horse = Horse.objects.get(id=reminder.horse.id)
        reminder.delete()
        # Redirect back to horse_inDepth page when performance is deleted
        return HttpResponseRedirect('/horse_inDepth/' + str(horse.id) + '/')
    else:
        return redirect('/login')


# Edit reminder of a specific horse belonging to a user
def edit_reminder(request, reminder_id):
    # Check for authentication
    if request.user.is_authenticated:
        # only perfrom edits when there is a post request
        if request.method == 'POST':
            # Get the reminder from database that needs to be edited
            reminder = AddReminder.objects.get(pk=reminder_id)
            horse = Horse.objects.get(id=reminder.horse.id)
            form = EditReminderForm(request.POST, instance=reminder)
            # if the edits are valid, save the changes and redirect back to horse_inDepth page
            if form.is_valid:
                form.save()
                return HttpResponseRedirect('/horse_inDepth/' + str(horse.id) + '/')
        else:
            # If it is a get request jsut load the current values entered for reminder
            reminder = AddReminder.objects.get(pk=reminder_id)
            form = EditReminderForm(instance=reminder)
            return render(request, 'edit_reminder.html', {'form': form})

    else:
        return redirect('/login')


# Edit performance of a specific horse belonging to a user
def edit_performance(request, performance_id):
    # Check for authentication
    if request.user.is_authenticated:
        # only perform edits when there is a post request
        if request.method == 'POST':
            # Get the performance from database that needs to be edited
            performance = AddPerformance.objects.get(pk=performance_id)
            horse = Horse.objects.get(id=performance.horse.id)
            form = EditPerformanceForm(request.POST, instance=performance)
            # if the edits are valid, save the changes and redirect back to horse_inDepth page
            if form.is_valid:
                form.save()
                return HttpResponseRedirect('/horse_inDepth/' + str(horse.id) + '/')
        else:
            # If it is a get request jsut load the current values entered for performance
            performance = AddPerformance.objects.get(pk=performance_id)
            form = EditPerformanceForm(instance=performance)
            return render(request, 'edit_performance.html', {'form': form})

    else:
        return redirect('/login')


def edit_horse(request, horse_id):
    if request.user.is_authenticated:
        horse = Horse.objects.get(id=horse_id)
        print (horse.questionare_required)
        if request.method == 'POST':
            form = EditHorseForm(request.POST, request.FILES, instance = horse)
            if form.is_valid():
                data = form.cleaned_data
                name = data.get('name')
                weight = data.get('weight')
                height = data.get('height')
                whorl = data.get('whorl')
                side_face = data.get('side_face')
                full_side = data.get('full_side')

                #remember to remove this for later on
                horse.questionare_required = False
                if (name is not None and len(name) > 1):
                    horse.name = name
                if (weight is not None and weight > 150 and weight < 1700):
                    horse.weight = weight
                if (height is not None and height > 50 and height < 250):
                    horse.height = height
                if (whorl is not None):
                    horse.whorl = whorl
                if (side_face is not None):
                    horse.side_face = side_face
                if (full_side is not None):
                    horse.full_side = full_side

                horse.save()
                return redirect('/horse_inDepth/' + str(horse.id) + '/', {'message': 'Horse Details Changed!'})
            else:

                form = EditHorseForm(instance=horse)
                return redirect('/edithorse/' + str(horse.id) + '/',
                                {'message': 'One or more fields invalid, please correct these fields', 'form': form,
                                 'horse': horse})

        form = EditHorseForm(instance=horse)
        return render(request, 'edithorse.html', {'form': form, 'horse': horse})
    else:
        return redirect('/login')


# Delete a performance record for a horse
def delete_perfromance(request, performance_id):
    # check user authentication
    if request.user.is_authenticated:
        # Find the performance that needs to be deleted in the database and delete
        perfromance = AddPerformance.objects.get(pk=performance_id)
        horse = Horse.objects.get(id=perfromance.horse.id)
        perfromance.delete()
        # Redirect back to horse_inDepth page when performance is deleted
        return HttpResponseRedirect('/horse_inDepth/' + str(horse.id) + '/')
    else:
        return redirect('login')


def setting(request):
    if request.user.is_authenticated:
        profile = User.objects.get(id=request.user.id)
        owner = HorseOwner.objects.get(user_id=profile)
        return render(request, 'setting.html',{'owner':owner})
    else:
        return redirect('/login')


def graph(request,horse_id):
    if request.user.is_authenticated:
        horse = Horse.objects.get(id=horse_id)

        # Insert generation code here
        record = EbarqRecord.objects.filter(horse=horse).order_by('-start_stamp')
        record_id = record[0].record_id
        totals, mean_totals = redex.redcap_survey(record_id)
        print(totals, mean_totals)
        return render(request, 'ebarqgraph.html', {'horse':horse, 'totals':totals, 'mean_totals':mean_totals})
    else:
        return redirect('/login')


def question(request):
    if request.user.is_authenticated:
        return render(request, 'questionnaire.html')
    else:
        return redirect('/login')

def PIS(request):
    if request.user.is_authenticated:
        profile = User.objects.get(id=request.user.id)
        owner = HorseOwner.objects.get(user_id=profile)
        return render(request,'PIS.html',{'owner':owner})
    else:
        return redirect('/login')
