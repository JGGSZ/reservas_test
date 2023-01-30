from django.db import models
from reservas_app.choices import estado_hab, estado_res, tipo_hab, tipo_pago 

# Create your models here.

class Habitacion(models.Model):
    estado = models.CharField(max_length=50, choices=estado_hab, null=False, blank=False)
    numero = models.CharField(max_length=20)
    tipo = models.CharField(max_length=20, choices=tipo_hab ,null=False, blank=False)
    fecha_creado = models.DateField(auto_now_add=True)
    fecha_mod = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.numero 
    
class Reserva(models.Model):
    estado = models.CharField(max_length=50, choices=estado_res, null=False, blank=False)
    cliente = models.CharField(max_length=50, null=False, blank=False)
    dni_cliente = models.CharField(max_length=50, null=False, blank=False)
    metodo_pago = models.CharField(max_length=50, choices=tipo_pago, null=False, blank=False)
    pago = models.IntegerField(null=False, blank=False)
    fecha_ingreso = models.DateField()
    fecha_salida = models.DateField()
    fecha_creado = models.DateField(auto_now_add=True)
    fecha_mod = models.DateTimeField(auto_now=True)
    estadia = models.CharField(max_length=50, null=False, blank=False)
    habitacion = models.ForeignKey(Habitacion, on_delete=models.CASCADE, related_name="habitaciones")
    
    def __str__(self):
        return str(self.habitacion.numero) + " - " + self.cliente + " - " + str(self.fecha_ingreso) + " - " + str(self.fecha_salida)
    

