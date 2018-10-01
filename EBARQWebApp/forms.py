from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from EBARQWebApp.models import *
from django.forms import ModelForm
from django.forms.widgets import DateInput

class HorseOwnerSignUpForm(UserCreationForm):
    forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class' : 'form-control'}))
    email = forms.EmailField(max_length=254, required=True, widget=forms.TextInput(attrs={'class' : 'form-control'}))
    first_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class' : 'form-control'}))
    last_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class' : 'form-control'}))


    def __init__(self, *args, **kwargs):
        super(HorseOwnerSignUpForm, self).__init__(*args, **kwargs)
        for fieldname in ['username', 'password1', 'password2']:
            # self.fields[fieldname].help_text = None
            self.fields['password1'].widget.attrs.update({'class' : 'form-control'})
            self.fields['password2'].widget.attrs.update({'class' : 'form-control'})
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')
        widgets = {
               'username': forms.TextInput(attrs={'class': 'form-control'}),
               'password1': forms.TextInput(attrs={'class': 'form-control'}),
               'password2': forms.TextInput(attrs={'class': 'form-control'}),
        }

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
        fields = ('name','age','gender','date_of_birth','weight','height', 'whorl', 'side_face', 'full_side')
        widgets = {
               'name': forms.TextInput(attrs={'class': 'form-control'}),
               'age': forms.TextInput(attrs={'class': 'form-control'}),
               'gender': forms.TextInput(attrs={'class': 'form-control'}),
               'date_of_birth':  DateInput(attrs={'type': 'date'}),
               'weight': forms.TextInput(attrs={'class': 'form-control'}),
               'height': forms.TextInput(attrs={'class': 'form-control'}),
        }

class QuestionForm(forms.ModelForm):
    question = forms.CharField(max_length=100)
    answer = forms.CharField(max_length=100)

    def __init__(self, *args, **kwargs):
        super(QuestionForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Question
        fields = ('question','answer')

class AddPerformanceForm(forms.ModelForm):
    time = forms.TimeField()
    type = forms.CharField(max_length=100)
    duration = forms.IntegerField()
    additional = forms.CharField(max_length=250)

    class Meta:
        model = AddPerformance
        fields = ('time','type','duration','additional')

class AddReminderForm(forms.ModelForm):
    event = forms.CharField(max_length=100)
    time = forms.TimeField()
    date = forms.DateField()
    notes = forms.CharField(max_length=250)

    class Meta:
        model = AddReminder
        fields = ('event','time','date','notes')
