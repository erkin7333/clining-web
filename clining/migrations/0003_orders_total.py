# Generated by Django 4.1.2 on 2022-11-12 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("clining", "0002_contactform_description"),
    ]

    operations = [
        migrations.AddField(
            model_name="orders",
            name="total",
            field=models.PositiveIntegerField(default=0, verbose_name="total"),
            preserve_default=False,
        ),
    ]
