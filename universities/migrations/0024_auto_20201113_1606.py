# Generated by Django 3.1.2 on 2020-11-13 16:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('universities', '0023_auto_20201112_2037'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='institutions',
            options={'managed': True, 'ordering': ['maincampus']},
        ),
    ]
