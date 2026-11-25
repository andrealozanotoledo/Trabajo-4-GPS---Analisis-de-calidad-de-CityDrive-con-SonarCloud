"""Servicio para reintegrar la disponibilidad de un vehículo tras la cancelación de una reserva."""

from typing import Dict, Any
from src.models.cancelacion_disponibilidad import CancelacionDisponibilidad

_DISPONIBILIDAD_VEHICULOS = {
    "VEH-01": "RESERVADO",
    "VEH-02": "RESERVADO",
    "VEH-03": "DISPONIBLE"
}

def reactivar_disponibilidad_por_cancelacion(id_vehiculo: str, id_reserva: str) -> Dict[str, Any]:
    """Actualiza el estado del vehículo a DISPONIBLE al confirmarse la cancelación de una reserva."""
    if not id_vehiculo or not id_vehiculo.strip():
        raise ValueError("El identificador del vehículo es obligatorio.")
    if not id_reserva or not id_reserva.strip():
        raise ValueError("El identificador de la reserva cancelada es obligatorio.")

    id_vehiculo_norm = id_vehiculo.strip().upper()
    if id_vehiculo_norm not in _DISPONIBILIDAD_VEHICULOS:
        raise ValueError(f"El vehículo '{id_vehiculo}' no está registrado en el sistema.")

    _DISPONIBILIDAD_VEHICULOS[id_vehiculo_norm] = "DISPONIBLE"

    registro = CancelacionDisponibilidad(
        id_vehiculo=id_vehiculo_norm,
        id_reserva_cancelada=id_reserva.strip().upper(),
        nuevo_estado="DISPONIBLE"
    )

    return {
        "status": "DISPONIBILIDAD_RESTABLECIDA",
        "detalle": registro.to_dict()
    }

if __name__ == "__main__":
    print("Probando reactivación de disponibilidad tras cancelación:")
    resultado = reactivar_disponibilidad_por_cancelacion("VEH-01", "RES-5501")
    print(f"Resultado: {resultado}")