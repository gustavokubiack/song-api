# Generated by Django 5.1.1 on 2024-09-22 21:42

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("genres", "0002_alter_genre_name"),
    ]

    operations = [
        migrations.AlterField(
            model_name="genre",
            name="name",
            field=models.CharField(max_length=200, verbose_name="Name"),
        ),
    ]
