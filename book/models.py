from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    year = models.PositiveIntegerField(max_length=4)
    publisher = models.CharField(max_length=100)
    pages = models.IntegerField()
    isbn = models.CharField(max_length=13)

    def __str__(self):
        return self.title
