from dataclasses import dataclass


@dataclass
class VehiculoDetalle:
    identificador: str
    marca: str
    modelo: str
    categoria: str
    plazas: int
    capacidad_maletero: str
    transmision: str
    estado_operativo: str


def mostrar_detalle_vehiculo(vehiculo):
    return (
        "CARACTERÍSTICAS DEL VEHÍCULO\n"
        f"Identificador: {vehiculo.identificador}\n"
        f"Marca: {vehiculo.marca}\n"
        f"Modelo: {vehiculo.modelo}\n"
        f"Categoría: {vehiculo.categoria}\n"
        f"Plazas: {vehiculo.plazas}\n"
        f"Capacidad de maletero/carga: {vehiculo.capacidad_maletero}\n"
        f"Transmisión: {vehiculo.transmision}\n"
        f"Estado operativo: {vehiculo.estado_operativo}"
    )