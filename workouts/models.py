from django.db import models
from django.contrib.auth.models import User

class WorkoutLog(models.Model):
    INTENSITY_CHOICES = [
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    sport_event = models.CharField(max_length=50)
    duration_minutes = models.IntegerField()
    distance_km = models.FloatField(null=True, blank=True)  # always 0 for throwers
    intensity = models.CharField(max_length=10, choices=INTENSITY_CHOICES)
    calories_burned = models.FloatField(null=True, blank=True)  # ML will predict later
    date = models.DateField(auto_now_add=True)
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.user.username} - {self.sport_event} on {self.date}"
