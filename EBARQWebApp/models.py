import datetime
import uuid

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class HorseOwner(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE) # Shouldn't this be One-to-One (one user has one user_id)
    # User must have a first name, last name is not required (trust me I know a guy)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Horse(models.Model):
    horse_owner = models.ForeignKey(HorseOwner, on_delete=models.CASCADE) # An owner can have multiple horses
    horse_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    # Horse has these details
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    gender = models.CharField(max_length=6)
    date_of_birth = models.DateField()
    weight = models.IntegerField()
    height = models.IntegerField()

    def __str__(self):
        # Represent the Horse with a String, uniquely with the horse_id for admin site
        return self.name

class Question(models.Model):
    horse = models.ForeignKey(Horse, on_delete=models.CASCADE) # Links this question to the Horse
    question = models.CharField(max_length=100)
    answer = models.CharField(max_length=100)

    def __str__(self):
        # Shows the question on admin page
        return self.question
