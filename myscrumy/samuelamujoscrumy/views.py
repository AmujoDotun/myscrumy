from django.shortcuts import render
from django.http import HttpResponse
from .models import ScrumyGoals,GoalStatus,ScrumyHistory
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
import random
from django import forms
from .forms import SignupForm, CreateGoalForm
from django.contrib.auth.hashers import make_password
from django.contrib import messages
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import Group
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect

from rest_framework import viewsets
from rest_framework.response import Response
from samuelamujoscrumy.serializers import ScrumUserSerializer, ScrumGoalSerializer
from django.contrib.auth.models import User



def index(request):
  if request.method == 'POST':
    form = SignupForm(request.POST)
    if form.is_valid():
        new_user = form.save()
        group = Group.objects.get(name="Developer")
        group.user_set.add(new_user.id)
        messages.success(request,'Your account has been created successfully. Now login')
        return redirect('login')
    else:
      context = {"form": form}
    return render(request, 'samuelamujoscrumy/index.html', context)
  else:
      form = SignupForm()
      context = {"form": form}
  return render(request, 'samuelamujoscrumy/index.html', context)
  
def goal_name(request):
  kwargs = {
    "goal_name": "Learn Django",
  }
  goal = ScrumyGoals.objects.filter(**kwargs)
  return HttpResponse(goal)





def move_goal(request, id):
    try:
        goal = ScrumyGoals.objects.get(goal_id = id)
        if request.method == "POST":
            goalstats = GoalStatus.objects.get(status_name=request.POST.get('goal_stats'))
            goal.goal_status = goalstats
            goal.save()
            messages.success(request,'You Successfully Moved your goal')
            return redirect("home")
        else:
            isDev="False"
            if request.user.groups.filter(name = "Developer").exists() and request.user.username != str(goal.user) or request.user.groups.filter(name = "Owner").exists() and request.user.username != str(goal.user) :
                messages.warning(request,'Sorry, you can only edit '+ request.user.username + ' goals')
                return redirect('home')
            elif request.user.groups.filter(name = "Developer").exists() and request.user.username == str(goal.user):

                isDev = "True"
                context={
                    'isDev':isDev,
                    'goal':str(goal.goal_status)
                }

                return render(request,'samuelamujoscrumy/movegoal.html',context)

            elif request.user.groups.filter(name = "Quality Assurance").exists() or request.user.groups.filter(name = "Admin").exists():

                isDev="False"
                context={
                    'isDev':isDev,
                    'goal':str(goal.goal_status)
                }
                return render(request,'samuelamujoscrumy/movegoal.html',context)

            elif request.user.groups.filter(name = "Owner").exists() and request.user.username == str(goal.user):
                isDev="False"
                context={
                    'isDev':isDev,
                    'goal':str(goal.goal_status)
                }
                return render(request,'samuelamujoscrumy/movegoal.html',context)
            else:
                messages.warning(request,"Can't perform this operation with the current user you are logged in as")
                return redirect("home")

    except ScrumyGoals.DoesNotExist:
        context={
                'invalid_id':id
            }
        return render(request,'samuelamujoscrumy/exception.html',context)


def add_goal(request):
    if request.method =="POST":
        form = CreateGoalForm(request.POST)
        
        if form.is_valid():
            User = get_user_model()
            user_name = User.objects.get(id=request.POST.get('user'))
            if request.user.username == str(user_name)  and request.POST.get('goal_status') == "Weekly Goal":
                goal=form.save(commit=False)
                rand=random.randint(1000,9999)
                goal_status = GoalStatus.objects.get(status_name=request.POST.get('goal_status'))
                goal.goal_id = rand
                goal.goal_status = goal_status
                goal.save()
                return redirect('home')
            elif str(user_name) != request.user.username and request.POST.get('goal_status') == "Weekly Goal":

                userIsDeveloper="False"
                if request.user.groups.filter(name = "Developer").exists():

                    userIsDeveloper="True"

                form = CreateGoalForm()
                
                context = {
                    'form':form,
                    'userIsDeveloper':userIsDeveloper,
                    'GoalStatusErr':request.user.username
                }

                return render(request,'samuelamujoscrumy/addgoal.html',context)
            else:
                goal=form.save(commit=False)
                rand=random.randint(1000,9999)
                goal_stats = GoalStatus.objects.get(status_name="Weekly Goal")
                goal.goal_id = rand
                goal.goal_status_id = '3'
                goal.save()
                return redirect('home')
    else:
        userIsDeveloper="False"
        if request.user.groups.filter(name = "Developer").exists() or request.user.groups.filter(name = "Owner").exists() or request.user.groups.filter(name = "Quality Assurance").exists():
            userIsDeveloper="True"

        form = CreateGoalForm()
        
        context = {
            'form':form,
            'userIsDeveloper':userIsDeveloper
        }

    return render(request,'samuelamujoscrumy/addgoal.html',context)


# def add_goal(request):
#     User = get_user_model()
#     goal_stats = GoalStatus.objects.get(status_name="Weekly Goal")
#     user = User.objects.get(id=1)
#     randint = random.randint(1000,9999)

    
#     scrumyGoal = ScrumyGoals(goal_name = "Keep Learning Django",goal_id=randint,created_by="Louis",moved_by="Louis",owner="Louis",goal_status=goal_stats,user=user)
#     scrumyGoal.save()
#     return HttpResponse('OK')



def home(request):
  User = get_user_model()
  allUsers = User.objects.all()
  datas = []
  for user in allUsers:
    dic = {}
    dic['users'] = user
    w_g = GoalStatus.objects.get(status_name="Weekly Goal")
    dic['w_g'] = user.scrumyUser.filter(goal_status = w_g)
    d_g = GoalStatus.objects.get(status_name="Daily Goal")
    dic['d_g'] = user.scrumyUser.filter(goal_status = d_g)
    v_g = GoalStatus.objects.get(status_name="Verify Goal")
    dic['v_g'] = user.scrumyUser.filter(goal_status = v_g)
    dn_g = GoalStatus.objects.get(status_name="Done Goal")
    dic['dn_g'] = user.scrumyUser.filter(goal_status = dn_g)
    datas.append(dic)
  
  context = {
    'datas': datas
  }
  return render(request, 'samuelamujoscrumy/home.html', context)




class ScrumGoalViewSet(viewsets.ViewSet):
    # display weekly goal
     def user_data(request):
        queryset = User.objects.all()
class UserViewSet(viewsets.ViewSet):
     def user_data(request):
        queryset = User.objects.all()


class ScrumUserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = ScrumUserSerializer


class ScrumGoalViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = ScrumyGoals.objects.all()
    serializer_class = ScrumGoalSerializer