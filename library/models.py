from django.db import models
# Create your models here.
# Create a Book model with attributes: title, author, genre, status

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    genre = models.CharField(max_length=255)
    status = models.CharField(max_length=255)

def __str__(self):
        return self.title