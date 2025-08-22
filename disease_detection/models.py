from django.db import models
from users.models import User

# Create your models here.

class DiseaseDetectionRequest(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    crop_image = models.ImageField(upload_to='disease_detection/')
    result = models.CharField(max_length=200, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
