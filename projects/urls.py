from django.contrib import admin
from django.urls import path,include
from rest_framework.routers import DefaultRouter

from . import views
urlpatterns = [
     path('projets/', views.ProjectAPIView.as_view(), name='projet-list'),
     path('message/', views.MessageAPIView.as_view(), name='message-list'),
]
