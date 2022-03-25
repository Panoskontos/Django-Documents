from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    STATUS = (
        ('In stock', 'In stock'),
        ('Out for Delivery', 'Out for Delivery'),
        ('Delivered', 'Delivered'),
    )
    status = models.CharField(max_length=100, choices=STATUS)
