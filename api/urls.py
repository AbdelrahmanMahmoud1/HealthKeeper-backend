
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', views.getRoutes),
    path('dashboard', include('dashboard.urls')),
    path('mydocuments/upload/',views.file_upload_api_view),
    path('mydocuments/getfiles/<str:pk>',views.getFiles), 
    path('mydocuments/viewfile/<str:pk>',views.viewFile),
    path('mydocuments/delete/<str:pk>',views.deleteDocument),
    path('medications/<str:pk>',views.getMedications),
    path('medications/add/',views.addMedication),
    path('medications/delete/<str:pk>',views.deleteMedication),
    path('appointments/<str:pk>',views.getAppointments),
    path('appointments/add/',views.addAppointment),
    path('appointments/delete/<str:pk>',views.deleteAppointment),
    # path('medications/',admin.site.urls), 
    # path('appointments/',admin.site.urls),
    # path('symptoms/',admin.site.urls) ,
    path('profile/<str:id>',views.getUserProfile),
    path('profile/chronic/get/<str:id>',views.getChronicConditions),
    path('profile/chronic/add',views.addChronicConditions),
    path('profile/chronic/delete/<str:pk>',views.deleteChronicCondition),
    path('profile/createuser/add',views.addUser),
    path('profile/updateuser/update',views.updateUser),
    path('profile/user/login',views.login),
    path('symptoms/check',views.check),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

