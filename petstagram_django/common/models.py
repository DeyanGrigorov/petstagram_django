from django.db import models

# Create your models here.
from petstagram_django.pets.models import Pets


class Comment(models.Model):
    pet = models.ForeignKey(Pets, on_delete=models.CASCADE)
    text = models.TextField()
