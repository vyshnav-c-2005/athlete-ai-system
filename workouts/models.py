from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

INTENSITY_CHOICES = [
    ('low', 'Low'),
    ('medium', 'Medium'),
    ('high', 'High'),
]

class WorkoutLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    duration_minutes = models.IntegerField()
    distance_km = models.FloatField(default=0)
    intensity = models.CharField(max_length=10, choices=INTENSITY_CHOICES)
    average_heart_rate = models.IntegerField()
    sets_reps = models.CharField(max_length=100, blank=True)
    calories_burned = models.FloatField(null=True, blank=True)

    def __str__(self):
        return f"{self.user.username} - {self.date}"
