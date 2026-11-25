from dataclasses import dataclass

from disponibilidad import (
    Vehiculo,
    Reserva,
    consultar_vehiculos_disponibles,
)
from fechas import RangoFechas


@dataclass
class SeleccionReserva:
    vehiculo_id: str
    rango_fechas: RangoFechas


def seleccionar_vehiculo(
    vehiculo: Vehiculo,
    reservas: list[Reserva],
    rango: RangoFechas,
) -> SeleccionReserva:
    disponibles = consultar_vehiculos_disponibles(
        [vehiculo],
        reservas,
        rango,
    )

    if not disponibles:
        raise ValueError(
            "El vehículo seleccionado no está disponible para las fechas indicadas."
        )

    return SeleccionReserva(
        vehiculo_id=vehiculo.identificador,
        rango_fechas=rango,
    )