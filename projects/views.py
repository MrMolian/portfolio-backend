
from django.shortcuts import render
from rest_framework import generics
from rest_framework.viewsets import ViewSet
from .models import Project
from rest_framework import filters
from .serializers import ProjectSerializer
from django_filters.rest_framework import DjangoFilterBackend

class ProjectAPIView(generics.ListAPIView):
        queryset = Project.objects.all()
        serializer_class = ProjectSerializer
        filter_backends = [DjangoFilterBackend,
                           filters.SearchFilter,
			 filters.OrderingFilter]
        search_fields = ['ladate']
