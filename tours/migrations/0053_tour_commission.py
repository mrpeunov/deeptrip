# Generated by Django 3.1.5 on 2021-04-15 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tours', '0052_auto_20210415_0919'),
    ]

    operations = [
        migrations.AddField(
            model_name='tour',
            name='commission',
            field=models.IntegerField(default=10, verbose_name='Коммиссия (%)'),
            preserve_default=False,
        ),
    ]
