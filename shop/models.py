from django.db import models

class Auth(models.Model):
    name = models.CharField(max_length=100)

class Saled(models.Model):
    customer = models.ForeignKey(Auth, on_delete=models.CASCADE)
    prodect = models.CharField(max_length=500)

class Category(models.Model):
    name = models.CharField(max_length=300)

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=500)
    price = models.IntegerField()
    date_term = models.DateField()

class Shopcard(models.Model):
    owner = models.ForeignKey(Auth, on_delete=models.CASCADE)
    number = models.IntegerField()

class Items(models.Model):
    pass

class Admin(models.Model):
    name = models.CharField(max_length=50)