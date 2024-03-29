"""myscrumy URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import include, url
from rest_framework import routers
from samuelamujoscrumy import views

router = routers.DefaultRouter()
router.register(r'users', views.ScrumUserViewSet)
router.register(r'ScrumyGoals', views.ScrumGoalViewSet)
# router = routers.DefaultRouter()

#  router.register(r'users', views.ScrumUserViewSet)
#  routers.register(r'ScrumyGoal', views.ScrumGoalViewSet)

app_name = 'samuelamujoscrumy'

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('index/', include('samuelamujoscrumy.urls')),
    path('admin/', admin.site.urls),
    path('samuelamujoscrumy/', include('samuelamujoscrumy.urls')),
    
        
]
