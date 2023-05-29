"""
This file contains URL patterns for 'employee' app,
It uses a DefaultRouter to generate views
"""
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from employee import views

router = DefaultRouter()
router.register('employees', views.EmployeeViewSet, basename='image-gallery')

urlpatterns = [
    path('', include(router.urls)),
]
