# Generated by Django 3.0.6 on 2020-07-03 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0001_initial'),
        ('order', '0003_auto_20200703_1508'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='menu',
            field=models.ManyToManyField(to='menu.DishItem'),
        ),
    ]
