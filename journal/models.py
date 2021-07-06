from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.deletion import CASCADE
from django.core.validators import MaxValueValidator, MinValueValidator 


class User(AbstractUser):

    # Return string representation of object
    def __str__(self):
        return f"{self.username}: {self.email}"


# User has many Entries
class Entry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="entries")
    timestamp = models.DateTimeField(auto_now_add=True)
    mood = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    events = models.CharField(max_length=1500, blank=True, default="")
    negative_thoughts = models.CharField(max_length=1500, blank=True, default="")
    positive_thoughts = models.CharField(max_length=1500, blank=True, default="")

    def __str__(self):
        return f"{self.user.username}'s entry on {self.timestamp}"


# User has many Activities
# Entries have many Activities, Activities have many Entries
class Activity(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="activities")
    entries = models.ManyToManyField(Entry, blank=True)
    name = models.CharField(max_length=50)

    def __str__(self):
        return f"Activity: {self.name}"


# Entries have many Distortions, Distortions have many Entries
class Distortion(models.Model):
    entries = models.ManyToManyField(Entry, blank=True)
    name = models.CharField(max_length=50)
    icon = models.CharField(max_length=50)
    blurb = models.CharField(max_length=500)
    description = models.CharField(max_length=2000, blank=True, default="")

    def __str__(self):
        return f"Distortion: {self.name}"
