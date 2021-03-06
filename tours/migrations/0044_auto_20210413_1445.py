# Generated by Django 3.1.5 on 2021-04-13 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tours', '0043_tour_transfer'),
    ]

    operations = [
        migrations.AddField(
            model_name='tour',
            name='transfer_points',
            field=models.ManyToManyField(blank=True, related_name='transfer_points', to='tours.Position', verbose_name='Точки трансфера'),
        ),
        migrations.AlterField(
            model_name='tour',
            name='positions',
            field=models.ManyToManyField(blank=True, related_name='positions', to='tours.Position', verbose_name='Местоположение экскурсии'),
        ),
        migrations.AlterField(
            model_name='tour',
            name='transfer',
            field=models.CharField(choices=[('y', 'Есть'), ('n', 'Нет'), ('yn', 'Есть + Нет')], default='yn', max_length=2, verbose_name='Трансфер'),
        ),
    ]
