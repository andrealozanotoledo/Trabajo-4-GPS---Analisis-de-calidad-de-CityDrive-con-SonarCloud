from dataclasses import dataclass


@dataclass
class Reserva:
    referencia: str
    estado: str = "activa"


def cancelar_reserva(reserva: Reserva) -> Reserva:
    if not reserva.referencia or not reserva.referencia.strip():
        raise ValueError("La referencia de la reserva no es válida.")

    if reserva.estado != "activa":
        raise ValueError("Solo se puede cancelar una reserva activa.")

    reserva.estado = "cancelada"
    return reserva