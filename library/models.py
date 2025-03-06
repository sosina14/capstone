# Create your models here.
# Create a Book model with attributes: title, author, genre, status
# library/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('student', 'Student'),
        ('admin', 'Admin'),
        ('superadmin', 'Super Admin'),
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='student')
