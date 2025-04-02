"""
URLconf pour l'application oc_lettings_site.

Ce fichier contient la configuration des URL pour l'application Django. Il lie les URL aux
vues correspondantes, y compris celles des modules lettings et profiles. Il définit aussi
l'URL de l'administration Django.
"""
from django.contrib import admin
from django.urls import path

from oc_lettings_site import views
from lettings import views as lettings_views
from profiles import views as profiles_views

urlpatterns = [
    path('', views.index, name='index'),
    path('lettings/', lettings_views.index, name='lettings_index'),
    path('lettings/<int:letting_id>/', lettings_views.letting, name='letting'),
    path('profiles/', profiles_views.index, name='profiles_index'),
    path('profiles/<str:username>/', profiles_views.profile, name='profile'),
    path('admin/', admin.site.urls),
]
