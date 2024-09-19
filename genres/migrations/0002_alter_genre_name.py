# Generated by Django 5.1.1 on 2024-09-19 13:01

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("genres", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="genre",
            name="name",
            field=models.CharField(
                choices=[
                    ("Pop", "Pop"),
                    ("Rock", "Rock"),
                    ("Jazz", "Jazz"),
                    ("Hip Hop", "Hip Hop"),
                    ("Classical", "Classical"),
                    ("Country", "Country"),
                    ("Reggae", "Reggae"),
                    ("Blues", "Blues"),
                    ("Electronic", "Electronic"),
                    ("Metal", "Metal"),
                    ("Folk", "Folk"),
                    ("R&B", "R&B"),
                    ("Latin", "Latin"),
                    ("Soul", "Soul"),
                ],
                max_length=200,
                unique=True,
                verbose_name="Name",
            ),
        ),
    ]
