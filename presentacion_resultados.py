
from dataclasses import dataclass


@dataclass
class VehiculoResultado:
    identificador: str
    marca: str
    modelo: str
    tipo: str


def presentar_resultados(vehiculos):
    if not vehiculos:
        return "No existen vehículos disponibles para las fechas seleccionadas."

    lineas = ["Vehículos disponibles:"]

    for vehiculo in vehiculos:
        lineas.append(
            f"{vehiculo.marca} {vehiculo.modelo} "
            f"({vehiculo.tipo}) - ID: {vehiculo.identificador}"
        )

    return "\n".join(lineas)
