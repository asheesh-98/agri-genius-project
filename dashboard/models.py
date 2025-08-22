from django.db import models
from users.models import User

# Create your models here.

class UserActivity(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    action = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True)

class SalesAnalytics(models.Model):
    date = models.DateField()
    total_sales = models.DecimalField(max_digits=12, decimal_places=2)
    total_orders = models.PositiveIntegerField()
