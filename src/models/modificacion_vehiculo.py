"""Modelo de datos para la entidad de vehículo editado y auditoría de cambios administrativos."""

from datetime import datetime
from typing import Dict, Any, Optional

class ModificacionVehiculo:
    def __init__(
        self,
        id_vehiculo: str,
        marca: str,
        modelo: str,
        tipo: str,
        precio_por_dia: float,
        estado: str = "DISPONIBLE",
        fecha_actualizacion: Optional[str] = None
    ):
        self.id_vehiculo = id_vehiculo
        self.marca = marca
        self.modelo = modelo
        self.tipo = tipo
        self.precio_por_dia = precio_por_dia
        self.estado = estado
        self.fecha_actualizacion = fecha_actualizacion if fecha_actualizacion else datetime.now().isoformat()

    def to_dict(self) -> Dict[str, Any]:
        return {
            "id_vehiculo": self.id_vehiculo,
            "marca": self.marca,
            "modelo": self.modelo,
            "tipo": self.tipo,
            "precio_por_dia": self.precio_por_dia,
            "estado": self.estado,
            "fecha_actualizacion": self.fecha_actualizacion
        }