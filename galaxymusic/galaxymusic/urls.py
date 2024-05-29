
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("", include("hr.urls")),
    path("hr/", include("hr.urls")),
    path("polls/", include("polls.urls")),
    path("api/", include("api.urls")),
    path('admin/', admin.site.urls),
    
    
    
    
]
