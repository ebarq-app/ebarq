from django.test import TestCase
from EBARQWebApp.models import *
from django.contrib.auth.models import User
from django.urls import reverse


class ModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        user = User.objects.create(username = "harold11", password = "Chicken33",
                                  email = "harold.gunderson@gmail.com")
        horse_owner = HorseOwner.objects.create(user_id = user, first_name='Harold',
                                                last_name='Gunderson')
        horse = Horse.objects.create(horse_owner = horse_owner, name = "Barry", age = 2, gender = "Male",
                                    date_of_birth = "2016-1-1", weight = 200, height = 200)
        reminder = AddReminder.objects.create(horse = horse, time = '12:00 pm', event = "new reminder", date = "2018-12-12", notes = "just remind me!")

        performance = AddPerformance.objects.create(horse = horse, time = '11:20 am', duration = 20, event = "Running", additional = "just a run")

    def test_first_name(self):
        owner = HorseOwner.objects.get(id = 1)
        first_name = owner.first_name
        self.assertEquals(first_name, 'Harold')

    def test_last_name_label(self):
        owner = HorseOwner.objects.get(id=1)
        last_name = owner.last_name
        self.assertEquals(last_name, 'Gunderson')

    def test_first_name_max_length(self):
        owner = HorseOwner.objects.get(id=1)
        max_length = owner._meta.get_field('first_name').max_length
        self.assertEquals(max_length, 50)

    def test_last_name_max_length (self):
        owner = HorseOwner.objects.get(id=1)
        max_length = owner._meta.get_field('last_name').max_length
        self.assertEquals(max_length, 50)

    def test_user_foreign_key(self):
        owner = HorseOwner.objects.get(id=1)
        user_id = owner.user_id
        self.assertEquals(user_id.username, "harold11")

    def test_horse_name(self):
        horse = Horse.objects.get(horse_owner= 1)
        name = horse.name
        self.assertEquals(name, 'Barry')

    def test_horse_age(self):
        horse = Horse.objects.get(id = 1)
        age = horse.age
        self.assertEquals(age, 2)

    def test_horse_gender(self):
        horse = Horse.objects.get(id= 1)
        gender = horse.gender
        self.assertEquals(gender, "Male")

    def test_horse_date_of_birth(self):
        horse = Horse.objects.get(id = 1)
        date_of_birth = horse.date_of_birth
        self.assertEquals(date_of_birth, datetime.date(2016, 1, 1))

    def test_reminder_event(self):
        reminder = AddReminder.objects.get(id = 1)
        event = reminder.event
        self.assertEquals(event,"new reminder")

    def test_reminder_note(self):
        reminder = AddReminder.objects.get(id = 1)
        notes = reminder.notes
        self.assertEquals(notes, "just remind me!")

    def test_reminder_date(self):
        reminder = AddReminder.objects.get(id = 1)
        date = reminder.date
        self.assertEquals(date, datetime.date(2018,12,12))

    def test_reminder_time(self):
        reminder = AddReminder.objects.get(id = 1)
        time = reminder.time
        self.assertEquals(time, datetime.time(12, 0))

    def test_performance_event(self):
        performance = AddPerformance.objects.get(id = 1)
        event = performance.event
        self.assertEquals(event, "Running")

    def tes_test_performance_duration(self):
        performance = AddPerformance.objects.get(id = 1)
        duration = perfromance.duration
        self.assertEquals(duration, 20)

    def test_performance_additional(self):
        performance = AddPerformance.objects.get(id = 1)
        additional = performance.additional
        self.assertEquals(additional, "just a run")

    def test_performance_time(self):
        performance = AddPerformance.objects.get(id = 1)
        time = performance.time
        self.assertEquals(time, datetime.time(11,20))
