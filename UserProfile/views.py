from django.shortcuts import render
from .models import UserProfile
# Create your views here.


def getUserProfile(id):
    userProfile = UserProfile.objects.get(id=id)
    return userProfile
