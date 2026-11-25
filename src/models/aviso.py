"""Modelo de datos para avisos y notificaciones de disponibilidad."""

from datetime import datetime

class AvisoDisponibilidad:
    def __init__(self, id_aviso: str, id_vehiculo: str, id_cliente: str, mensaje: str, fecha: str = None):
        self.id_aviso = id_aviso
        self.id_vehiculo = id_vehiculo
        self.id_cliente = id_cliente
        self.mensaje = mensaje
        self.fecha = fecha if fecha else datetime.now().isoformat()

    def to_dict(self):
        return {
            "id_aviso": self.id_aviso,
            "id_vehiculo": self.id_vehiculo,
            "id_cliente": self.id_cliente,
            "mensaje": self.mensaje,
            "fecha": self.fecha
        }