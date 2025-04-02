from django.db import models
from django.urls import reverse

class SkincareProduct(models.Model):
    name = models.CharField(max_length=200)
    brand = models.CharField(max_length=100)
    benefits = models.TextField(max_length=500)
    value = models.FloatField()
    category = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.name} ({self.id})'
    
    def get_absolute_url(self):
        # Use the 'reverse' function to dynamically find the URL for viewing this cat's details
        return reverse('all_skincare')