# Generated by Django 3.1.1 on 2021-04-08 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ita', '0024_auto_20210322_0319'),
    ]

    operations = [
        migrations.AddField(
            model_name='rate',
            name='type_base',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='ประเภทตัวชี้วัด'),
        ),
    ]