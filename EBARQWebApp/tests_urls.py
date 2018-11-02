from django.urls import reverse
from django.conf.urls import url, include
from . import urls
from django.test import TestCase


class UrlsTest(TestCase):

    def test_index(self):
        url = reverse('index')
        self.assertEqual(url, '/')

    def test_login(self):
        url = reverse('login')
        self.assertEqual(url, '/login/')

    def test_signup(self):
        url = reverse('signup')
        self.assertEqual(url, '/signup/')

    def test_dashboard(self):
        url = reverse('dashboard')
        self.assertEqual(url, '/dashboard/')

    def test_horseadd(self):
        url = reverse('horse_add')
        self.assertEqual(url, '/horse_add/')

    def test_eidt_horse(self):
        url = reverse('edithorse', args =[100])
        self.assertEqual(url, '/edithorse/100/')

    def test_delete_reminder(self):
        url = reverse('delete_reminder', args =[21])
        self.assertEqual(url, '/delete_reminder/21')

    def test_eidt_reminder(self):
        url = reverse('edit_reminder', args =[21])
        self.assertEqual(url, '/edit_reminder/21')

    def test_eidt_performance(self):
        url = reverse('edit_performance', args =[35])
        self.assertEqual(url, '/edit_performance/35')

    def test_delete_performance(self):
        url = reverse('delete_performance', args =[35])
        self.assertEqual(url, '/delete_performance/35')

    def test_question(self):
        url = reverse('question')
        self.assertEqual(url, '/question/')

    def test_ebarqdashboard(self):
        url = reverse('ebarqdashboard')
        self.assertEqual(url, '/ebarqdashboard/')

    def test_survey_complete(self):
        url = reverse('survey_complete', args = ['test1@gmail.com', 2, 3])
        self.assertEqual(url, '/survey_complete/test1@gmail.com/2/3/')

    def test_userprofile(self):
        url = reverse('userprofile')
        self.assertEqual(url, '/userprofile/')

    def test_editprofile(self):
        url = reverse('editprofile')
        self.assertEqual(url, '/editprofile/')

    def test_horseprofile(self):
        url = reverse('horseprofile')
        self.assertEqual(url, '/horseprofile/')

    def test_horse_indepth(self):
        url = reverse('horse_inDepth', args=[3])
        self.assertEqual(url, '/horse_inDepth/3/')

    def test_graph(self):
        url = reverse('graph', args=[2])
        self.assertEqual(url, '/graph/2/')

    def test_addperformance(self):
        url = reverse('addperformance', args=[10])
        self.assertEqual(url, '/addperformance/10/')

    def test_addreminder(self):
        url = reverse('addreminder', args=[10])
        self.assertEqual(url, '/addreminder/10/')

    def test_horseReminders(self):
        url = reverse('horseReminders')
        self.assertEqual(url, '/horseReminders/')

    def test_setting(self):
        url = reverse('setting')
        self.assertEqual(url, '/setting/')

    def test_PIS(self):
        url = reverse('PIS')
        self.assertEqual(url, '/PIS/')
