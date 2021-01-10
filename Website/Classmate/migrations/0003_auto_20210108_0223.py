# Generated by Django 3.0.8 on 2021-01-07 20:53

import datetime
from django.db import migrations, models
from django.utils.timezone import utc
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Classmate', '0002_auto_20210108_0217'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='description',
            field=models.CharField(default=datetime.datetime(2021, 1, 7, 20, 53, 36, 806753, tzinfo=utc), max_length=2000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='course',
            name='started_from',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Started from'),
            preserve_default=False,
        ),
    ]