# Generated by Django 3.1.1 on 2021-04-21 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0004_auto_20210322_0319'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reportraweit',
            name='raw',
        ),
        migrations.RemoveField(
            model_name='reportrawiit',
            name='raw',
        ),
        migrations.AddField(
            model_name='reportraweit',
            name='rawDone',
            field=models.TextField(blank=True, null=True, verbose_name='เนื้อหา'),
        ),
        migrations.AddField(
            model_name='reportraweit',
            name='rawType',
            field=models.TextField(blank=True, null=True, verbose_name='หัวข้อ'),
        ),
        migrations.AddField(
            model_name='reportraweit',
            name='result',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='ผลการประเมิน'),
        ),
        migrations.AddField(
            model_name='reportraweit',
            name='score',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='ผลคะแนนรวม 100 %'),
        ),
        migrations.AddField(
            model_name='reportraweit',
            name='score30',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='ผลคะแนนรวม 30 %'),
        ),
        migrations.AddField(
            model_name='reportraweit',
            name='user_do',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='บุคลากร (ที่ประเมิน)'),
        ),
        migrations.AddField(
            model_name='reportraweit',
            name='user_set',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='บุคลากร (ที่กำหนด)'),
        ),
        migrations.AddField(
            model_name='reportrawiit',
            name='rawDone',
            field=models.TextField(blank=True, null=True, verbose_name='เนื้อหา'),
        ),
        migrations.AddField(
            model_name='reportrawiit',
            name='rawType',
            field=models.TextField(blank=True, null=True, verbose_name='หัวข้อ'),
        ),
        migrations.AddField(
            model_name='reportrawiit',
            name='result',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='ผลการประเมิน'),
        ),
        migrations.AddField(
            model_name='reportrawiit',
            name='score',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='ผลคะแนนรวม 100 %'),
        ),
        migrations.AddField(
            model_name='reportrawiit',
            name='score30',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='ผลคะแนนรวม 30 %'),
        ),
        migrations.AddField(
            model_name='reportrawiit',
            name='user_do',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='บุคลากร (ที่ประเมิน)'),
        ),
        migrations.AddField(
            model_name='reportrawiit',
            name='user_set',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='บุคลากร (ที่กำหนด)'),
        ),
    ]