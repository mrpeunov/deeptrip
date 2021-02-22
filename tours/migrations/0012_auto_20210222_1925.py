# Generated by Django 3.1.5 on 2021-02-22 16:25

from django.db import migrations, models
import django.db.models.deletion
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        ('tours', '0011_auto_20210222_1904'),
    ]

    operations = [
        migrations.AddField(
            model_name='tour',
            name='cluster',
            field=models.ForeignKey(blank=True, default='1', on_delete=django.db.models.deletion.PROTECT, to='tours.cluster'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='tour',
            name='cities',
            field=smart_selects.db_fields.ChainedManyToManyField(chained_field='cluster', chained_model_field='cluster', horizontal=True, related_name='add_cities', to='tours.City', verbose_name='Дополнительные'),
        ),
        migrations.AlterField(
            model_name='tour',
            name='city',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, related_name='main_city', to='tours.city'),
        ),
    ]
