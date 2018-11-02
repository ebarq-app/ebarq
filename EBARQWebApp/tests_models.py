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
        horse = Horse.objects.create(horse_owner = horse_owner, name = "Barry",age = 10)
        reminder = AddReminder.objects.create(horse = horse, time = '12:00 pm', event = "new reminder", date = "2018-12-12", notes = "just remind me!")

        performance = AddPerformance.objects.create(horse = horse, time = '11:20 am', duration = 20, event = "Running", additional = "just a run")
        record = EbarqRecord.objects.create(horse = horse, record_id = 10, start_stamp = '2019-12-12', end_stamp = '2019-12-12')
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
        self.assertEquals(age, 10)

    def test_horse_questionare_required(self):
        horse = Horse.objects.get(id = 1)
        questionare_required = horse.questionare_required
        self.assertEquals(questionare_required,True)

    def test_horse_foreign_key(self):
        horse = Horse.objects.get(id = 1)
        owner = horse.horse_owner
        self.assertEquals(owner.id,1)

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

    def test_reminder_foreign_key(self):
        reminder = AddReminder.objects.get(id = 1)
        horse = reminder.horse
        self.assertEquals(horse.id, 1)

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

    def test_performance_foreign_key(self):
        performance = AddPerformance.objects.get(id = 1)
        horse = performance.horse
        self.assertEquals(horse.id, 1)

    def test_record_id(self):
        record = EbarqRecord.objects.get(id = 1)
        record_id = record.record_id
        self.assertEquals(record_id, 10)

    def test_record_start_stamp(self):
        record = EbarqRecord.objects.get(id = 1)
        start = record.start_stamp
        self.assertEquals(start, datetime.date(2019,12,12))

    def test_record_end_stamp(self):
        record = EbarqRecord.objects.get(id = 1)
        end = record.end_stamp
        self.assertEquals(end, datetime.date(2019,12,12))

    def test_record_foreign_key(self):
        record = EbarqRecord.objects.get(id = 1)
        horse = record.horse
        self.assertEquals(horse.id, 1)
