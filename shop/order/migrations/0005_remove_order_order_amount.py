# Generated by Django 3.0.5 on 2020-04-27 09:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0004_order_order_amount'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='order_amount',
        ),
    ]
