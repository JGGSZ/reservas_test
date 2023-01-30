from rest_framework.response import Response
from reservas_app.models import Habitacion, Reserva
from reservas_app.api.serializers import HabitacionSerializer, ReservaSerializer
from rest_framework import status
from rest_framework.views import APIView
import datetime


    
class HabDisponiblesAv(APIView):
    def get(self, request):
        fecha_ingreso = request.GET.get('fecha_ingreso')
        fecha_salida = request.GET.get('fecha_salida')
        reserved_rooms = Reserva.objects.filter(fecha_ingreso__gte=fecha_ingreso, fecha_salida__lte=fecha_salida)
        room_ids = [room.habitacion.id for room in reserved_rooms]
        available_rooms = Habitacion.objects.exclude(id__in=room_ids)
        serializer = HabitacionSerializer(available_rooms, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = ReservaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class HabitacionAv(APIView):
    def get(self, request):
        habitacion = Habitacion.objects.all()
        serializer = HabitacionSerializer(habitacion, many=True, context ={'request': request})
        return Response(serializer.data)
    
    def post(self, request):
        serializer = HabitacionSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        
class HabitacionDetalleAV(APIView):
    def get(self, request, pk):
        try:
            habitacion = Habitacion.objects.get(pk=pk)
        except Habitacion.DoesNotExist:
            return Response({'error': 'habitacion no encontrada'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = HabitacionSerializer(habitacion, context={'request': request})
        return Response(serializer.data)
    
    def put(self, request, pk):
        try:
            habitacion = Habitacion.objects.get(pk=pk)
        except Habitacion.DoesNotExist:
            return Response({'error': 'habitacion no encontrada'}, status=status.HTTP_404_NOT_FOUND)
        serializer = HabitacionSerializer(habitacion, data=request.data, context={'request':request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, pk):
        try:
            habitacion = Habitacion.objects.get(pk=pk)
        except Habitacion.DoesNotExist:
            return Response({'error': 'habitacion no encontrada'}, status=status.HTTP_404_NOT_FOUND)
        serializer = HabitacionSerializer(habitacion, data=request.data, context={'request':request})
        
        habitacion.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
        
    

class ReservaAV(APIView):
    
    def get(self, request):
        reserva = Reserva.objects.all()
        serializer = ReservaSerializer(reserva, many = True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = ReservaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
                
        
class ReservaDetalleAV(APIView):
    
    def get(self, request, pk ): 
        try:
            reserva = Reserva.objects.get(pk=pk)
        except Reserva.DoesNotExist:
            return Response({'error': 'reserva no encontrada'},status=status.HTTP_404_NOT_FOUND)
        
        serializer = ReservaSerializer(reserva) 
        return Response(serializer.data)
    
    def put(self, request, pk):
        try:
            reserva = Reserva.objects.get(pk=pk)
        except Reserva.DoesNotExist:
            return Response({'error': 'reserva no encontrada'},status=status.HTTP_404_NOT_FOUND)
        
        serializer = ReservaSerializer(reserva, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            reserva = Reserva.objects.get(pk=pk)
        except Reserva.DoesNotExist:
            return Response({'error': 'reserva no encontrada'},status=status.HTTP_404_NOT_FOUND)
        
        reserva.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    