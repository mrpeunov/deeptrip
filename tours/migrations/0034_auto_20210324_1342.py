# Generated by Django 3.1.5 on 2021-03-24 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tours', '0033_auto_20210311_1156'),
    ]

    operations = [
        migrations.AddField(
            model_name='tour',
            name='auto_gid',
            field=models.BooleanField(default=True, verbose_name='Автоматизировать провернный гид'),
        ),
        migrations.AddField(
            model_name='tour',
            name='gid',
            field=models.BooleanField(default=False, verbose_name='Проверенный гид'),
        ),
    ]
