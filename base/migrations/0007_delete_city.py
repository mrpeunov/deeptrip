# Generated by Django 3.1.5 on 2021-02-18 06:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tours', '0006_auto_20210218_0936'),
        ('base', '0006_auto_20210207_0930'),
    ]

    operations = [
        migrations.DeleteModel(
            name='City',
        ),
    ]
