# Generated by Django 3.0.6 on 2020-07-03 14:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_auto_20200703_1507'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='customer',
        ),
        migrations.RemoveField(
            model_name='order',
            name='menu',
        ),
        migrations.RemoveField(
            model_name='order',
            name='ordered_date',
        ),
    ]
