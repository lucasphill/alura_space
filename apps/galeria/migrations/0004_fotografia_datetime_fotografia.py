# Generated by Django 5.1 on 2024-08-30 00:01

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('galeria', '0003_fotografia_publicada'),
    ]

    operations = [
        migrations.AddField(
            model_name='fotografia',
            name='datetime_fotografia',
            field=models.DateTimeField(default=datetime.datetime(2024, 8, 29, 21, 1, 5, 13873)),
        ),
    ]
