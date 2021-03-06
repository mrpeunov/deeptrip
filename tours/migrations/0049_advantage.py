# Generated by Django 3.1.5 on 2021-04-14 06:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tours', '0048_auto_20210414_0836'),
    ]

    operations = [
        migrations.CreateModel(
            name='Advantage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('children', 'Дети'), ('time', 'Время'), ('transfer', 'Трансфер'), ('group', 'Группа'), ('prepay', 'Предоплата')], max_length=10, verbose_name='Тип')),
                ('title', models.CharField(blank=True, default='Без предоплаты', max_length=32, verbose_name='Заголовок')),
                ('description', models.CharField(blank=True, default='Бронируйте экскурсию без предоплаты', max_length=64, verbose_name='Описание')),
                ('tour', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='tours.tour', verbose_name='Экскурсия')),
            ],
        ),
    ]
