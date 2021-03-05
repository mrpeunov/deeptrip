# Generated by Django 3.1.5 on 2021-03-05 06:33

import ckeditor.fields
import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tours', '0018_remove_category_city'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tour',
            name='include',
        ),
        migrations.AddField(
            model_name='tour',
            name='add_price',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=10), blank=True, default="{'hm', 'rr'}", size=4),
        ),
        migrations.AlterField(
            model_name='tour',
            name='description',
            field=ckeditor.fields.RichTextField(verbose_name='Описание экскурсии'),
        ),
    ]
