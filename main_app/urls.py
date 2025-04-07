from django.urls import include, path
from . import views # Import views to connect routes to view functions
from django.contrib import admin
from django.contrib.auth.views import LogoutView 


urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('skincare/all_skincare/', views.all_skincare, name='all_skincare'),
    path('skincare/morning/', views.morning, name='morning'),
    path('skincare/evening/', views.evening, name='evening'),
    path('skincare/weekly/', views.weekly, name='weekly'),
    path('skincare/sera_skincare/', views.sera_skincare, name='sera_skincare'),
    path('skincare/<int:product_id>/', views.product_detail, name='product_detail'),
    path('skincare/create/', views.ProductCreate.as_view(), name='product_create'),
    path('skincare/<int:pk>/update/', views.ProductUpdate.as_view(), name='product_update'),
    path('skincare/<int:pk>/delete/', views.ProductDelete.as_view(), name='product_delete'),
    path('logs/usage_logs/', views.usage_logs, name="usage_logs"),
    path('logs/add_usage_log/', views.add_usage_log, name='add_usage_log'),
    path('accounts/signup/', views.signup, name='signup'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
