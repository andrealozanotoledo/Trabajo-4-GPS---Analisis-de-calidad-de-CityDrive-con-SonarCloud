"""Modelo para la entidad de bloqueo y estado de disponibilidad del vehículo por rango temporal."""

from datetime import datetime

class BloqueoVehiculo:
    def __init__(self, id_vehiculo: str, id_reserva: str, fecha_inicio: str, fecha_fin: str, estado_disponibilidad: str = "BLOQUEADO"):
        self.id_vehiculo = id_vehiculo
        self.id_reserva = id_reserva
        self.fecha_inicio = fecha_inicio
        self.fecha_fin = fecha_fin
        self.estado_disponibilidad = estado_disponibilidad

    def to_dict(self):
        return {
            "id_vehiculo": self.id_vehiculo,
            "id_reserva": self.id_reserva,
            "fecha_inicio": self.fecha_inicio,
            "fecha_fin": self.fecha_fin,
            "estado_disponibilidad": self.estado_disponibilidad
        }