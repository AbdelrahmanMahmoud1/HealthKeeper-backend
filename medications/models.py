from django.db import models
import uuid
from UserProfile.models import UserProfile

# Create your models here.
class Medications(models.Model):
    name = models.CharField(max_length=500)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    userId = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    time = models.DateTimeField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
