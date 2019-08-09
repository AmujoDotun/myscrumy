from django import forms
from .models import ScrumyGoals
from django.contrib.auth import get_user_model

class SignupForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = ['first_name', 'last_name', 'email', 'username', 'password']
        widgets = {
            'first_name' : forms.TextInput(
                attrs={'class':'form-control','placeholder':'e.g Louis'}
             ),
            'last_name':forms.TextInput(
                attrs={'class':'form-control','placeholder':'e.g Eyoma'}
            ),
            'username':forms.TextInput(
                attrs={'class':'form-control','placeholder':'e.g LouisEyoma'}
            ),
            'email':forms.TextInput(
                attrs={'class':'form-control', 'type': 'email', 'placeholder':'e.g louiseyoma@linuxjobber.com'}
            ),
            'password':forms.TextInput(
                attrs={'class':'form-control', 'type': 'password', 'placeholder':'Password'}
            )
        }

class CreateGoalForm(forms.ModelForm):
    class Meta:
        model = ScrumyGoals
        fields = ['goal_name', 'user']
        widgets = {
            'goal_name':forms.TextInput(
                attrs={'class':'form-control','placeholder':'E.g Learn How To Code'}
            ),
            'user':forms.Select(
                attrs={'class':'form-control','placeholder':'E.g Learn How To Code'}
            )
        }