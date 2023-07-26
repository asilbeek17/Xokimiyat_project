from django.db import models


class Shaharlar(models.Model):
    image1 = models.ImageField(upload_to='City_image/')
    image2 = models.ImageField(upload_to='City_image/')
    image3 = models.ImageField(upload_to='City_image/')
    title = models.CharField(max_length=155)
    description = models.TextField()

    class Meta:
        verbose_name = 'Shahar'
        verbose_name_plural = 'Shaharlar'

    def __str__(self):
        return self.title


class Tumanlar(models.Model):
    image1 = models.ImageField(upload_to='Region_image/')
    image2 = models.ImageField(upload_to='Region_image/')
    image3 = models.ImageField(upload_to='Region_image/')
    title = models.CharField(max_length=155)
    description = models.TextField()

    class Meta:
        verbose_name = 'Tuman'
        verbose_name_plural = 'Tumanlar'

    def __str__(self):
        return self.title


class Loyiha_turlari(models.Model):
    image = models.ImageField(upload_to='loyiha_turi/')
    title = models.CharField(max_length=155)

    class Meta:
        verbose_name = 'Loyiha_turi'
        verbose_name_plural = 'Loyiha_turlari'

    def __str__(self):
        return self.title


class Holati(models.Model):
    image = models.ImageField(upload_to='state/')
    title = models.CharField(max_length=155)

    class Meta:
        verbose_name = 'Holat'
        verbose_name_plural = 'Holati'

    def __str__(self):
        return self.title


class Loyihalar(models.Model):

    image1 = models.ImageField('upload_to/Loyihalar/')
    image2 = models.ImageField('upload_to/Loyihalar/')
    image3 = models.ImageField('upload_to/Loyihalar/')
    title = models.CharField(max_length=155)
    description = models.TextField()
    state = models.ForeignKey(to=Holati, on_delete=models.CASCADE)
    loyiha_turi = models.ForeignKey(to=Loyiha_turlari, on_delete=models.CASCADE)
    time = models.DateTimeField(auto_now_add=True)
    time = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Loyiha'
        verbose_name_plural = 'Loyihalar'

    def __str__(self):
        return self.title


class Contact(models.Model):
    first_name = models.CharField(max_length=155)
    last_name = models.CharField(max_length=155)
    email = models.EmailField()
    phone_number = models.CharField(max_length=13)
    text = models.TextField()

    class Meta:
        verbose_name = "Bog'lanish"
        verbose_name_plural = "Bog'lanishlar"

    def __str__(self):
        return self.first_name

