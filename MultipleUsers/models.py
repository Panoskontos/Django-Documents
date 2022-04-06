from django.db import models
from django.contrib.auth.models import User, AbstractUser


class CustomUser(AbstractUser):
    USER_TYPE_CHOICES = (
        ('student', 'student'),
        ('teacher', 'teacher'),
        ('secretary', 'secretary'),
        ('supervisor', 'supervisor'),
        ('admin', 'admin'),
    )

    user_type = models.PositiveSmallIntegerField(
        choices=USER_TYPE_CHOICES, null=True)


class First(models.Model):
    username = models.OneToOneField(
        CustomUser, on_delete=models.CASCADE, null=True)
