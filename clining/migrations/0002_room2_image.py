# Generated by Django 4.1.2 on 2022-11-18 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("clining", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="room2",
            name="image",
            field=models.ImageField(
                blank=True, null=True, upload_to="media/ccc", verbose_name=""
            ),
        ),
    ]
