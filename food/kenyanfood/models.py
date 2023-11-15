from django.db import models

# Create your models here.
class Food(models.Model):
    """A model representing the Food object."""

    name = models.CharField(max_length=200)
    description = models.CharField(max_length=500)