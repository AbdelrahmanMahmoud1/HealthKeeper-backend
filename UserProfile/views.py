from django.shortcuts import render
from .models import UserProfile, ChronicCondition
# Create your views here.


def getUserProfile(id):
    userProfile = UserProfile.objects.get(id=id)
    return userProfile

def getChronicConditions(id):
    conditions = ChronicCondition.objects.filter(userId=id)
    return conditions

def updateUser(data):
    user = UserProfile.objects.get(id=data['userId'])
    user.name=data['name']
    user.email=data['email']
    user.bloodType=data['bloodType']
    user.age=data['age']
    user.weight=data['weight']
    user.height=data['height']
    user.EmergencyMobileNumber= data['EmergencyMobileNumber']
    user.mobileNumber= data['mobileNumber']
    user.save()
    return user



def deleteChronicConditions(id):
    conditions = ChronicCondition.objects.get(id=id)
    ChronicCondition.delete(conditions)
    return 


def login(email):
    print(email)
    user = UserProfile.objects.get(email=email)
    return user.id
