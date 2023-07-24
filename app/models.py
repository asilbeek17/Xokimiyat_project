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

    class State(models.TextChoices):
        Tugallangan = 'Tugallangan'
        Tugallanmagan = 'Tugallanmagan'

    image = models.ImageField('upload_to/sanoat_loyiha/')
    title = models.CharField(max_length=155)
    description = models.TextField()
    state = models.CharField(max_length=155, choices=State.choices, default=State.Tugallanmagan)


class Qishloq_xojaligi_loyiha(models.Model):

    class State(models.TextChoices):
        Tugallangan = 'Tugallangan'
        Tugallanmagan = 'Tugallanmagan'

    image = models.ImageField('upload_to/qishloq_xojaligi_loyiha/')
    title = models.CharField(max_length=155)
    description = models.TextField()
    state = models.CharField(max_length=155, choices=State.choices, default=State.Tugallanmagan)


class Xizmat_korsatish_loyiha(models.Model):

    class State(models.TextChoices):
        Tugallangan = 'Tugallangan'
        Tugallanmagan = 'Tugallanmagan'

    image = models.ImageField('upload_to/xizmat_korsatish_loyiha/')
    title = models.CharField(max_length=155)
    description = models.TextField()
    state = models.CharField(max_length=155, choices=State.choices, default=State.Tugallanmagan)
