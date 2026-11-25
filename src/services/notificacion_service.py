"""Servicio para gestionar el aviso de cambios de disponibilidad y control de reservas incompatibles."""

from typing import List, Dict, Any
from src.models.aviso import AvisoDisponibilidad

_ESTADO_VEHICULOS = {
    "VEH-01": "DISPONIBLE",
    "VEH-02": "NO DISPONIBLE"
}
_BUZON_AVISOS: List[AvisoDisponibilidad] = []
_RESERVAS_REGISTRADAS: List[Dict[str, Any]] = []

def emitir_aviso_cambio_disponibilidad(id_vehiculo: str, id_cliente: str, nuevo_estado: str) -> Dict[str, Any]:
    """Genera y registra una alerta al cliente cuando cambia la disponibilidad de un vehículo."""
    if not id_vehiculo or not id_cliente:
        raise ValueError("El identificador del vehículo y del cliente son obligatorios.")

    id_vehiculo_norm = id_vehiculo.strip().upper()
    nuevo_estado_norm = nuevo_estado.strip().upper()
    _ESTADO_VEHICULOS[id_vehiculo_norm] = nuevo_estado_norm

    id_generado = f"AVIS-{len(_BUZON_AVISOS) + 1:04d}"
    mensaje = f"Atención: El vehículo {id_vehiculo_norm} ha cambiado su estado a {nuevo_estado_norm}."

    nuevo_aviso = AvisoDisponibilidad(id_generado, id_vehiculo_norm, id_cliente, mensaje)
    _BUZON_AVISOS.append(nuevo_aviso)

    return nuevo_aviso.to_dict()

def validar_disponibilidad_para_reserva(id_vehiculo: str, id_cliente: str) -> Dict[str, Any]:
    """Comprueba disponibilidad: si no está disponible, emite aviso e impide registrar reserva incompatible."""
    id_vehiculo_norm = id_vehiculo.strip().upper()
    estado = _ESTADO_VEHICULOS.get(id_vehiculo_norm, "NO DISPONIBLE")

    if estado != "DISPONIBLE":
        aviso = emitir_aviso_cambio_disponibilidad(id_vehiculo_norm, id_cliente, estado)
        raise ValueError(f"Reserva incompatible rechazada: Vehículo no disponible. Aviso emitido: {aviso['mensaje']}")

    return {"status": "DISPONIBLE_CONFIRMADO", "id_vehiculo": id_vehiculo_norm}

def intentar_registrar_reserva(id_reserva: str, id_vehiculo: str, id_cliente: str) -> Dict[str, Any]:
    """Intenta registrar la reserva únicamente si el vehículo pasa el filtro de disponibilidad."""
    validar_disponibilidad_para_reserva(id_vehiculo, id_cliente)

    reserva = {
        "id_reserva": id_reserva,
        "id_vehiculo": id_vehiculo.strip().upper(),
        "id_cliente": id_cliente,
        "estado": "CONFIRMADA"
    }
    _RESERVAS_REGISTRADAS.append(reserva)
    return {"status": "REGISTRADA", "reserva": reserva}

def obtener_reservas_registradas() -> List[Dict[str, Any]]:
    """Devuelve la lista actual de reservas registradas para comprobación de pruebas."""
    return list(_RESERVAS_REGISTRADAS)