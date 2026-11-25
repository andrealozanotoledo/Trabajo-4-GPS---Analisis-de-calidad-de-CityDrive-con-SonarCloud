"""Modelo de datos para la entidad de reserva temporal asociada a un cliente."""

from datetime import datetime

class ReservaTemporal:
    def __init__(self, id_reserva_temp: str, id_vehiculo: str, nombre_cliente: str, email: str, telefono: str, fecha_creacion: str = None):
        self.id_reserva_temp = id_reserva_temp
        self.id_vehiculo = id_vehiculo
        self.nombre_cliente = nombre_cliente
        self.email = email
        self.telefono = telefono
        self.fecha_creacion = fecha_creacion if fecha_creacion else datetime.now().isoformat()

    def to_dict(self):
        return {
            "id_reserva_temp": self.id_reserva_temp,
            "id_vehiculo": self.id_vehiculo,
            "nombre_cliente": self.nombre_cliente,
            "email": self.email,
            "telefono": self.telefono,
            "fecha_creacion": self.fecha_creacion
        }