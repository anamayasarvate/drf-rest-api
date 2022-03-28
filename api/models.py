from django.db import models

class Library(models.Model):
    name = models.CharField(max_length=100)
    books_count = models.IntegerField()