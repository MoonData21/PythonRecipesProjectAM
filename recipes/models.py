from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Recipe(models.Model):
    CATEGORY_CHOICES = [
        ('main', 'Main Dish'),
        ('side', 'Side Dish'),
        ('dessert', 'Dessert'),
        ('breakfast', 'Breakfast'),
        ('snack', 'Snack')
    ]

    title = models.CharField(max_length=100)
    description = models.TextField()
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='main')  # <-- Added category field

    author = models.ForeignKey(User, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse("recipes-detail", kwargs={"pk": self.pk})

    def __str__(self):
        return self.title  # <-- Fixed to return a string, not a tuple