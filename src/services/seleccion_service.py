"""Servicio para procesar las acciones de selección de vehículo."""

from typing import Dict, Any
from src.models.seleccion_vehiculo import SeleccionVehiculo


_CATALOGO_AUTORENT = {
    "VEH-01": {
        "matricula": "1111-AAA",
        "modelo": "Seat Ibiza",
        "disponible": True,
    },
    "VEH-02": {
        "matricula": "2222-BBB",
        "modelo": "Ford Focus",
        "disponible": False,
    },
    "VEH-03": {
        "matricula": "3333-CCC",
        "modelo": "Renault Clio",
        "disponible": True,
    },
}


_VEHICULOS_CATALOGO = {
    "VEH-01": "DISPONIBLE",
    "VEH-02": "RESERVADO",
}


def seleccionar_vehiculo_para_reserva(
    id_vehiculo: str,
) -> Dict[str, Any]:
    if not id_vehiculo or not id_vehiculo.strip():
        raise ValueError(
            "El identificador del vehículo es obligatorio para realizar la selección."
        )

    id_normalizado = id_vehiculo.strip().upper()
    vehiculo = _CATALOGO_AUTORENT.get(id_normalizado)

    if not vehiculo:
        raise ValueError(
            f"El vehículo con identificador '{id_vehiculo}' no existe en AutoRent."
        )

    if not vehiculo["disponible"]:
        raise ValueError(
            f"El vehículo '{vehiculo['modelo']}' no está disponible para selección."
        )

    url_destino = f"/reservas/formulario?id_vehiculo={id_normalizado}"

    seleccion = SeleccionVehiculo(
        id_vehiculo=id_normalizado,
        matricula=vehiculo["matricula"],
        modelo=vehiculo["modelo"],
        url_formulario=url_destino,
        disponible=True,
    )

    return {
        "status": "SELECCIONADO",
        "redireccion": seleccion.url_formulario,
        "datos": seleccion.to_dict(),
    }


def seleccionar_vehiculo(
    id_vehiculo: str,
    id_usuario: str,
) -> Dict[str, Any]:
    if not id_vehiculo or not id_usuario:
        raise ValueError(
            "Se requieren el identificador del vehículo y del usuario."
        )

    id_vehiculo_norm = id_vehiculo.strip().upper()
    estado = _VEHICULOS_CATALOGO.get(id_vehiculo_norm)

    if not estado:
        raise ValueError(
            f"El vehículo '{id_vehiculo}' no existe en el catálogo."
        )

    if estado != "DISPONIBLE":
        raise ValueError(
            f"No se puede seleccionar el vehículo '{id_vehiculo_norm}': "
            "no se encuentra disponible."
        )

    seleccion = SeleccionVehiculo(
        id_seleccion=f"SEL-{id_vehiculo_norm}",
        id_vehiculo=id_vehiculo_norm,
        id_usuario=id_usuario.strip(),
        estado_disponibilidad=estado,
    )

    return {
        "status": "SELECCION_EXITOSA",
        "redireccion": f"/reservas/formulario?vehiculo={id_vehiculo_norm}",
        "detalle": seleccion.to_dict(),
    }
