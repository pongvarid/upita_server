# Generated by Django 3.1.1 on 2020-11-22 07:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('iit', '0005_auto_20201122_0833'),
    ]

    operations = [
        migrations.AddField(
            model_name='assessmentissues',
            name='order',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='assessmentissues',
            name='year',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='iit.year', verbose_name='ปีงบประมาณ'),
        ),
    ]
