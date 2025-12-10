from django.urls import path
from django.views.generic import TemplateView
from . import views

from django.contrib.auth import views as auth_views

urlpatterns = [
    path('profile/', views.profile, name='profile'),
    path('profile/edit/', views.edit_profile, name='edit_profile'),
    path('signup/athlete/', views.signup_athlete, name='signup_athlete'),
    path('signup/coach/', views.signup_coach, name='signup_coach'),
    
    # Fix: Use LoginView
    path('login/athlete/', auth_views.LoginView.as_view(template_name="users/login_athlete.html"), name='login_athlete'),
    path('login/coach/', auth_views.LoginView.as_view(template_name="users/login_coach.html"), name='login_coach'),
    
    path('dashboard/', views.athlete_dashboard, name='athlete_dashboard'),
    path('coach/dashboard/', views.coach_dashboard, name='coach_dashboard'),
]



