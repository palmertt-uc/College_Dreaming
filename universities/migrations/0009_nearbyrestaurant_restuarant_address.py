# Generated by Django 3.1 on 2020-09-13 23:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('universities', '0008_auto_20200910_0200'),
    ]

    operations = [
        migrations.AddField(
            model_name='nearbyrestaurant',
            name='restuarant_address',
            field=models.CharField(default='123 Address, St, Cincinnati, OH 45209', max_length=200),
        ),
    ]
