# Generated by Django 3.1.7 on 2021-03-11 20:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nitc', '0005_auto_20210309_1535'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='register',
            name='course_days',
        ),
        migrations.RemoveField(
            model_name='register',
            name='course_time_type',
        ),
        migrations.AddField(
            model_name='register',
            name='startdate',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2021, 3, 11, 20, 23, 11, 336521)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='register',
            name='surname',
            field=models.CharField(default=datetime.datetime(2021, 3, 11, 20, 23, 43, 271409), max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='register',
            name='number_group',
            field=models.CharField(max_length=50),
        ),
    ]
