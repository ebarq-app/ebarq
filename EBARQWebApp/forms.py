from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from EBARQWebApp.models import *
from django.forms import ModelForm
from django.forms.widgets import DateInput, TimeInput


class HorseOwnerSignUpForm(UserCreationForm):
    forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(max_length=254, required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
    contact_number = forms.CharField(max_length=10, widget=forms.TextInput(attrs={'class': 'form-control'}))

    def __init__(self, *args, **kwargs):
        super(HorseOwnerSignUpForm, self).__init__(*args, **kwargs)
        for fieldname in ['username', 'password1', 'password2']:
            # self.fields[fieldname].help_text = None
            self.fields['password1'].widget.attrs.update({'class': 'form-control'})
            self.fields['password2'].widget.attrs.update({'class': 'form-control'})

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'contact_number', 'password1', 'password2')
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'password1': forms.TextInput(attrs={'class': 'form-control'}),
            'password2': forms.TextInput(attrs={'class': 'form-control'}),
        }
    def clean_email(self):
        email = self.cleaned_data.get('email')
        username = self.cleaned_data.get('username')
        if email and User.objects.filter(email=email).exclude(username=username).exists():
            raise forms.ValidationError('Email addresses must be unique!')
        return email

    def clean_contact_number(self):
        contact_number = self.cleaned_data.get('contact_number')
        if HorseOwner.objects.filter(contact_number = contact_number).exclude(pk=self.instance.pk).exists():
            raise forms.ValidationError('Phone numebr must be unique!')
        return contact_number

class HorseSignupForm(forms.ModelForm):
    # name = forms.CharField(max_length=50)
    # age = forms.IntegerField()
    # gender = forms.CharField(max_length=6)
    # date_of_birth = forms.DateField() # Change for current date - age input
    # weight = forms.IntegerField()
    # height = forms.IntegerField()
    #
    # whorl = forms.ImageField()
    # side_face = forms.ImageField()
    # full_side = forms.ImageField()
    #
    # def __init__(self, *args, **kwargs):
    #     super(HorseSignupForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Horse
        fields = ('name', 'age', 'full_side', 'side_face', 'whorl')
        widgets = {
            "Horse's Name": forms.TextInput(attrs={'class': 'form-control'}),
            'age': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def clean_date_of_birth(self):
        date_of_birth = self.cleaned_data['date_of_birth']
        if date_of_birth > datetime.date.today():
            raise forms.ValidationError("The date cannot be in the future!")
        return date_of_birth

class QuestionForm(forms.ModelForm):
    question = forms.CharField(max_length=100)
    answer = forms.CharField(max_length=100)

    def __init__(self, *args, **kwargs):
        super(QuestionForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Question
        fields = ('question', 'answer')


class AddReminderForm(forms.ModelForm):
    notes = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = AddReminder
        fields = ('event', 'time', 'date', 'notes')
        widgets = {
            'event': forms.TextInput(attrs={'class': 'form-control'}),
            'time': TimeInput(attrs={'type': 'time'}),
            'date': DateInput(attrs={'type': 'date'}),
        }

    def clean_date(self):
        date = self.cleaned_data['date']
        if date < datetime.date.today():
            raise forms.ValidationError("Reminder cannot be set in the past!")
        return date

class EditReminderForm(forms.ModelForm):
    notes = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = AddReminder
        fields = ('event', 'time', 'date', 'notes')
        widgets = {
            'event': forms.TextInput(attrs={'class': 'form-control'}),
            'time': TimeInput(attrs={'type': 'time'}),
            'date': DateInput(attrs={'type': 'date'}),
            }

    def clean_date(self):
        date = self.cleaned_data['date']
        if date < datetime.date.today():
            raise forms.ValidationError("Reminder cannot be set in the past!")
        return date

    def __init__(self, *args, **kwargs):
        super(EditReminderForm, self).__init__(*args, **kwargs)

class AddPerformanceForm(forms.ModelForm):
    notes = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = AddPerformance
        fields = ('event', 'time', 'duration', 'notes')
        widgets = {
            'time': TimeInput(attrs={'type': 'time'}),
            'event': forms.TextInput(attrs={'class': 'form-control'}),
            'duration': forms.TextInput(attrs={'class': 'form-control'}),
        }


class EditPerformanceForm(forms.ModelForm):
    notes = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = AddPerformance
        fields = ('event', 'time', 'duration', 'notes')
        widgets = {
            'time': TimeInput(attrs={'type': 'time'}),
            'event': forms.TextInput(attrs={'class': 'form-control'}),
            'duration': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super(EditPerformanceForm, self).__init__(*args, **kwargs)




class UpdateUserForm(forms.ModelForm):
    forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
    contact_number = forms.CharField(max_length=10, widget=forms.TextInput(attrs={'class': 'form-control'}))
    class Meta:
        model = HorseOwner
        fields = ('first_name', 'last_name', 'contact_number','display_image')
    def __init__(self, *args, **kwargs):
        super(UpdateUserForm, self).__init__(*args, **kwargs)

class EditHorseForm(forms.ModelForm):
    whorl = forms.ImageField(required=False)
    side_face = forms.ImageField(required=False)
    full_side = forms.ImageField(required=False)

    # Horse has these details
    name = forms.CharField(max_length=50, required=False)
    weight = forms.IntegerField(validators= [MaxValueValidator(1700), MinValueValidator(150)], required=False)
    height = forms.IntegerField(validators= [MaxValueValidator(250), MinValueValidator(50)], required=False)

    class Meta:
        model = Horse
        fields = ('name','weight','height','whorl','side_face','full_side')
