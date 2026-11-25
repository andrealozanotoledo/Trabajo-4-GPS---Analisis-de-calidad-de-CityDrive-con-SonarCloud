"""Servicio para integrar la confirmación de reserva, resolución de conflictos y revalidación de disponibilidad."""

from datetime import datetime
from threading import Lock
from typing import Dict, Any, List

from src.models.confirmacion_reserva import ConfirmacionReserva


# Catálogo base de disponibilidad de vehículos
_ESTADO_VEHICULOS_CONFIRMACION = {
    "VEH-101": "DISPONIBLE",
    "VEH-102": "NO DISPONIBLE",
    "VEH-104": "DISPONIBLE"
}


# Historial de reservas confirmadas
_RESERVAS_CONFIRMADAS: List[ConfirmacionReserva] = []

# Evita que dos confirmaciones simultáneas puedan revalidar y registrar
# el mismo vehículo para fechas incompatibles al mismo tiempo
_BLOQUEO_CONFIRMACION = Lock()


def _hay_solapamiento(
    inicio_a: str,
    fin_a: str,
    inicio_b: str,
    fin_b: str
) -> bool:
    """Verifica si dos intervalos de fechas colisionan."""
    fmt = "%Y-%m-%d"

    ini_a = datetime.strptime(inicio_a, fmt)
    fin_a_dt = datetime.strptime(fin_a, fmt)
    ini_b = datetime.strptime(inicio_b, fmt)
    fin_b_dt = datetime.strptime(fin_b, fmt)

    return max(ini_a, ini_b) <= min(fin_a_dt, fin_b_dt)


def revalidar_disponibilidad(
    id_vehiculo: str,
    fecha_inicio: str,
    fecha_fin: str
) -> bool:
    """Revalida que el vehículo esté disponible y no tenga reservas confirmadas en conflicto."""
    id_vehiculo_norm = id_vehiculo.strip().upper()

    if (
        _ESTADO_VEHICULOS_CONFIRMACION.get(id_vehiculo_norm)
        != "DISPONIBLE"
    ):
        return False

    for conf in _RESERVAS_CONFIRMADAS:
        if conf.id_vehiculo == id_vehiculo_norm:
            if _hay_solapamiento(
                conf.fecha_inicio,
                conf.fecha_fin,
                fecha_inicio,
                fecha_fin
            ):
                return False

    return True


def confirmar_y_registrar_reserva(
    datos_reserva: Dict[str, Any]
) -> Dict[str, Any]:
    """Valida, revalida disponibilidad y registra definitivamente la reserva."""

    campos_requeridos = [
        "id_reserva",
        "id_vehiculo",
        "id_cliente",
        "importe_total",
        "fecha_inicio",
        "fecha_fin"
    ]

    for campo in campos_requeridos:
        if campo not in datos_reserva or datos_reserva[campo] is None:
            raise ValueError(
                f"Falta el dato obligatorio '{campo}' "
                "para completar el registro."
            )

    if float(datos_reserva["importe_total"]) <= 0:
        raise ValueError(
            "El importe total de la reserva debe ser mayor que cero."
        )

    id_vehiculo = str(
        datos_reserva["id_vehiculo"]
    ).strip().upper()

    fecha_inicio = str(
        datos_reserva["fecha_inicio"]
    ).strip()

    fecha_fin = str(
        datos_reserva["fecha_fin"]
    ).strip()

    # La revalidación y el registro se realizan de forma atómica.
    # Mientras una confirmación está comprobando y registrando,
    # ninguna otra puede realizar simultáneamente el mismo proceso.
    with _BLOQUEO_CONFIRMACION:

        if not revalidar_disponibilidad(
            id_vehiculo,
            fecha_inicio,
            fecha_fin
        ):
            raise ValueError(
                f"Conflicto de reserva: El vehículo "
                f"'{id_vehiculo}' no está disponible "
                "o presenta solapamiento en las fechas seleccionadas."
            )

        id_confirmacion = (
            f"CONF-{len(_RESERVAS_CONFIRMADAS) + 1:04d}"
        )

        registro = ConfirmacionReserva(
            id_confirmacion=id_confirmacion,
            id_reserva=str(
                datos_reserva["id_reserva"]
            ).strip().upper(),
            id_vehiculo=id_vehiculo,
            id_cliente=str(
                datos_reserva["id_cliente"]
            ).strip(),
            importe_total=float(
                datos_reserva["importe_total"]
            ),
            fecha_inicio=fecha_inicio,
            fecha_fin=fecha_fin
        )

        _RESERVAS_CONFIRMADAS.append(registro)

        return {
            "estado": "CONFIRMADA",
            "detalle": registro.to_dict()
        }


def obtener_reservas_confirmadas() -> List[Dict[str, Any]]:
    """Devuelve las confirmaciones vigentes para validación de pruebas."""
    return [
        reserva.to_dict()
        for reserva in _RESERVAS_CONFIRMADAS
    ]


if __name__ == "__main__":

    print(
        "Probando confirmación, revalidación "
        "y conflicto de reservas:"
    )

    datos1 = {
        "id_reserva": "RES-8801",
        "id_vehiculo": "VEH-104",
        "id_cliente": "CLI-205",
        "importe_total": 150.0,
        "fecha_inicio": "2026-12-01",
        "fecha_fin": "2026-12-05"
    }

    r1 = confirmar_y_registrar_reserva(datos1)

    print(
        f"Reserva registrada con éxito: "
        f"{r1['estado']}"
    )

    datos_conflicto = {
        "id_reserva": "RES-8802",
        "id_vehiculo": "VEH-104",
        "id_cliente": "CLI-206",
        "importe_total": 120.0,
        "fecha_inicio": "2026-12-03",
        "fecha_fin": "2026-12-07"
    }

    try:
        confirmar_y_registrar_reserva(
            datos_conflicto
        )
    except ValueError as error:
        print(
            "Conflicto detectado y rechazado "
            f"correctamente: {error}"
        )

    datos_no_disponible = {
        "id_reserva": "RES-8803",
        "id_vehiculo": "VEH-102",
        "id_cliente": "CLI-207",
        "importe_total": 200.0,
        "fecha_inicio": "2026-12-10",
        "fecha_fin": "2026-12-12"
    }

    try:
        confirmar_y_registrar_reserva(
            datos_no_disponible
        )
    except ValueError as error:
        print(
            "Rechazo por falta de disponibilidad "
            f"base superado: {error}"
        )