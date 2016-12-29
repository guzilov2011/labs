from django.db import models

# Create your models here.


class BookModel(models.Model):
    name = models.CharField(max_length=30)
    author = models.CharField(max_length=30)
    publisher = models.CharField(max_length=30)
    pages_num = models.IntegerField(default = 0)


class OrderModel(models.Model):
    customer = models.CharField(max_length=30)
    description = models.CharField(max_length=30)
    books_num = models.IntegerField(default=0)
    book = models.ManyToManyField(BookModel)
