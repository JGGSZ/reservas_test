# Generated by Django 4.1.5 on 2023-01-28 23:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservas_app', '0005_alter_habitacion_estado_alter_reserva_estado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reserva',
            name='estadia',
            field=models.CharField(max_length=50),
        ),
    ]
