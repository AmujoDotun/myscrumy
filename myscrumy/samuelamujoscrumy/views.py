from django.shortcuts import render
from django.http import HttpResponse
from .models import ScrumyGoals,GoalStatus,ScrumyHistory
from django.contrib.auth import get_user_model
import random



kwargs = {
    'goal_name': 'Learn Django'
}

def index(request) :
    goal_name=ScrumyGoals.objects.filter(**kwargs)
    # return HttpResponse(ScrumyGoals.objects.filter(goal_name ="Learn Django"))
    return HttpResponse(goal_name)
    # context = {
    #     'kwargs': ScrumyGoals.objects.filter(**kwargs)
    # }
    # return render(request, 'samuelamujoscrumy/index.html', context)
   
    # return HttpResponse('kwargs': ScrumyGoals.objects.filter(**kwargs))




def move_goal(request,goal_id):
    try:
        goal = ScrumyGoals.objects.get(goal_id = goal_id)
        return HttpResponse(goal.goal_name)
    except ScrumyGoals.DoesNotExist:
        return HttpResponse('Whatsup....!!! Sorry what you are looking for doesn\'t exist')



def add_goal(request):
    User = get_user_model()
    goal_stats = GoalStatus.objects.get(status_name="Weekly Goal")
    user = User.objects.get(id=1)
    randint = random.randint(1000,9999)

    
    scrumyGoal = ScrumyGoals(goal_name = "Keep Learning Django",goal_id=randint,created_by="Louis",moved_by="Louis",owner="Louis",goal_status=goal_stats,user=user)
    scrumyGoal.save()
    return HttpResponse('OK')

def home(request):
    scrumy_goal = ScrumyGoals.objects.filter(goal_name="Keep Learning Django")

    return HttpResponse(scrumy_goal)