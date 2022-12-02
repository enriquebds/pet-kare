# Generated by Django 4.1.3 on 2022-12-02 13:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("pets", "0004_remove_pet_group_remove_pet_traits"),
        ("groups", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="group",
            name="pet",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="groups",
                to="pets.pet",
            ),
        ),
    ]