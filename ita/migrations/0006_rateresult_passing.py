# Generated by Django 3.1.2 on 2020-10-26 05:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ita', '0005_rateresult_register_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='rateresult',
            name='passing',
            field=models.BooleanField(default=False),
        ),
    ]
