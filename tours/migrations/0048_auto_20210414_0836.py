# Generated by Django 3.1.5 on 2021-04-14 05:36

from django.db import migrations, models
import django.db.models.deletion
import django_better_admin_arrayfield.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('tours', '0047_tour_period'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='period',
            options={'verbose_name': 'период работы', 'verbose_name_plural': 'периоды работы'},
        ),
        migrations.AlterField(
            model_name='tour',
            name='period',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='tours.period', verbose_name='Период года'),
        ),
        migrations.AlterField(
            model_name='tour',
            name='start_list',
            field=django_better_admin_arrayfield.models.fields.ArrayField(base_field=models.TimeField(), blank=True, null=True, size=4, verbose_name='Начало'),
        ),
    ]
