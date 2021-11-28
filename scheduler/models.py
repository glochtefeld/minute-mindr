from django.db import models

# Create your models here.

class User(models.Model):
    first_name = models.CharField(max_length=20)
    email = models.EmailField()
    password = models.CharField(max_length=255,**{'null':True}) # See input methods.

class Schedule(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=30)

class Activity(models.Model):
    schedule_id = models.ForeignKey(Schedule, on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    color = models.CharField(max_length=15)

class Event(models.Model):
    activity_id = models.ForeignKey(Activity, on_delete=models.CASCADE)
    description = models.CharField(max_length=300)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

# Settings
# class UserPreference(models.Model):
    # pass

# class ConstrainedChoice(models.Model):
    # pass

# class Setting(models.Model):
    # pass
