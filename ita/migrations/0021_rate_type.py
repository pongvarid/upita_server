# Generated by Django 3.1.1 on 2021-02-06 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ita', '0020_reportagencyeit_other'),
    ]

    operations = [
        migrations.AddField(
            model_name='rate',
            name='type',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='ประเภท'),
        ),
    ]
