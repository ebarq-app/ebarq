from django.test import TestCase
from EBARQWebApp.models import *
from django.contrib.auth import login, authenticate, logout
# from EBARRQWebApp.views import *
from django.contrib.auth.models import User
from django.urls import reverse

from EBARQWebApp.views import *


class TesFlow(TestCase):
    def setUp(self):
        self.credentials = {
            'username': 'Sanic',
            'password': 'fast123456',
            'email': 'gotta_go@fast.com'
        }
        self.newcredentials = {
            'username': 'Sanic',
            'password': 'fast123456'
        }
        # user = User.objects.create_user(**self.credentials)
        # user.is_active = True
        # user.save()
        # owner.save()

    def test_registration_user_not_activated(self):

        response = self.client.post('/signup', self.credentials, follow=True)
        newresponse = self.client.post('/login/', self.newcredentials)
        self.assertFalse(response.context['user'].is_active)

    def test_invalid_user_login_redirect(self):
        newresponse = self.client.post('/login/', self.newcredentials)
        self.assertTrue(newresponse.status_code, 301)
        self.assertEquals(newresponse["location"],'/login' )

    def test_inactive_user_redirect(self):
        response = self.client.post('/signup/', self.credentials, follow=True)
        newresponse = self.client.post('/login/', self.newcredentials)
        self.assertEquals(newresponse["location"],'/login' )

    def test_active_user_with_no_horse_redirect(self):
        user = User.objects.create_user(**self.credentials)
        owner = HorseOwner.objects.create(user_id = user, first_name = "Sanic", last_name = "sane")
        newresponse = self.client.post('/login/', self.newcredentials)
        self.assertEquals(newresponse["location"],'/PIS')

    def test_active_user_with_horse_redirect(self):
        user = User.objects.create_user(**self.credentials)
        owner = HorseOwner.objects.create(user_id = user, first_name = "Sanic", last_name = "sane")
        horse = Horse.objects.create(horse_owner = owner, name = "Barry", age = 2)
        newresponse = self.client.post('/login/', self.newcredentials)
        self.assertEquals(newresponse["location"],'/dashboard')

    def test_add_horse(self):
        user = User.objects.create_user(**self.credentials)
        owner = HorseOwner.objects.create(user_id = user, first_name = "Sanic", last_name = "sane")
        horse = Horse.objects.create(horse_owner = owner, name = "Barry", age = 2)
        newresponse = self.client.post('/login/', self.newcredentials)
        response = self.client.post('/horse_add/', name = "Barry", age = 2)
        self.assertEquals(newresponse["location"],'/dashboard')

class RenderingTest(TestCase):
    def setUp(self):
        self.credentials = {
            'username': 'Sanic',
            'password': 'fast123456',
            'email': 'gotta_go@fast.com'
        }
        self.newcredentials = {
            'username': 'Sanic',
            'password': 'fast123456'
        }

    def test_signup_render(self):
        response = self.client.get('/signup/')
        self.assertEquals(response.status_code, 200)

    def test_login_render(self):
        response = self.client.get('/login/')
        self.assertEquals(response.status_code, 200)

    def test_dashboard_render(self):
        user = User.objects.create_user(**self.credentials)
        owner = HorseOwner.objects.create(user_id = user, first_name = "Sanic", last_name = "sane")
        newresponse = self.client.post('/login/', self.newcredentials)
        horse = Horse.objects.create(horse_owner = owner, name = "Barry", age = 2)
        response = self.client.get('/dashboard/')
        self.assertEquals(response.status_code, 200)

    def test_horse_add_render(self):
        user = User.objects.create_user(**self.credentials)
        owner = HorseOwner.objects.create(user_id = user, first_name = "Sanic", last_name = "sane")
        newresponse = self.client.post('/login/', self.newcredentials)
        horse = Horse.objects.create(horse_owner = owner, name = "Barry", age = 2)
        response = self.client.get('/horse_add/')
        self.assertEquals(response.status_code, 200)

    def test_horse_add_render(self):
        user = User.objects.create_user(**self.credentials)
        owner = HorseOwner.objects.create(user_id = user, first_name = "Sanic", last_name = "sane")
        newresponse = self.client.post('/login/', self.newcredentials)
        horse = Horse.objects.create(horse_owner = owner, name = "Barry", age = 2)
        response = self.client.get('/horse_add/')
        self.assertEquals(response.status_code, 200)


    def test_horse_profile_render(self):
        user = User.objects.create_user(**self.credentials)
        owner = HorseOwner.objects.create(user_id = user, first_name = "Sanic", last_name = "sane")
        newresponse = self.client.post('/login/', self.newcredentials)
        horse = Horse.objects.create(horse_owner = owner, name = "Barry", age = 2)
        response = self.client.get('/horseprofile/')
        self.assertEquals(response.status_code, 200)

    # def test_horse_indepth_render(self):
    #
    #     user = User.objects.create_user(**self.credentials)
    #     owner = HorseOwner.objects.create(user_id = user, first_name = "Sanic", last_name = "sane")
    #     newresponse = self.client.post('/login/', self.newcredentials)
    #     horse = Horse.objects.create(horse_owner = owner, name = "Barry", age = 2)
    #     response = self.client.get(reverse('horse_inDepth', args=(horse.id)))
    #     self.assertEquals(response.status_code, 200)

    def test_profile_setting_render(self):
        user = User.objects.create_user(**self.credentials)
        owner = HorseOwner.objects.create(user_id = user, first_name = "Sanic", last_name = "sane")
        newresponse = self.client.post('/login/', self.newcredentials)
        horse = Horse.objects.create(horse_owner = owner, name = "Barry", age = 2)
        response = self.client.get('/setting/')
        self.assertEquals(response.status_code, 200)

    def test_pis_render(self):
        user = User.objects.create_user(**self.credentials)
        owner = HorseOwner.objects.create(user_id = user, first_name = "Sanic", last_name = "sane")
        newresponse = self.client.post('/login/', self.newcredentials)
        response = self.client.get('/PIS/')
        self.assertEquals(response.status_code, 200)

    def test_edit_profile_setting_render(self):
        user = User.objects.create_user(**self.credentials)
        owner = HorseOwner.objects.create(user_id = user, first_name = "Sanic", last_name = "sane")
        newresponse = self.client.post('/login/', self.newcredentials)
        horse = Horse.objects.create(horse_owner = owner, name = "Barry", age = 2)
        response = self.client.get('/editprofile/')
        self.assertEquals(response.status_code, 200)

    def test_horse_add_render(self):
        user = User.objects.create_user(**self.credentials)
        owner = HorseOwner.objects.create(user_id = user, first_name = "Sanic", last_name = "sane")
        newresponse = self.client.post('/login/', self.newcredentials)
        horse = Horse.objects.create(horse_owner = owner, name = "Barry", age = 2)
        response = self.client.get('/horse_inDepth/1')
        self.assertEquals(response.status_code, 301)

    def test_edit_profile_setting_unauthenticated_render(self):
        response = self.client.get('/editprofile/')
        self.assertEquals(response["location"],'/login')

    def test_profile_setting_unauthenticated_render(self):
        response = self.client.get('/setting/')
        self.assertEquals(response["location"],'/login')

    def test_horse_profile_unauthenticated_render(self):
        response = self.client.get('/horseprofile/')
        self.assertEquals(response["location"],'/login')

    def test_ebarq_dashboard_unauthenticated_render(self):
        response = self.client.get('/ebarqdashboard/')
        self.assertEquals(response["location"],'/login')

    def test_horse_add_unauthenticated_render(self):
        response = self.client.get('/horse_add/')
        self.assertEquals(response["location"],'/login')

    def test_dashboard_unauthenticated_render(self):
        response = self.client.get('/dashboard/')
        self.assertEquals(response["location"],'/login')

    def test_pis_unauthenticated_render(self):
        response = self.client.get('/PIS/')
        self.assertEquals(response["location"],'/login')
