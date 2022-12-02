# Generated by Django 4.1.3 on 2022-12-02 05:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("groups", "0001_initial"),
        ("traits", "0002_trait_created_at"),
        ("pets", "0002_alter_pet_group"),
    ]

    operations = [
        migrations.AlterField(
            model_name="pet",
            name="group",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="pets",
                to="groups.group",
            ),
        ),
        migrations.AlterField(
            model_name="pet",
            name="traits",
            field=models.ManyToManyField(
                default=None, related_name="pets", to="traits.trait"
            ),
        ),
    ]
