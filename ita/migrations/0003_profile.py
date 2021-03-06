# Generated by Django 3.1.2 on 2020-10-26 02:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ita', '0002_auto_20201025_2257'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('register_type', models.CharField(choices=[('office365', 'office365'), ('ปกติ', 'ปกติ')], max_length=255)),
                ('status', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('agency', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ita.agency')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'ผู้ใช้',
                'verbose_name_plural': 'ผู้ใช้',
            },
        ),
    ]
