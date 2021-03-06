# Generated by Django 3.1.5 on 2021-04-14 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tours', '0050_auto_20210414_1002'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tour',
            name='groups',
        ),
        migrations.RemoveField(
            model_name='tour',
            name='image',
        ),
        migrations.RemoveField(
            model_name='tour',
            name='seat_request',
        ),
        migrations.AddField(
            model_name='tour',
            name='prepay',
            field=models.BooleanField(default=True, verbose_name='Есть предоплата?'),
        ),
        migrations.AddField(
            model_name='tour',
            name='prepay_percent',
            field=models.PositiveIntegerField(default=10, verbose_name='Предоплата (%)'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tour',
            name='price_for',
            field=models.CharField(default='за квадрик', max_length=20, verbose_name='За что?'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='tour',
            name='price',
            field=models.PositiveIntegerField(verbose_name='Цена (для главной)'),
        ),
        migrations.AlterField(
            model_name='tour',
            name='time',
            field=models.CharField(max_length=32, verbose_name='Продолжительность'),
        ),
    ]
