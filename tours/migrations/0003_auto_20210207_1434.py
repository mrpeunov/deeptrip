# Generated by Django 3.1.5 on 2021-02-07 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tours', '0002_auto_20210204_1455'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tour',
            name='description',
            field=models.TextField(verbose_name='Описание экскурсии'),
        ),
    ]
