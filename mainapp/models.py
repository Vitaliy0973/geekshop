from email.mime import image
from operator import mod
# from tkinter import CASCADE
from unicodedata import category, name
'''Models for product and category'''

from django.db import models

# Create your models here.


class ProductCategories(models.Model):
    '''Model for category'''
    name = models.CharField(max_length=64, unique=True)
    descriptions = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    '''Models for product'''
    name = models.CharField(max_length=128)
    image = models.ImageField(upload_to='product_images', blank=True)
    descriptions = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    quantity = models.PositiveIntegerField(default=0)
    category = models.ForeignKey(ProductCategories, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} | {self.category}'
