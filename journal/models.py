from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.deletion import CASCADE
from django.core.validators import MaxValueValidator, MinValueValidator
from django.urls.base import reverse
from django.utils.text import Truncator
from django.utils import timezone


class User(AbstractUser):

    def top_distortions(self):
        distortions_dict = {}

        # Create dict of dicts structured:
        # {distortion_id: {"distortion": distortion, "count": count}}
        for entry in self.entries.all():
            for distortion in entry.distortion_set.all():

                if distortion.id in distortions_dict:
                    distortions_dict[distortion.id]["count"] += 1
                else:
                    distortions_dict[distortion.id] = {"distortion": distortion, "count": 1}

        # Get rid of id keys from dict since no longer needed and convert to list
        distortions_list = distortions_dict.values()

        # Return sorted list of distortions based on count, descending
        return sorted(distortions_list, key = lambda i: i["count"], reverse=True)


    def top_activities(self):
        activities_dict = {}

        # Create dict of dicts structured:
        # {activity_id: {"activity": activity, "count": count}}
        for entry in self.entries.all():
            for activity in entry.activity_set.all():

                if activity.id in activities_dict:
                    activities_dict[activity.id]["count"] += 1
                else:
                    activities_dict[activity.id] = {"activity": activity, "count": 1}

        # Get rid of id keys from dict since no longer needed and convert to list
        activities_list = activities_dict.values()

        # Return sorted list of activities based on count, descending
        return sorted(activities_list, key = lambda i: i["count"], reverse=True)


    def mood_over_time(self):        
        # Query for all entries
        entries = self.entries.order_by('-timestamp')
        data = []
        
        for entry in entries:
            data.append({
                "timestamp": entry.timestamp,
                "mood": entry.mood
            })

        return data


    def mood_totals(self):
        # Query for all entries
        entries = self.entries.all()
        data = {
            "Awful": 0,
            "Bad": 0,
            "Neutral": 0,
            "Good": 0,
            "Great": 0
        }
        
        for entry in entries:
            if entry.mood == 1:
                data["Awful"] += 1
            elif entry.mood == 2:
                data["Bad"] += 1
            elif entry.mood == 3:
                data["Neutral"] += 1
            elif entry.mood == 4:
                data["Good"] += 1
            elif entry.mood == 5:
                data["Great"] += 1

        return data

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

    def get_time(self):
        return "{:d}:{:02d}".format(self.timestamp.hour, self.timestamp.minute)

    def get_date(self):
        return "{:d}-{:02d}-{:02d}".format(self.timestamp.year, self.timestamp.month, self.timestamp.day)

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
