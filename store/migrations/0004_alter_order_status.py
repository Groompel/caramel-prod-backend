# Generated by Django 3.2.13 on 2022-05-10 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_auto_20220510_1205'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('CREATED', 'Создан'), ('IN_PROGRESS', 'В процессе'), ('READY_FOR_SHIPPING', 'Готов к доставке'), ('SHIPPING', 'Доставляется'), ('DONE', 'Завершен'), ('DECLINED', 'Отклонен')], default='CREATED', max_length=255, verbose_name='Статус'),
        ),
    ]
