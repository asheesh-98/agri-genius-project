from django.db import models

# Create your models here.

class Scheme(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    eligibility = models.TextField(blank=True)
    link = models.URLField(blank=True)
    updated_at = models.DateTimeField(auto_now=True)
