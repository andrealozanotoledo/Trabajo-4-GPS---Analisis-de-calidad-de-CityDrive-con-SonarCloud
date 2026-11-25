"""Servicio para gestionar el bloqueo temporal de vehículos y verificar colisiones de fechas."""

from datetime import datetime
from typing import Dict, Any, List

from src.models.bloqueo_vehiculo import BloqueoVehiculo
from src.services.confirmacion_service import obtener_reservas_confirmadas


# Catálogo base de vehículos
_CATALOGO_ESTADOS = {
    "VEH-01": "DISPONIBLE",
    "VEH-02": "DISPONIBLE",
    "VEH-03": "MANTENIMIENTO",
    "VEH-101": "DISPONIBLE",
    "VEH-102": "NO DISPONIBLE",
    "VEH-104": "DISPONIBLE",
}


# Bloqueos activos indexados por vehículo
_HISTORIAL_BLOQUEOS: List[BloqueoVehiculo] = []


def _fechas_se_solapan(
    inicio_a: str,
    fin_a: str,
    inicio_b: str,
    fin_b: str,
) -> bool:
    """Comprueba si dos intervalos temporales se solapan."""

    fmt = "%Y-%m-%d"

    ini_a = datetime.strptime(inicio_a, fmt)
    fin_a_dt = datetime.strptime(fin_a, fmt)
    ini_b = datetime.strptime(inicio_b, fmt)
    fin_b_dt = datetime.strptime(fin_b, fmt)

    return max(ini_a, ini_b) <= min(fin_a_dt, fin_b_dt)


def esta_vehiculo_disponible_en_fechas(
    id_vehiculo: str,
    fecha_inicio: str,
    fecha_fin: str,
) -> bool:
    """Verifica si el vehículo está libre en el intervalo dado."""

    id_vehiculo_norm = id_vehiculo.strip().upper()

    if _CATALOGO_ESTADOS.get(id_vehiculo_norm) != "DISPONIBLE":
        return False

    for bloqueo in _HISTORIAL_BLOQUEOS:

        if bloqueo.id_vehiculo != id_vehiculo_norm:
            continue

        if _fechas_se_solapan(
            bloqueo.fecha_inicio,
            bloqueo.fecha_fin,
            fecha_inicio,
            fecha_fin,
        ):
            return False

    return True


def bloquear_vehiculo_para_reserva(
    id_vehiculo: str,
    id_reserva: str,
    fecha_inicio: str,
    fecha_fin: str,
    estado_reserva: str = "CONFIRMADA",
) -> Dict[str, Any]:
    """Bloquea un vehículo para un intervalo temporal."""

    if not id_vehiculo or not id_reserva:
        raise ValueError(
            "El identificador del vehículo y de la reserva son obligatorios."
        )

    id_vehiculo_norm = id_vehiculo.strip().upper()

    estado_base = _CATALOGO_ESTADOS.get(id_vehiculo_norm)

    if not estado_base:
        raise ValueError(
            f"El vehículo '{id_vehiculo}' no existe en el sistema."
        )

    if estado_base == "MANTENIMIENTO":
        raise ValueError(
            f"No se puede bloquear el vehículo '{id_vehiculo_norm}': "
            "se encuentra en MANTENIMIENTO."
        )

    if estado_reserva.strip().upper() != "CONFIRMADA":
        raise ValueError(
            f"No se puede bloquear el vehículo: la reserva "
            f"'{id_reserva}' no está confirmada "
            f"(estado: {estado_reserva})."
        )

    if not esta_vehiculo_disponible_en_fechas(
        id_vehiculo_norm,
        fecha_inicio,
        fecha_fin,
    ):
        raise ValueError(
            f"El vehículo '{id_vehiculo_norm}' ya cuenta con "
            f"un bloqueo activo incompatible en el rango "
            f"{fecha_inicio} a {fecha_fin}."
        )

    nuevo_bloqueo = BloqueoVehiculo(
        id_vehiculo=id_vehiculo_norm,
        id_reserva=id_reserva.strip().upper(),
        fecha_inicio=fecha_inicio,
        fecha_fin=fecha_fin,
    )

    _HISTORIAL_BLOQUEOS.append(nuevo_bloqueo)

    return {
        "status": "BLOQUEO_CONFIRMADO",
        "bloqueo": nuevo_bloqueo.to_dict(),
    }


def bloquear_reserva_confirmada(
    id_reserva: str,
) -> Dict[str, Any]:
    """
    Bloquea el vehículo y las fechas asociados a una reserva
    que exista realmente entre las reservas confirmadas.
    """

    if not id_reserva or not id_reserva.strip():
        raise ValueError(
            "El identificador de la reserva es obligatorio."
        )

    id_reserva_norm = id_reserva.strip().upper()

    reservas_confirmadas = obtener_reservas_confirmadas()

    reserva = None

    for reserva_confirmada in reservas_confirmadas:
        if reserva_confirmada["id_reserva"] == id_reserva_norm:
            reserva = reserva_confirmada
            break

    if reserva is None:
        raise ValueError(
            f"La reserva '{id_reserva_norm}' no existe "
            "o no se encuentra confirmada."
        )

    return bloquear_vehiculo_para_reserva(
        id_vehiculo=reserva["id_vehiculo"],
        id_reserva=reserva["id_reserva"],
        fecha_inicio=reserva["fecha_inicio"],
        fecha_fin=reserva["fecha_fin"],
        estado_reserva="CONFIRMADA",
    )


if __name__ == "__main__":

    print("Comprobando lógica de bloqueo de vehículos.")

    resultado = bloquear_vehiculo_para_reserva(
        "VEH-01",
        "RES-100",
        "2026-12-01",
        "2026-12-05",
        "CONFIRMADA",
    )

    print(
        f"Bloqueo en rango confirmado: "
        f"{resultado['status']}"
    )

    try:
        bloquear_vehiculo_para_reserva(
            "VEH-02",
            "RES-101",
            "2026-12-01",
            "2026-12-05",
            "RECHAZADA",
        )
    except ValueError as error:
        print(
            f"Rechazo por reserva no confirmada: {error}"
        )

    try:
        bloquear_vehiculo_para_reserva(
            "VEH-01",
            "RES-102",
            "2026-12-03",
            "2026-12-08",
            "CONFIRMADA",
        )
    except ValueError as error:
        print(
            f"Rechazo por solapamiento temporal: {error}"
        )