# Generated by Django 3.1.5 on 2021-02-08 08:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tours', '0004_auto_20210208_1055'),
    ]

    operations = [
        migrations.AddField(
            model_name='town',
            name='image',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='town',
            name='h2',
            field=models.CharField(max_length=64, verbose_name='Заговок h2'),
        ),
    ]
