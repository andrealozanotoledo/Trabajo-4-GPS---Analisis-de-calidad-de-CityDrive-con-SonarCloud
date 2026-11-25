from dataclasses import dataclass
from datetime import date
from threading import Lock


@dataclass
class Reserva:
    vehiculo_id: str
    fecha_inicio: date
    fecha_fin: date
    estado: str = "activa"


_bloqueo_reservas = Lock()


def fechas_se_solapan(
    inicio_1: date,
    fin_1: date,
    inicio_2: date,
    fin_2: date,
) -> bool:
    if inicio_1 > fin_1 or inicio_2 > fin_2:
        raise ValueError("La fecha de inicio no puede ser posterior a la fecha de fin.")

    return inicio_1 <= fin_2 and inicio_2 <= fin_1


def vehiculo_disponible(
    vehiculo_id: str,
    fecha_inicio: date,
    fecha_fin: date,
    reservas: list[Reserva],
) -> bool:
    if fecha_inicio > fecha_fin:
        raise ValueError("La fecha de inicio no puede ser posterior a la fecha de fin.")

    for reserva in reservas:
        if reserva.vehiculo_id != vehiculo_id:
            continue

        if reserva.estado != "activa":
            continue

        if fechas_se_solapan(
            fecha_inicio,
            fecha_fin,
            reserva.fecha_inicio,
            reserva.fecha_fin,
        ):
            return False

    return True


def registrar_reserva_si_disponible(
    vehiculo_id: str,
    fecha_inicio: date,
    fecha_fin: date,
    reservas: list[Reserva],
) -> Reserva:
    with _bloqueo_reservas:
        if not vehiculo_disponible(
            vehiculo_id,
            fecha_inicio,
            fecha_fin,
            reservas,
        ):
            raise ValueError(
                "El vehículo ya no está disponible para las fechas indicadas."
            )

        reserva = Reserva(
            vehiculo_id=vehiculo_id,
            fecha_inicio=fecha_inicio,
            fecha_fin=fecha_fin,
        )

        reservas.append(reserva)

        return reserva