# filepath: /c:/Users/migue/Desktop/estudos diversos/tempof1/f1-laptimes/config/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('laptimes.urls')),
]