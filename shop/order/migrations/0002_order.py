# Generated by Django 3.0.5 on 2020-04-27 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_user', models.DecimalField(decimal_places=0, max_digits=10)),
                ('order_total', models.DecimalField(decimal_places=0, max_digits=6)),
            ],
        ),
    ]
