# Generated by Django 3.2.6 on 2021-11-11 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Orden', '0004_orden_valor'),
    ]

    operations = [
        migrations.AddField(
            model_name='orden',
            name='token',
            field=models.CharField(default=1, max_length=60),
            preserve_default=False,
        ),
    ]
