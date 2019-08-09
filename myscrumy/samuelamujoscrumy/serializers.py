from django.contrib.auth.models import User
from rest_framework import serializers
from .models import ScrumyGoals





class ScrumUserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email']


class ScrumGoalSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ScrumyGoals
        fields = ['url', 'goal_name']



