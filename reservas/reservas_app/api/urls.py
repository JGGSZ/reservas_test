from django.urls import path
# from inmuebleslist_app.api.views import inmueble_list, inmueble_detalle
from reservas_app.api.views import HabitacionAv, HabitacionDetalleAV, ReservaAV, ReservaDetalleAV, HabDisponiblesAv


urlpatterns = [
    path('habitacion/', HabitacionAv.as_view(), name='habitaciones'),
    path('habitacion/<int:pk>', HabitacionDetalleAV.as_view(), name='habitacion-detail'),
    path('reservas/', ReservaAV.as_view(), name='reservas'),
    path('reservas/<int:pk>', ReservaDetalleAV.as_view(), name='reservas-detail'),
    path('habitaciones_disponibles/', HabDisponiblesAv.as_view(), name='habitaciones_disponibles'),

    
]