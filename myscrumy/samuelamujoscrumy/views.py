from django.shortcuts import render
from django.http import HttpResponse
from .models import ScrumyGoals,GoalStatus,ScrumyHistory
from django.contrib.auth.models import User
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
        return render(request, 'samuelamujoscrumy/exception.html')



def add_goal(request):
    User = get_user_model()
    goal_stats = GoalStatus.objects.get(status_name="Weekly Goal")
    user = User.objects.get(id=1)
    randint = random.randint(1000,9999)

    
    scrumyGoal = ScrumyGoals(goal_name = "Keep Learning Django",goal_id=randint,created_by="Louis",moved_by="Louis",owner="Louis",goal_status=goal_stats,user=user)
    scrumyGoal.save()
    return HttpResponse('OK')


def home(request):
    status = GoalStatus.objects.all()
    users = User.objects.all()
    a = GoalStatus.objects.get(status_name="Weekly Goal")
    goal_stats = a.scrumygoals_set.all()
    b = GoalStatus.objects.get(status_name="Daily Goal")
    goal_stats1 = b.scrumygoals_set.all()
    c = GoalStatus.objects.get(status_name="Verify Goal")
    goal_stats2 = c.scrumygoals_set.all()
    d = GoalStatus.objects.get(status_name="Done Goal")
    goal_stats3 = d.scrumygoals_set.all()
   

    context = {
        'status': status,
        'users': users,
        'goal_stats': goal_stats,
        'goal_stats1': goal_stats1,
        'goal_stats2': goal_stats2,
        'goal_stats3': goal_stats3,
    }
    return render(request, 'samuelamujoscrumy/home.html', context)




# def home(request):
#     User =get_user_model()
#     goal_stats = GoalStatus.objects.get(status_name="Weekly Goal")
    
#     user = User.objects.get(id=1)

#     scrumy_goal = ScrumyGoals.objects.filter(goal_name="Keep Learning Django")

    
#     user = ScrumyGoals.objects.all()

#     return render(request, 'samuelamujoscrumy/home.html', {'user': user, 'scrumy_goal': scrumy_goal})


# def exception(request,goal_id):
#     try:
#         goal = ScrumyGoals.objects.get(goal_id = goal_id)
#         return HttpResponse(goal.goal_name)
#     except ScrumyGoals.DoesNotExist:
#         return render(request, 'samuelamujoscrumy/exception.html')