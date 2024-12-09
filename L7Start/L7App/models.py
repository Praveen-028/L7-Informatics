from django.db import models
from django.contrib.auth.models import User  # Import User model

class IceCream(models.Model):
    name = models.CharField(max_length=100)
    flavor = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Suggestion(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    flavor = models.CharField(max_length=255)
    allergy = models.TextField(blank=True)
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}'s suggestion"
