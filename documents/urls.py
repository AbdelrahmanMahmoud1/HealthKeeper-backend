from django.urls import path, include
from . import views
from django.views.decorators.csrf import csrf_exempt
urlpatterns = [
    path('upload/', csrf_exempt(views.upload_file)),
]
