import datetime
import uuid

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.validators import MaxValueValidator, MinValueValidator, RegexValidator

class HorseOwner(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE) # Shouldn't this be One-to-One (one user has one user_id)
    # User must have a first name, last name is not required (trust me I know a guy)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    display_image = models.ImageField(upload_to='', default='user.png',blank=True)

    phone_regex = RegexValidator(regex=r'^\+?1?\d{10}$',
                                 message="Phone number must be entered in the format: '+999999999'. Up to 10 digits allowed.")
    contact_number = models.CharField(validators=[phone_regex], max_length=10, blank=True,default="0000000000")  # validators should be a list

    def __str__(self):
        return self.name


class Horse(models.Model):
    CHOICES = (
    ('male', 'male'),
    ('female', 'female')
    )
    horse_owner = models.ForeignKey(HorseOwner, on_delete=models.CASCADE) # An owner can have multiple horses
    #horse_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    full_side = models.ImageField(upload_to='',default='default1.jpg',blank=True)
    whorl = models.ImageField(upload_to='', default='default3.png',blank=True)
    side_face = models.ImageField(upload_to='',default='default2.jpg',blank=True)

    # Horse has these details
    name = models.CharField(max_length=50)
    age = models.IntegerField()


    def __str__(self):
        # Represent the Horse with a String, uniquely with the horse_id for admin site
        return self.name

class EbarqRecord(models.Model):
    horse = models.ForeignKey(Horse, on_delete=models.CASCADE)
    record_id = models.IntegerField()
    start_stamp = models.DateField(null=True)
    end_stamp = models.DateField(null=True)


class Question(models.Model):
    horse = models.ForeignKey(Horse, on_delete=models.CASCADE) # Links this question to the Horse
    question = models.CharField(max_length=100)
    answer = models.CharField(max_length=100)

    def __str__(self):
        # Shows the question on admin page
        return self.question

class AddPerformance(models.Model):
    horse = models.ForeignKey(Horse, on_delete=models.CASCADE)

    time = models.TimeField()
    event = models.CharField(max_length=100)
    duration = models.IntegerField()
    additional = models.CharField(max_length=250)

class AddReminder(models.Model):
    horse = models.ForeignKey(Horse, on_delete=models.CASCADE)
    event = models.CharField(max_length=100)
    time = models.TimeField()
    date = models.DateField()
    notes = models.CharField(max_length=250)
