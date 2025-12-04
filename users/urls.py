from django.urls import path
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path('profile/', views.profile, name='profile'),
    path('profile/edit/', views.edit_profile, name='edit_profile'),
    path('signup/athlete/', views.signup_athlete, name='signup_athlete'),
    path('signup/coach/', views.signup_coach, name='signup_coach'),
    path('login/athlete/', TemplateView.as_view(template_name="users/login_athlete.html")),
    path('login/coach/', TemplateView.as_view(template_name="users/login_coach.html")),
    path('dashboard/', views.athlete_dashboard, name='athlete_dashboard'),
]



