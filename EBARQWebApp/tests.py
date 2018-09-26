from django.test import TestCase

from EBARQWebApp.models import *
from django.contrib.auth.models import User


class HorseOwnewModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        user = User.objects.create(username = "harold11", password = "Chicken33",
                                   email = "harold.gunderson@gmail.com")
        HorseOwner.objects.create(user_id = user, first_name='Harold',
                                  last_name='Gunderson')

    def test_first_name(self):
        owner = HorseOwner.objects.get(id=1)
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
