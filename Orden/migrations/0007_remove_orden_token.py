# Generated by Django 2.2 on 2021-11-11 19:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Orden', '0006_auto_20211111_1145'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orden',
            name='token',
        ),
    ]
