# Generated by Django 3.1.1 on 2022-12-27 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ita', '0029_auto_20220821_0225'),
    ]

    operations = [
        migrations.AddField(
            model_name='rate',
            name='type_sub',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='ประเภทย่อย'),
        ),
    ]
