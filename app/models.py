from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=155)


class City(models.Model):
    image = models.ImageField(upload_to='City_image/')
    title = models.CharField(max_length=155)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


class Region(models.Model):
    image = models.ImageField(upload_to='Region_image/')
    title = models.CharField(max_length=155)
    description = models.TextField
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
