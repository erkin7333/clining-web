# Generated by Django 4.1.3 on 2022-11-10 05:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clining', '0003_remove_orders_price_remove_orders_roomcategory_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orders',
            name='priceroom',
        ),
        migrations.RemoveField(
            model_name='orders',
            name='priceservice',
        ),
    ]
