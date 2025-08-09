from django.db import models
from django.contrib.auth.models import User

class Crop(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100, blank=True)
    description = models.TextField(blank=True)
    avg_price = models.FloatField(default=0.0)
    image = models.ImageField(upload_to='crops/', blank=True, null=True)

    def __str__(self):
        return self.name

class Listing(models.Model):
    farmer = models.ForeignKey(User, on_delete=models.CASCADE)
    crop = models.ForeignKey(Crop, on_delete=models.CASCADE)
    quantity = models.FloatField()
    price = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    pay_later = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.crop.name} by {self.farmer.username}'

class Feedback(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Feedback by {self.user}'

class DiseaseScan(models.Model):
    uploaded_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='disease/')
    result = models.CharField(max_length=200, blank=True)
    confidence = models.FloatField(default=0.0)

    def __str__(self):
        return f'Scan {self.id} - {self.result}'
