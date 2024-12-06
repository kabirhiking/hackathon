
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    is_doctor = models.BooleanField(default=False)
    phone = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField(blank=True, null=True)


class HealthData(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    metric_type = models.CharField(max_length=50)  # Example: "Steps", "Mood"
    value = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)


class HealthTip(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    tip = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)


class MentalHealthCheckIn(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    mood_score = models.IntegerField()  # Example: 1-10 scale
    feedback = models.TextField(blank=True, null=True)
    mindfulness_suggestion = models.TextField(blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)



