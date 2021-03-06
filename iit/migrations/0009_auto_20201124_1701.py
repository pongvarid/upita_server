# Generated by Django 3.1.1 on 2020-11-24 10:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('iit', '0008_answersuggestion'),
    ]

    operations = [
        migrations.AddField(
            model_name='answerissue',
            name='value_by',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='answerissue',
            name='value_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='iit.choice'),
        ),
        migrations.AlterField(
            model_name='answerissue',
            name='value',
            field=models.FloatField(blank=True, default=0.0, null=True, verbose_name='คะแนน'),
        ),
    ]
