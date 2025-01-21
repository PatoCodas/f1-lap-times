from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('delete/<int:lap_time_id>/', views.delete_lap_time, name='delete_lap_time'),
]