from django.shortcuts import render
from rest_framework import viewsets
from .models import Scheme
from .serializers import SchemeSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class SchemeViewSet(viewsets.ModelViewSet):
    queryset = Scheme.objects.all()
    serializer_class = SchemeSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

# Create your views here.
