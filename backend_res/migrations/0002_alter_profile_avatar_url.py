# Generated by Django 3.2.8 on 2021-10-31 04:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend_res', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='avatar_url',
            field=models.TextField(default='https://source.unsplash.com/collection/1346951/50x50?sig=1', max_length=255),
        ),
    ]
