from django.db import models

class SkincareProduct(models.Model):
    name = models.CharField(max_length=200)
    brand = models.CharField(max_length=100)
    benefits = models.TextField(max_length=500)
    value = models.FloatField()
    category = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.name} ({self.id})'