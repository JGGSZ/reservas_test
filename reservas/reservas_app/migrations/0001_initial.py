# Generated by Django 4.1.5 on 2023-01-27 00:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Habitacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.CharField(choices=[('Disponible', 'Disponible'), ('Ocupada', 'Ocupada'), ('Inahabilitada', 'Inahabilitada')], default='Disponible', max_length=50)),
                ('numero', models.CharField(max_length=20)),
                ('tipo', models.CharField(choices=[('Individual', 'Individual'), ('Matrimonial', 'Matrimonial'), ('Familiar', 'Familiar')], max_length=20)),
                ('creado', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Reserva',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.CharField(choices=[('Activa', 'Activa'), ('Pendiente', 'Pendiente'), ('Completada', 'Completada'), ('Cancelada', 'Cancelada')], default='Pendiente', max_length=50)),
                ('cliente', models.CharField(max_length=50)),
                ('dni_cliente', models.CharField(max_length=50)),
                ('metodo_pago', models.CharField(max_length=50)),
                ('pago', models.IntegerField(max_length=50)),
                ('fecha_ingreso', models.DateField(auto_now_add=True)),
                ('fecha_salida', models.DateField()),
                ('fecha_mod', models.DateTimeField(auto_now=True)),
                ('estadia', models.IntegerField(max_length=1000)),
                ('habitacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='habitaciones', to='reservas_app.habitacion')),
            ],
        ),
    ]
