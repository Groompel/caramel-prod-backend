# Generated by Django 3.2.13 on 2022-05-16 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boiler', '0002_alter_boiler_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='boiler',
            name='ending_time_of_iteration',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Конечное время выполнения нышней партии'),
        ),
        migrations.AlterField(
            model_name='boiler',
            name='engine_target_voltage',
            field=models.FloatField(blank=True, null=True, verbose_name='SP'),
        ),
        migrations.AlterField(
            model_name='boiler',
            name='engine_voltage',
            field=models.FloatField(blank=True, null=True, verbose_name='PV'),
        ),
        migrations.AlterField(
            model_name='boiler',
            name='error_prev',
            field=models.FloatField(blank=True, null=True, verbose_name='Предыдущая ошибка'),
        ),
        migrations.AlterField(
            model_name='boiler',
            name='initial_order_volume',
            field=models.FloatField(blank=True, null=True, verbose_name='Общий объем заказа'),
        ),
        migrations.AlterField(
            model_name='boiler',
            name='made_volume',
            field=models.FloatField(blank=True, null=True, verbose_name='Проделанный объем заказа'),
        ),
    ]
