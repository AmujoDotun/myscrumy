from django.contrib import admin
from samuelamujoscrumy.models import ScrumyGoals,ScrumyHistory,GoalStatus


# Register your models here.

admin.site.register(ScrumyGoals)
admin.site.register(ScrumyHistory)
admin.site.register(GoalStatus)