"""Modelo de datos para el registro de reactivación de disponibilidad tras cancelación."""

from datetime import datetime

class CancelacionDisponibilidad:
    def __init__(self, id_vehiculo: str, id_reserva_cancelada: str, nuevo_estado: str = "DISPONIBLE", fecha: str = None):
        self.id_vehiculo = id_vehiculo
        self.id_reserva_cancelada = id_reserva_cancelada
        self.nuevo_estado = nuevo_estado
        self.fecha = fecha if fecha else datetime.now().isoformat()

    def to_dict(self):
        return {
            "id_vehiculo": self.id_vehiculo,
            "id_reserva_cancelada": self.id_reserva_cancelada,
            "nuevo_estado": self.nuevo_estado,
            "fecha": self.fecha
        }