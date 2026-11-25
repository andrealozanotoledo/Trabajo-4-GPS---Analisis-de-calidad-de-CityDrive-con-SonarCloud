from dataclasses import dataclass
from datetime import date

from fechas import RangoFechas


@dataclass
class Vehiculo:
    identificador: str
    marca: str
    modelo: str
    tipo: str
    estado: str = "disponible"


@dataclass
class Reserva:
    vehiculo_id: str
    fecha_inicio: date
    fecha_fin: date
    estado: str = "activa"


def hay_solapamiento(
    inicio_1: date,
    fin_1: date,
    inicio_2: date,
    fin_2: date,
) -> bool:
    return inicio_1 <= fin_2 and inicio_2 <= fin_1


def consultar_vehiculos_disponibles(
    vehiculos: list[Vehiculo],
    reservas: list[Reserva],
    rango: RangoFechas,
) -> list[Vehiculo]:
    valido, mensaje = rango.validar()

    if not valido:
        raise ValueError(mensaje)

    disponibles = []

    for vehiculo in vehiculos:
        if vehiculo.estado != "disponible":
            continue

        ocupado = False

        for reserva in reservas:
            if reserva.vehiculo_id != vehiculo.identificador:
                continue

            if reserva.estado != "activa":
                continue

            if hay_solapamiento(
                rango.fecha_inicio,
                rango.fecha_fin,
                reserva.fecha_inicio,
                reserva.fecha_fin,
            ):
                ocupado = True
                break

        if not ocupado:
            disponibles.append(vehiculo)

    return disponibles