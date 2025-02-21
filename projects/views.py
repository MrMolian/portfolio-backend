
from django.shortcuts import render
from rest_framework import generics
from rest_framework.viewsets import ViewSet
from .models import Project,YearMessage
from rest_framework import filters
from .serializers import ProjectSerializer,MessageSerializer
from django_filters.rest_framework import DjangoFilterBackend

class ProjectAPIView(generics.ListAPIView):
        queryset = Project.objects.all()
        serializer_class = ProjectSerializer
        filter_backends = [DjangoFilterBackend,
                           filters.SearchFilter,
			 filters.OrderingFilter]
        search_fields = ['ladate']

class MessageAPIView(generics.ListAPIView):
        queryset = YearMessage.objects.all()
        serializer_class = MessageSerializer
        filter_backends = [DjangoFilterBackend,
                           filters.SearchFilter,
			 filters.OrderingFilter]
        search_fields = ['year']
