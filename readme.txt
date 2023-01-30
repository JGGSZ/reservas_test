Este es el código para un sistema de gestión de reservas de habitaciones en un hotel. Este código utiliza el framework Django y la biblioteca de Django Rest Framework para crear una API REST.

en models.py podemos encontrar:

La clase Habitación tiene los siguientes campos:

estado: un campo de tipo CharField que contiene el estado de la habitación (disponible, ocupada, etc.)
numero: un campo de tipo CharField que contiene el número de la habitación
tipo: un campo de tipo CharField que contiene el tipo de habitación (sencilla, doble, etc.)
fecha_creado: un campo de tipo DateField que contiene la fecha en la que se creó la habitación
fecha_mod: un campo de tipo DateTimeField que contiene la fecha en la que se modificó la habitación
La clase tiene un método str que devuelve el número de la habitación.


- La clase Reserva tiene los siguientes campos:

estado: un campo de tipo CharField que contiene el estado de la reserva (confirmada, cancelada, etc.)
cliente: un campo de tipo CharField que contiene el nombre del cliente
dni_cliente: un campo de tipo CharField que contiene el DNI del cliente
metodo_pago: un campo de tipo CharField que contiene el método de pago de la reserva (efectivo, tarjeta, etc.)
pago: un campo de tipo IntegerField que contiene el pago de la reserva
fecha_ingreso: un campo de tipo DateField que contiene la fecha de ingreso de la reserva
fecha_salida: un campo de tipo DateField que contiene la fecha de salida de la reserva
fecha_creado: un campo de tipo DateField que contiene la fecha en la que se creó la reserva
fecha_mod: un campo de tipo DateTimeField que contiene la fecha en la que se modificó la reserva
estadia: un campo de tipo CharField que contiene la estadía de la reserva
habitacion: un campo de tipo ForeignKey que contiene la habitación relacionada con la reserva
La clase tiene un método str que devuelve el número de la habitación, el nombre del cliente y las fechas de ingreso y salida.

También hay dos funciones de validación, una para validar las reservas y otra para validar el número de habitación.

- en serializers.py podemos encontrar: 

Funciones
validate_reservas: esta función valida si una reserva es válida o no, verificando si la fecha de ingreso es anterior a la fecha de salida y si la habitación está disponible en esas fechas.

validate_habitacion_numero: esta función valida si el número de habitación es único.

HabitacionNumeroField: esta clase hereda de serializers.RelatedField y define la representación de una habitación como su número y tipo.

Clases serializadoras
HabitacionSerializer: esta clase serializa los datos de una habitación y valida el número de habitación con la función validate_habitacion_numero.

ReservaSerializer: esta clase serializa los datos de una reserva, valida la reserva con la función validate_reservas y también calcula la estadía de la reserva. Además, proporciona una representación legible para el usuario de la habitación relacionada a la reserva.

- en views.py podemos encontrar:

HabDisponiblesAv: Esta clase maneja la búsqueda de habitaciones disponibles para reservar. Además, también permite realizar reservas a través de una petición POST.

HabitacionAv: Esta clase maneja las operaciones CRUD (Crear, Leer, Actualizar, Borrar) para las habitaciones en el hotel.

HabitacionDetalleAv: Esta clase maneja operaciones específicas para una habitación en particular.

ReservaAV: Esta clase maneja las operaciones CRUD para las reservas realizadas en el hotel.

ReservaDetalleAv: Esta clase maneja operaciones específicas para una reserva en particular.

- urls.py y endpoints:

path('habitacion/', HabitacionAv.as_view(), name='habitaciones'): Este patrón de URL se encarga de manejar la vista de habitaciones, enlazada con la clase HabitacionAv 

path('habitacion/<int:pk>', HabitacionDetalleAV.as_view(), name='habitacion-detail'): Este patrón de URL se encarga de manejar la vista de detalle de habitación, enlazada con la clase HabitacionDetalleAV 

path('reservas/', ReservaAV.as_view(), name='reservas'): Este patrón de URL se encarga de manejar la vista de reservas, enlazada con la clase ReservaAV 

path('reservas/<int:pk>', ReservaDetalleAV.as_view(), name='reservas-detail'): Este patrón de URL se encarga de manejar la vista de detalle de reserva, enlazada con la clase ReservaDetalleAV 

path('habitaciones_disponibles/', HabDisponiblesAv.as_view(), name='habitaciones_disponibles'): Este patrón de URL se encarga de manejar la vista de habitaciones disponibles y da la posibilidad de agregar una reserva, enlazada con la clase HabDisponiblesAv 




