# Generated by Django 3.2.13 on 2022-05-16 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_alter_order_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('CREATED', 'Создан'), ('IN_PROGRESS', 'В процессе'), ('READY_FOR_SHIPPING', 'Готов к доставке'), ('SHIPPING', 'Доставляется'), ('DONE', 'Завершен'), ('DECLINED', 'Отклонен'), ('IN_QUEUE', 'В очереди на выполнение')], default='CREATED', max_length=255, verbose_name='Статус'),
        ),
    ]
