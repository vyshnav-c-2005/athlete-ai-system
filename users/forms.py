from django import forms
from .models import AthleteProfile, CoachProfile
from django.contrib.auth.models import User

class AthleteProfileForm(forms.ModelForm):
    class Meta:
        model = AthleteProfile
        fields = [
            'sport_group',
            'sport_event',
            'age',
            'height_cm',
            'weight_kg',
            'experience_level',
            'training_goal',
            'coach',
        ]


class AthleteSignupForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'password', 'email']


class CoachSignupForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'password', 'email']
