from django.urls import path
from . import views # Import views to connect routes to view functions

urlpatterns = [
    path('', views.home, name='home'),
    path('morning/', views.morning, name='morning'),
    path('evening/', views.morning, name='evening'),
    path('weekly/', views.morning, name='weekly'),
]
