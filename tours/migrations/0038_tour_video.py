# Generated by Django 3.1.5 on 2021-03-25 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tours', '0037_auto_20210325_1537'),
    ]

    operations = [
        migrations.AddField(
            model_name='tour',
            name='video',
            field=models.URLField(blank=True, verbose_name='Ссылка на видео'),
        ),
    ]
