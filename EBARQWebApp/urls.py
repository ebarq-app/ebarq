from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views as auth_views
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    url(r'^$', views.index, name='index'),

    url(r'^login/$', views.login_view, name='login'),
    url(r'^signup/$', views.signup, name='signup'),

    url(r'^dashboard/', views.dashboard, name='dashboard'),
    url(r'^horse_add/',views.horse_add_view, name='horse_add'),
url(r'^horse_add_view_new/',views.horse_add_view_new, name='horse_add_new'),

    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.activate, name='activate'),

    url(r'^dashboard/', views.dashboard, name='dashboard'),
    url(r'^ebarqdashboard/',views.ebarqdashboard, name='ebarqdashboard'),
    url(r'^userprofile/',views.userprofile, name='userprofile'),
    url(r'^editprofile/',views.editprofile, name='editprofile'),
    url(r'^horseprofile/',views.horseprofile, name='horseprofile'),
    url(r'^horse_inDepth/(?P<horse_id>[0-9]+)/$',views.horse_inDepth, name='horse_inDepth'),
    # url(r'^addhorse/', views.addhorse, name='addhorse'),
     url(r'^graph/',views.graph, name='graph'),
    url(r'^addperformance/',views.addperformance, name='addperformance'),
    url(r'^addreminder/',views.addreminder, name='addreminder'),
    url(r'^horseReminders/',views.horseReminders, name='horseReminders'),
     url(r'^setting/',views.setting, name='setting')
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT )
