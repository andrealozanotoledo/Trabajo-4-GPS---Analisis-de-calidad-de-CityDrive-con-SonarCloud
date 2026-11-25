"""Modelo de datos para la entidad Vehículo con atributo de tipo para filtrado."""

class VehiculoFiltro:
    def __init__(self, id_vehiculo: str, marca: str, modelo: str, tipo: str, disponible: bool = True):
        self.id_vehiculo = id_vehiculo
        self.marca = marca
        self.modelo = modelo
        self.tipo = tipo  # 'COCHE' o 'FURGONETA'
        self.disponible = disponible

    def to_dict(self):
        return {
            "id_vehiculo": self.id_vehiculo,
            "marca": self.marca,
            "modelo": self.modelo,
            "tipo": self.tipo,
            "disponible": self.disponible
        }