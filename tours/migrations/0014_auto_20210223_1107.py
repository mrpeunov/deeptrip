# Generated by Django 3.1.5 on 2021-02-23 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tours', '0013_auto_20210223_1105'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tour',
            name='notes',
            field=models.CharField(blank=True, max_length=64, verbose_name='Примечания'),
        ),
    ]