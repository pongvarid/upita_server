# Generated by Django 3.1.1 on 2022-01-19 19:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eit', '0003_auto_20201125_0147'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issue',
            name='name',
            field=models.TextField(),
        ),
    ]
