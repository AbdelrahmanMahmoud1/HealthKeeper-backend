from django.db import models
import uuid

# Create your models here.

class UserProfile(models.Model):
    name = models.CharField(max_length=250)
    email = models.EmailField(max_length=250)
    age = models.IntegerField(null=True, blank=True)
    weight = models.DecimalField(null=True, blank=True,max_digits=5 ,decimal_places=2)
    height = models.DecimalField(null=True, blank=True,max_digits=5, decimal_places=2)
    bloodType = models.CharField(max_length=3, null=True, blank=True)
    mobileNumber = models.IntegerField(max_length=15,null=True, blank=True)
    EmergencyMobileNumber = models.IntegerField(max_length=15,null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.name