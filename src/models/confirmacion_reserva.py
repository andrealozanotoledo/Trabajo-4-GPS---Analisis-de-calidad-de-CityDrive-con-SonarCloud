"""Modelo de datos para el registro definitivo y confirmación de la reserva."""

from datetime import datetime

class ConfirmacionReserva:
    def __init__(self, id_confirmacion: str, id_reserva: str, id_vehiculo: str, id_cliente: str, importe_total: float, fecha_inicio: str, fecha_fin: str, fecha_registro: str = None):
        self.id_confirmacion = id_confirmacion
        self.id_reserva = id_reserva
        self.id_vehiculo = id_vehiculo
        self.id_cliente = id_cliente
        self.importe_total = importe_total
        self.fecha_inicio = fecha_inicio
        self.fecha_fin = fecha_fin
        self.fecha_registro = fecha_registro if fecha_registro else datetime.now().isoformat()

    def to_dict(self):
        return {
            "id_confirmacion": self.id_confirmacion,
            "id_reserva": self.id_reserva,
            "id_vehiculo": self.id_vehiculo,
            "id_cliente": self.id_cliente,
            "importe_total": self.importe_total,
            "fecha_inicio": self.fecha_inicio,
            "fecha_fin": self.fecha_fin,
            "fecha_registro": self.fecha_registro
        }