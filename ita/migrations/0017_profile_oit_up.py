# Generated by Django 3.1.1 on 2021-01-08 00:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ita', '0016_urlinrate'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='oit_up',
            field=models.BooleanField(default=False, verbose_name='สามารถประเมิน OIT มหาวิทยาลัยพะเยา ได้'),
        ),
    ]
