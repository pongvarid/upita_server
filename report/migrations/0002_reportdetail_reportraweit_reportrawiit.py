# Generated by Django 3.1.1 on 2021-02-01 17:15

from django.db import migrations, models
import django.db.models.deletion
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('ita', '0020_reportagencyeit_other'),
        ('report', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReportRawIIT',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.CharField(max_length=255, verbose_name='ปีงบประมาณ')),
                ('raw', jsonfield.fields.JSONField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('agency', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ita.agency', verbose_name='หน่วยงาน/คณะ')),
            ],
            options={
                'verbose_name': 'รายงานรายระเอียด IIT',
                'verbose_name_plural': 'รายงานรายระเอียด IIT',
            },
        ),
        migrations.CreateModel(
            name='ReportRawEIT',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.CharField(max_length=255, verbose_name='ปีงบประมาณ')),
                ('raw', jsonfield.fields.JSONField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('agency', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ita.agency', verbose_name='หน่วยงาน/คณะ')),
            ],
            options={
                'verbose_name': 'รายงานรายระเอียด EIT',
                'verbose_name_plural': 'รายงานรายระเอียด EIT',
            },
        ),
        migrations.CreateModel(
            name='ReportDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.CharField(max_length=255, verbose_name='ปีงบประมาณ')),
                ('name', models.CharField(max_length=255, verbose_name='ปีงบประมาณ')),
                ('score', models.FloatField(default=0.0)),
                ('order', models.IntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('agency', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ita.agency', verbose_name='หน่วยงาน/คณะ')),
            ],
            options={
                'verbose_name': 'รายงานคะแนนภาพรวม',
                'verbose_name_plural': 'รายงานคะแนนภาพรวม',
            },
        ),
    ]
