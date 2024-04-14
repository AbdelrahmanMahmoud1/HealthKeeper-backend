from django.shortcuts import render
from .models import Medications

# Create your views here.
def getMedications(id):
    medications = Medications.objects.filter(userId = id)
    return medications

def deleteMedication(id):
    medication = Medications.objects.get(id=id)
    Medications.delete(medication)
    return 