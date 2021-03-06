# Generated by Django 3.1.1 on 2020-11-09 21:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ita', '0008_auto_20201110_0216'),
    ]

    operations = [
        migrations.AddField(
            model_name='rateresult',
            name='name',
            field=models.TextField(blank=True, null=True, verbose_name='หัวข้อ'),
        ),
        migrations.AddField(
            model_name='rateresult',
            name='ref',
            field=models.TextField(blank=True, null=True, verbose_name='หมายเหตุ'),
        ),
        migrations.AlterField(
            model_name='rate',
            name='year',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ita.year', verbose_name='ประจำปี'),
        ),
    ]
