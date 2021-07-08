from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.deletion import CASCADE
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils.text import Truncator
from django.utils import timezone


class User(AbstractUser):
    
    # Return dict of dicts structured:
    # {distortion_id: {"distortion": distortion, "count": count}}
    def top_distortions(self):        
        distortions_dict = {}

        for entry in self.entries.all():
            for distortion in entry.distortion_set.all():
                
                # if distortion.id in distortions_dict:
                #     distortions_dict[distortion.id][1] += 1
                # else:
                #     distortions_dict[distortion.id] = [distortion, 1]

                if distortion.id in distortions_dict:
                    distortions_dict[distortion.id]["count"] += 1
                else:
                    distortions_dict[distortion.id] = {"distortion": distortion, "count": 1}

        return distortions_dict

    # Return list of lists structured:
    # ["activity": activity, "count": number]
    def top_activities(self):
        activities = []
        return activities
    
    # Return 4 most recent entries
    def recent_entries(self):
        return self.entries.order_by('-timestamp')[:4]

    # Return string representation of object
    def __str__(self):
        return f"{self.username}: {self.email}"


# User has many Entries
class Entry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="entries")
    timestamp = models.DateTimeField(default=timezone.now)
    mood = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    events = models.CharField(max_length=1500, blank=True, default="")
    negative_thoughts = models.CharField(max_length=1500, blank=True, default="")
    positive_thoughts = models.CharField(max_length=1500, blank=True, default="")

    def truncated_events(self):
        return Truncator(self.events).words(50)

    def __str__(self):
        return f"{self.user.username}'s entry on {self.timestamp}"


# User has many Activities
# Entries have many Activities, Activities have many Entries
class Activity(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="activities")
    entries = models.ManyToManyField(Entry, blank=True)
    name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name}"


# Entries have many Distortions, Distortions have many Entries
class Distortion(models.Model):
    entries = models.ManyToManyField(Entry, blank=True)
    name = models.CharField(max_length=50)
    icon = models.CharField(max_length=50)
    blurb = models.CharField(max_length=500)
    description = models.CharField(max_length=2000, blank=True, default="")

    def __str__(self):
        return f"{self.name}"
