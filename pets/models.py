from django.db import models

# Create your models here.
class SexOptions(models.TextChoices):
    female = 'Female'
    male = 'Male'
    not_informed = 'Not Informed'


class Pet(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    weight = models.FloatField()
    sex = models.CharField(max_length=20, choices=SexOptions.choices, default=SexOptions.not_informed)