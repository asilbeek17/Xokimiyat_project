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


class Sanoat_loyihalar(models.Model):

    class State(models.TextChoices):
        Tugallangan = 'Tugallangan'
        Tugallanmagan = 'Tugallanmagan'

    image = models.ImageField('upload_to/sanoat_loyiha/')
    title = models.CharField(max_length=155)
    description = models.TextField()
    state = models.CharField(max_length=155, choices=State.choices, default=State.Tugallanmagan)

    def __str__(self):
        return self.title


class Qishloq_xojaligi_loyihalar(models.Model):

    class State(models.TextChoices):
        Tugallangan = 'Tugallangan'
        Tugallanmagan = 'Tugallanmagan'

    image = models.ImageField('upload_to/qishloq_xojaligi_loyiha/')
    title = models.CharField(max_length=155)
    description = models.TextField()
    state = models.CharField(max_length=155, choices=State.choices, default=State.Tugallanmagan)

    def __str__(self):
        return self.title


class Xizmat_korsatish_loyihalar(models.Model):

    class State(models.TextChoices):
        Tugallangan = 'Tugallangan'
        Tugallanmagan = 'Tugallanmagan'

    image = models.ImageField('upload_to/xizmat_korsatish_loyiha/')
    title = models.CharField(max_length=155)
    description = models.TextField()
    state = models.CharField(max_length=155, choices=State.choices, default=State.Tugallanmagan)

    def __str__(self):
        return self.title
