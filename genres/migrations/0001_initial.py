# Generated by Django 5.1.1 on 2024-09-19 00:46

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Genre",
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
                (
                    "name",
                    models.CharField(
                        choices=[
                            ("Action", "Action"),
                            ("Adventure", "Adventure"),
                            ("Comedy", "Comedy"),
                            ("Drama", "Drama"),
                            ("Horror", "Horror"),
                            ("Science Fiction", "Science Fiction"),
                            ("Fantasy", "Fantasy"),
                            ("Romance", "Romance"),
                            ("Mystery", "Mystery"),
                            ("Thriller", "Thriller"),
                            ("Animation", "Animation"),
                            ("Documentary", "Documentary"),
                            ("Musical", "Musical"),
                            ("Historical", "Historical"),
                            ("Family", "Family"),
                        ],
                        max_length=200,
                        unique=True,
                        verbose_name="Name",
                    ),
                ),
            ],
        ),
    ]
