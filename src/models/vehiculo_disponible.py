"""Modelo de datos para la representación del vehículo en el catálogo y su estado operativo."""

from typing import Dict, Any

class VehiculoDisponible:
    def __init__(
        self,
        id_vehiculo: str,
        marca: str,
        modelo: str,
        tipo: str,
        precio_por_dia: float,
        estado_operativo: str = "DISPONIBLE",
        matricula: str = "",
        capacidad_pasajeros: int = 5
    ):
        self.id_vehiculo = id_vehiculo
        self.marca = marca
        self.modelo = modelo
        self.tipo = tipo
        self.precio_por_dia = precio_por_dia
        self.estado_operativo = estado_operativo
        self.matricula = matricula
        self.capacidad_pasajeros = capacidad_pasajeros

    def to_dict(self) -> Dict[str, Any]:
        return {
            "id_vehiculo": self.id_vehiculo,
            "marca": self.marca,
            "modelo": self.modelo,
            "tipo": self.tipo,
            "precio_por_dia": self.precio_por_dia,
            "estado_operativo": self.estado_operativo,
            "matricula": self.matricula,
            "capacidad_pasajeros": self.capacidad_pasajeros
        }