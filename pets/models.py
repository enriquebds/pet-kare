from django.db import models

# Create your models here.
class SexOptions(models.TextChoices):
    FEMALE = "Female"
    MALE = "Male"
    DEFAULT = "Not Informed"


class Pet(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    weight = models.FloatField()
    sex = models.CharField(
        max_length=20, choices=SexOptions.choices, default=SexOptions.DEFAULT
    )

    group = models.ForeignKey(
        "groups.Group", on_delete=models.CASCADE, related_name="groups"
    )

    traits = models.ManyToManyField("traits.Trait", related_name="traits")
