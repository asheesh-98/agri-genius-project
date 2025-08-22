from rest_framework import serializers
from .models import DiseaseDetectionRequest

class DiseaseDetectionRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = DiseaseDetectionRequest
        fields = '__all__'
