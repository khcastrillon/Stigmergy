# Generated by Django 3.2.6 on 2021-10-01 05:34

from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('Orden', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='orden',
            name='estado',
            field=models.CharField(default='creado', max_length=1000),
            preserve_default=False,
        ),
    ]
