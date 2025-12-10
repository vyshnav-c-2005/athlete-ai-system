from django.urls import path
from . import views

urlpatterns = [
    path('profile/', views.profile, name='profile'),
    path('profile/edit/', views.edit_profile, name='edit_profile'),

    # Dashboards
    path('dashboard/', views.dashboard, name='dashboard'),  # Dispatcher
    path('dashboard/athlete/', views.athlete_dashboard, name='athlete_dashboard'),
    path('dashboard/coach/', views.coach_dashboard, name='coach_dashboard'),

    # Signups
    path('signup/athlete/', views.signup_athlete, name='signup_athlete'),
    path('signup/coach/', views.signup_coach, name='signup_coach'),
    
    # Auth (using Django's built-in views, but we might need custom templates)
    path('login/', views.login_view, name='login'), # We'll need a custom login view or use auth_views
    path('logout/', views.logout_view, name='logout'), # Same for logout
]
