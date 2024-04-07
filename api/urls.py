
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
    # path('medications/',admin.site.urls), 
    # path('appointments/',admin.site.urls),
    # path('symptoms/',admin.site.urls) ,
    path('profile/<str:id>',views.getUserProfile),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

