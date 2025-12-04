from django.urls import path
# from django import include 
from . import views

urlpatterns = [
    path('add/', views.add_workout, name='add_workout'),
    path('list/', views.list_workouts, name='list_workouts'),

]
