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
                                    date_of_birth = "2016-1-1", weight = 100, height = 200)

def setUp(self):
    # print("setUp: Run once for every test method to setup clean data.")
    pass


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

    def test_date_of_birth(self):
        horse = Horse.objects.get(id = 1)
        date_of_birth = horse.date_of_birth
        self.assertEquals(date_of_birth, datetime.date(2016, 1, 1))
