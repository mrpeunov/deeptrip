# Generated by Django 3.1.5 on 2021-01-11 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tours', '0004_auto_20210111_1426'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imageitem',
            name='description',
            field=models.CharField(max_length=128, verbose_name='Описание фотографии'),
        ),
    ]
