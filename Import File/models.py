from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=100)
    book = models.FileField(blank=True)
    author = models.CharField(max_length=100)
