# Generated by Django 3.1.2 on 2020-11-01 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_auto_20201101_1203'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='pic',
            field=models.ImageField(default='download.jpeg', upload_to=''),
        ),
    ]