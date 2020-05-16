from django.urls import path

from . import views

app_name = 'AIT2020'
urlpatterns = [
    path('', views.home, name='home')
]