from django.db import models

# Create your models here.


class Product(models.Model):
	nameProduct = models.CharField(max_length=25)
