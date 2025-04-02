from django.urls import path
from . import views # Import views to connect routes to view functions

urlpatterns = [
    path('', views.home, name='home'),
    path('skincare/all_skincare/', views.all_skincare, name='all_skincare'),
    path('skincare/morning/', views.morning, name='morning'),
    path('skincare/evening/', views.evening, name='evening'),
    path('skincare/weekly/', views.weekly, name='weekly'),
    path('skincare/<int:product_id>/', views.product_detail, name='product_detail'),
    path('skincare/create/', views.ProductCreate.as_view(), name='product_create'),
    path('skincare/<int:pk>/update/', views.ProductUpdate.as_view(), name='product_update'),
    path('skincare/<int:pk>/delete/', views.ProductDelete.as_view(), name='product_delete'),
]
