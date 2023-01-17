# Generated by Django 4.1.5 on 2023-01-15 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Sports",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                ("description", models.CharField(max_length=200)),
                ("num_of_players", models.IntegerField()),
                (
                    "sport_type",
                    models.CharField(
                        choices=[("Indoor", "indoor"), ("Outdoor", "outdoor")],
                        max_length=10,
                    ),
                ),
            ],
        ),
    ]
