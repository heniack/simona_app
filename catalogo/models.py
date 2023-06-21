from django.db import models


class Categories(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Products(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    image_url = models.URLField(blank=True)
    price= models.IntegerField(null=True)
    stock = models.IntegerField(default = 0)
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

"""class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Products, on_delete=models.CASCADE)"""

    
