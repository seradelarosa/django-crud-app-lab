from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class SkincareProduct(models.Model):
    name = models.CharField(max_length=200)
    brand = models.CharField(max_length=100)
    benefits = models.TextField(max_length=500)
    value = models.FloatField()
    category = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} ({self.id})'
    
    def get_absolute_url(self):
        # Use the 'reverse' function to dynamically find the URL for viewing this cat's details
        return reverse('all_skincare')
    

class UsageLog(models.Model):
    product = models.ForeignKey(SkincareProduct, on_delete=models.CASCADE, related_name='usage_logs')
    usage_time = models.DateTimeField()
    usage_category = models.CharField(max_length=20, choices=[('morning', 'Morning'), ('evening', 'Evening'), ('weekly', 'Weekly')])
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.product.name} used on {self.usage_time.strftime('%Y-%m-%d %H:%M')}"
