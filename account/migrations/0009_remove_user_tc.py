# Generated by Django 3.2.13 on 2022-04-26 17:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0008_userrequest'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='tc',
        ),
    ]
