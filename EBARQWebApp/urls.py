from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),

    url(r'^login/$', views.login_view, name='login'),
    url(r'^signup/$', views.signup, name='signup'),
<<<<<<< HEAD
=======
    url(r'^dashboard/', views.dashboard, name='dashboard'),
    url(r'^horse_add/',views.horse_add_view, name='horse_add'),

>>>>>>> 607c5512be081ffd2c64abb305ddc1a7efdd733b
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.activate, name='activate'),

    url(r'^dashboard/', views.dashboard, name='dashboard'),
    url(r'^ebarqdashboard/',views.ebarqdashboard, name='ebarqdashboard'),
    url(r'^userprofile/',views.userprofile, name='userprofile'),

    url(r'^addperformance/',views.addperformance, name='addperformance'),
    url(r'^addreminder/',views.addreminder, name='addreminder'),
    url(r'^horsedetail/',views.horsedetail, name='horsedetail'),

]
