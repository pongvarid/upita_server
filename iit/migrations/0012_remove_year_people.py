# Generated by Django 3.1.1 on 2020-11-29 13:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('iit', '0011_auto_20201129_2018'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='year',
            name='people',
        ),
    ]
