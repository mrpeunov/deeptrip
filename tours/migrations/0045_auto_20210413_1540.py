# Generated by Django 3.1.5 on 2021-04-13 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tours', '0044_auto_20210413_1445'),
    ]

    operations = [
        migrations.AddField(
            model_name='tour',
            name='transfer_no_first',
            field=models.CharField(default='хуй', max_length=64, verbose_name='1 строка (Трансфера нет или  не нужен)'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tour',
            name='transfer_no_second',
            field=models.CharField(default='хуй', max_length=64, verbose_name='2 строка (Трансфера нет или он не нужен)'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tour',
            name='transfer_yes_first',
            field=models.CharField(default='хуй', max_length=64, verbose_name='1 строка (Трансфер есть)'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tour',
            name='transfer_yes_second',
            field=models.CharField(default='хуй', max_length=64, verbose_name='2 строка (Трансфер есть)'),
            preserve_default=False,
        ),
    ]
