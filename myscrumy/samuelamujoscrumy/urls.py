from django.urls import path
from django.urls import include
from . import views

urlpatterns = [
    path('', views.index, name='index'),

    path('movegoal/<int:goal_id>', views.move_goal),
    path('addgoal/', views.add_goal),
    path('home/', views.home),
    path('accounts/', include('django.contrib.auth.urls')),
]