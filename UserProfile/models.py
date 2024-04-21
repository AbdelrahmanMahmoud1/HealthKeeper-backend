from django.db import models
import uuid

# Create your models here.

class UserProfile(models.Model):
    name = models.CharField(max_length=250, blank=True, null=True)
    email = models.EmailField(max_length=250,unique=True)
    age = models.IntegerField(null=True, blank=True)
    weight = models.DecimalField(null=True, blank=True,max_digits=5 ,decimal_places=2)
    height = models.DecimalField(null=True, blank=True,max_digits=5, decimal_places=2)
    bloodType = models.CharField(max_length=3, null=True, blank=True)
    mobileNumber = models.IntegerField(null=True, blank=True)
    EmergencyMobileNumber = models.IntegerField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    url = models.CharField(max_length=3000, null=True, blank=True)

    def __str__(self):
        return self.name
    
class ChronicCondition(models.Model):
    name = models.CharField(max_length=250)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    description = models.TextField(null=True, blank=True)
    userId = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    date= models.DateTimeField()

    def __str__(self):
        return self.name