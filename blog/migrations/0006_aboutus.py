# Generated by Django 5.1.4 on 2025-01-09 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0005_post_category"),
    ]

    operations = [
        migrations.CreateModel(
            name="AboutUs",
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
                ("content", models.TextField()),
            ],
        ),
    ]
