from django.db import models


class Shaharlar(models.Model):
    image = models.ImageField(upload_to='City_image/')
    title = models.CharField(max_length=155)
    description = models.TextField()

    def __str__(self):
        return self.title


class Tumanlar(models.Model):
    image = models.ImageField(upload_to='Region_image/')
    title = models.CharField(max_length=155)
    description = models.TextField()

    def __str__(self):
        return self.title


class Loyihalar(models.Model):

    class Loyiha_turi(models.TextChoices):
        Sanoat_loyihalar = 'Sanoat_loyihalar'
        Qishloq_xojaligi_loyihalar = 'Qishloq_xojaligi_loyihalar'
        Xizmat_korsatish_loyihalar = 'Xizmat_korsatish_loyihalar'

    class State(models.TextChoices):
        Tugallangan = 'Tugallangan'
        Tugallanmagan = 'Tugallanmagan'

    image = models.ImageField('upload_to/Loyihalar/')
    title = models.CharField(max_length=155)
    description = models.TextField()
    state = models.CharField(max_length=155, choices=State.choices, default=State.Tugallanmagan)
    loyiha_turi = models.CharField(max_length=155, choices=Loyiha_turi.choices, default=Loyiha_turi.Sanoat_loyihalar)

    def __str__(self):
        return self.title