from rest_framework import serializers
from reservas_app.models import Habitacion, Reserva
from django.core.exceptions import ValidationError
import datetime



def validate_reservas(value):
    habitacion = value.get('habitacion')
    fecha_ingreso = value.get('fecha_ingreso')
    fecha_salida = value.get('fecha_salida')
    if fecha_ingreso >= fecha_salida:
        raise serializers.ValidationError("La fecha de ingreso debe ser anterior a la fecha de salida")
    existing_reservations = Reserva.objects.filter(habitacion=habitacion, fecha_ingreso__lte=fecha_salida, fecha_salida__gte=fecha_ingreso)
    if existing_reservations.exists():
        raise serializers.ValidationError(f'Habitacion reservada entre las fechas: {fecha_ingreso} - {fecha_salida}')
    
def validate_habitacion_numero(value):
    habitacion_numero =value.get('numero')
    existing_habitaciones = Habitacion.objects.filter(numero = habitacion_numero)
    if existing_habitaciones.exists():
        raise serializers.ValidationError("no se pueden repetir numero de habitaciones")
    
        
class HabitacionNumeroField(serializers.RelatedField):
    def to_representation(self, value):
        return value.numero + ' - ' + value.tipo 

class HabitacionSerializer(serializers.ModelSerializer):
    habitaciones = serializers.StringRelatedField(many=True) 
    class Meta:
        model = Habitacion
        fields = "__all__"
    
    def validate(self, data):
        validate_habitacion_numero(data)
        return data   
       
class ReservaSerializer(serializers.ModelSerializer):
    habitacion_dato = HabitacionNumeroField(source='habitacion', read_only=True)
    
    class Meta:
        model = Reserva
        fields = "__all__"
        read_only_fields = ('habitacion_dato', 'estadia', 'fecha_creado', 'fecha_mod')
        
    def validate(self, data):
        if self.instance is None:
            validate_reservas(data)
        else:
            existing_reservations = Reserva.objects.filter(habitacion=data['habitacion'], fecha_ingreso__lte=data['fecha_salida'], fecha_salida__gte=data['fecha_ingreso'])
            existing_reservations = existing_reservations.exclude(pk=self.instance.pk)
            if existing_reservations.exists():
                raise serializers.ValidationError(f'Habitacion reservada entre las fechas: {data["fecha_ingreso"]} - {data["fecha_salida"]}')
        return data
    
    def create(self, validated_data):
        
        fecha_ingreso = validated_data['fecha_ingreso']
        fecha_salida = validated_data['fecha_salida']
        estadia = (fecha_salida - fecha_ingreso).days
        validated_data['estadia'] = estadia
        return super().create(validated_data)
    
    def update(self, instance, validated_data):
        fecha_ingreso = validated_data.get('fecha_ingreso', instance.fecha_ingreso)
        fecha_salida = validated_data.get('fecha_salida', instance.fecha_salida)
        estadia = (fecha_salida - fecha_ingreso).days
        validated_data['estadia'] = estadia
        return super().update(instance, validated_data)