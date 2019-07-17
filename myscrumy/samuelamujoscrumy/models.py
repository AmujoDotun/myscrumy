from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class GoalStatus(models.Model):
    status_name = models.CharField(max_length=100)

class ScrumyGoals(models.Model):
    goal_id = models.IntegerField(default=1)
    goal_name = models.CharField(max_length=100)
    created_by = models.CharField(max_length=100)
    moved_by = models.CharField(max_length=100)
    owner = models.CharField(max_length=100)
    goal_status = models.ForeignKey(GoalStatus, on_delete=models.PROTECT)
    user =  models.ForeignKey(User, on_delete=models.CASCADE)

    
class ScrumyHistory(models.Model):
    moved_by = models.CharField(max_length=100)
    created_by = models.CharField(max_length=100)
    moved_from = models.CharField(max_length=100)
    moved_to = models.CharField(max_length=100)
    time_of_action = models.DateTimeField()
    goal = models.ForeignKey(ScrumyGoals, on_delete=models.CASCADE)

