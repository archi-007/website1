from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Guitar(models.Model):
    guitar_name = models.CharField(max_length = 50)
    guitar_price = models.IntegerField()
    guitar_image = models.ImageField(upload_to='images')
    guitar_type = models.CharField(max_length = 50)
    cut = models.CharField(max_length=50)
    truss = models.CharField(max_length = 5)
    top = models.CharField(max_length=50)
    sideback = models.CharField(max_length=50)
    feature_1 = models.CharField(max_length=50)
    feature_2 = models.CharField(max_length=50)
    feature_3 = models.CharField(max_length=50)
    feature_4 = models.CharField(max_length=50)
    pickup = models.CharField(max_length=50)

    def __str__(self):
        return self.guitar_name

class Accessories(models.Model):
    acc_name = models.CharField(max_length = 50)
    acc_price = models.IntegerField()
    acc_image = models.ImageField(upload_to='images')
    feature_1 = models.CharField(max_length=50)
    feature_2 = models.CharField(max_length=50)
    feature_3 = models.CharField(max_length=50)
    feature_4 = models.CharField(max_length=50)
    feature_5 = models.CharField(max_length=50)

    def __str__(self):
        return self.acc_name



class Apparel(models.Model):
    app_name = models.CharField(max_length = 50)
    app_price = models.IntegerField()
    app_image = models.ImageField(upload_to='images')
    feature_1 = models.CharField(max_length=50)
    feature_2 = models.CharField(max_length=50)
    feature_3 = models.CharField(max_length=50)

    def __str__(self):
        return self.app_name


