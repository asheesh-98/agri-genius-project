from django.shortcuts import render
from rest_framework import viewsets
from .models import DiseaseDetectionRequest
from .serializers import DiseaseDetectionRequestSerializer
from rest_framework.permissions import IsAuthenticated

class DiseaseDetectionRequestViewSet(viewsets.ModelViewSet):
    queryset = DiseaseDetectionRequest.objects.all()
    serializer_class = DiseaseDetectionRequestSerializer
    permission_classes = [IsAuthenticated]

# Create your views here.
