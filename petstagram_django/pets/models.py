from django.db import models


# Create your models here.

class Pets(models.Model):
    TYPE_CHOICE_DOG = 'dog'
    TYPE_CHOICE_CAT = 'cat'
    TYPE_CHOICE_PARROT = 'parrot'

    TYPE_CHOICES = (
        (TYPE_CHOICE_DOG, 'dog'),
        (TYPE_CHOICE_CAT, 'cat'),
        (TYPE_CHOICE_PARROT, 'parrot'),
    )

    type = models.CharField(
        max_length=6,
        choices=TYPE_CHOICES,
    )
    name = models.CharField(
        max_length=6,
    )
    age = models.PositiveIntegerField(
        # validators=[
        #     models.Min(1)
        # ]
    )
    description = models.TextField()

    image = models.ImageField(
        upload_to='pets',
    )


class Like(models.Model):
    pet = models.ForeignKey(Pets, null=True, on_delete=models.CASCADE)
