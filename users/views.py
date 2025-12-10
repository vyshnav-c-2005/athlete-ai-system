from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm


from .models import AthleteProfile, CoachProfile
from .forms import AthleteProfileForm, AthleteSignupForm, CoachSignupForm
from workouts.models import WorkoutLog
import datetime


# -----------------------
# ATHLETE DASHBOARD
# -----------------------
@login_required
def athlete_dashboard(request):
    profile, created = AthleteProfile.objects.get_or_create(user=request.user)

    # Today's calories burned
    today_logs = WorkoutLog.objects.filter(
        user=request.user,
        date__exact=datetime.date.today()
    )
    calories_burned_today = sum([w.calories_burned or 0 for w in today_logs])

    #  until meals module is built
    calories_consumed_today = 0

    # Recent workouts
    recent_workouts = WorkoutLog.objects.filter(
        user=request.user
    ).order_by('-date')[:5]

    # Temporary recommendation
    recommendation = {
        "workout": "Run 3 km at medium pace",
        "diet": "High protein, 2200 calories",
    }

    return render(request, "dashboard_athlete.html", {
        "profile": profile,
        "calories_burned_today": calories_burned_today,
        "calories_consumed_today": calories_consumed_today,
        "recent_workouts": recent_workouts,
        "recommendation": recommendation,
    })


# COACH DASHBOARD

@login_required
def coach_dashboard(request):
    coach_profile, created = CoachProfile.objects.get_or_create(user=request.user)
    athletes = coach_profile.athletes.all()
    
    return render(request, "users/dashboard_coach.html", {
        "coach": coach_profile,
        "athletes": athletes
    })


# ATHLETE PROFILE VIEW

@login_required
def profile(request):
    profile, created = AthleteProfile.objects.get_or_create(user=request.user)
    return render(request, "users/profile.html", {"profile": profile})


# EDIT ATHLETE PROFILE
@login_required
def edit_profile(request):
    profile, created = AthleteProfile.objects.get_or_create(user=request.user)

    if request.method == "POST":
        form = AthleteProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect("profile")
    else:
        form = AthleteProfileForm(instance=profile)

    return render(request, "users/edit_profile.html", {"form": form})


# SIGNUP — ATHLETE

def signup_athlete(request):
    if request.method == "POST":
        form = AthleteSignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data["password"])
            user.save()

            # Create athlete profile
            AthleteProfile.objects.create(user=user)

            login(request, user)

            # Redirect to profile setup page
            return redirect("edit_profile")

    else:
        form = AthleteSignupForm()

    return render(request, "users/signup_athlete.html", {"form": form})



# SIGNUP — COACH

def signup_coach(request):
    if request.method == "POST":
        form = CoachSignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data["password"])
            user.save()

            CoachProfile.objects.create(user=user)

            login(request, user)
            return redirect("coach_dashboard")

    else:
        form = CoachSignupForm()

    return render(request, "users/signup_coach.html", {"form": form})


# DISPATCHER & AUTH

@login_required
def dashboard(request):
    if hasattr(request.user, 'coachprofile'):
        return redirect('coach_dashboard')
    elif hasattr(request.user, 'athleteprofile'):
        return redirect('athlete_dashboard')
    return redirect('profile')

def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('dashboard')
    else:
        form = AuthenticationForm()
    return render(request, "users/login.html", {"form": form})

def logout_view(request):
    logout(request)
    return redirect('home')

