# Generated by Django 4.2.3 on 2023-10-09 16:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='created',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 10, 9, 22, 23, 0, 613656)),
        ),
    ]
