# Generated by Django 3.2.6 on 2021-11-20 04:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Orden', '0008_orden_token'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orden',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
