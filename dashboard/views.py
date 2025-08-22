from django.shortcuts import render
from rest_framework import viewsets
from .models import UserActivity, SalesAnalytics
from .serializers import UserActivitySerializer, SalesAnalyticsSerializer
from rest_framework.permissions import IsAuthenticated

# Create your views here.

class UserActivityViewSet(viewsets.ModelViewSet):
    queryset = UserActivity.objects.all()
    serializer_class = UserActivitySerializer
    permission_classes = [IsAuthenticated]

class SalesAnalyticsViewSet(viewsets.ModelViewSet):
    queryset = SalesAnalytics.objects.all()
    serializer_class = SalesAnalyticsSerializer
    permission_classes = [IsAuthenticated]
