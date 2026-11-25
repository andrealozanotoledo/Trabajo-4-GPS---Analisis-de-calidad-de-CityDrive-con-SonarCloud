"""Modelo de datos para la representación de una reserva en consulta administrativa."""

from datetime import datetime
from typing import Dict, Any

class ReservaActiva:
    def __init__(
        self,
        id_reserva: str,
        id_vehiculo: str,
        cliente: str,
        fecha_inicio: str,
        fecha_fin: str,
        estado: str = "CONFIRMADA"
    ):
        self.id_reserva = id_reserva
        self.id_vehiculo = id_vehiculo
        self.cliente = cliente
        self.fecha_inicio = fecha_inicio
        self.fecha_fin = fecha_fin
        self.estado = estado.upper()

    def to_dict(self) -> Dict[str, Any]:
        return {
            "id_reserva": self.id_reserva,
            "id_vehiculo": self.id_vehiculo,
            "cliente": self.cliente,
            "fecha_inicio": self.fecha_inicio,
            "fecha_fin": self.fecha_fin,
            "estado": self.estado
        }