# Generated by Django 3.2.8 on 2022-01-01 10:13

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='sendperson',
            field=models.CharField(default=datetime.datetime(2022, 1, 1, 10, 13, 9, 835425, tzinfo=utc), max_length=100, verbose_name='发送者'),
            preserve_default=False,
        ),
    ]