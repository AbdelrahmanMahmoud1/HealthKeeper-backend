from django.shortcuts import render
from .models import Appointmets

# Create your views here.
def getAppointments(id):
    medications = Appointmets.objects.filter(userId = id)
    return medications

def deleteAppointment(id):
    medication = Appointmets.objects.get(id=id)
    Appointmets.delete(medication)
    return 