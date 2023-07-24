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


class Sanoat_loyiha(models.Model):
    title = models.CharField(max_length=155)
    description = models.TextField()
    state = models.BooleanField(default=False)


class Qishloq_xojaligi_loyiha(models.Model):
    title = models.CharField(max_length=155)
    description = models.TextField()
    state = models.BooleanField(default=False)


class Xizmat_korsatish_loyiha(models.Model):
    title = models.CharField(max_length=155)
    description = models.TextField()
    state = models.BooleanField(default=False)
