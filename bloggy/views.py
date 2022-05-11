from django.shortcuts import render
from django.db import models

# Create your views here.


class phoneCategory(models.Model):
    name = models.CharField(max_length=80)

    def __str__(self) -> str:
        return self.name
        


class phone(models.Model):
    category = models.ForeignKey(
        phoneCategory,
        on_delete=models.CASCADE
    )
    name = models.CharField(max_length = 80)
    phone_image_url = models.CharField(max_length=500)
    description = models.TextField()
    slug = models.SlugField(unique = True)

    def __str__(self) -> str:
        return self.name


