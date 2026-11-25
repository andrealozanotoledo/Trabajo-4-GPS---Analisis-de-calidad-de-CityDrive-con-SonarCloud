from disponibilidad import Vehiculo, Reserva, hay_solapamiento
from fechas import RangoFechas


def comprobar_disponibilidad_vehiculo(
    vehiculo: Vehiculo,
    reservas: list[Reserva],
    rango: RangoFechas,
) -> bool:
    valido, mensaje = rango.validar()

    if not valido:
        raise ValueError(mensaje)

    if vehiculo.estado != "disponible":
        return False

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
            return False

    return True