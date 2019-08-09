from django.urls import path, include
from . import views



urlpatterns = [
    path('', views.index, name='index'),
    path('goal_name', views.goal_name),
    path('movegoal/<int:id>', views.move_goal, name="movegoal"),
    path('addgoal', views.add_goal, name="addgoal"),
    path('home', views.home, name="home"),
    path('accounts/', include('django.contrib.auth.urls')),
]
