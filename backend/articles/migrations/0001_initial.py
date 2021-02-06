# Generated by Django 3.1.5 on 2021-01-10 17:11

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64, verbose_name='Название')),
                ('content', ckeditor.fields.RichTextField(verbose_name='Контент')),
                ('date', models.DateField(auto_now=True, verbose_name='Дата')),
                ('views', models.IntegerField(default=0, verbose_name='Количество просмотров')),
                ('comments', models.IntegerField(default=0, verbose_name='Количество комментов')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, verbose_name='Имя пользователя')),
                ('content', models.TextField(verbose_name='Текст комментария')),
                ('date', models.DateField(auto_now=True, verbose_name='Дата')),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='articles.article')),
            ],
        ),
    ]