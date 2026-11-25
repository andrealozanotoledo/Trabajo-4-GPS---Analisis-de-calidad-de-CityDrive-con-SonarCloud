"""Servicio para validar datos obligatorios y asociar un cliente ficticio a una reserva temporal."""

from typing import Dict, Any
from src.models.reserva_temporal import ReservaTemporal

_RESERVAS_TEMPORALES = []

def asociar_cliente_a_reserva_temporal(id_vehiculo: str, datos_cliente: Dict[str, Any]) -> Dict[str, Any]:
    """Valida los campos obligatorios del cliente y lo asocia a una reserva temporal."""
    if not id_vehiculo or not str(id_vehiculo).strip():
        raise ValueError("El identificador del vehículo es obligatorio para crear la reserva temporal.")

    campos_obligatorios = ["nombre", "email", "telefono"]
    for campo in campos_obligatorios:
        valor = datos_cliente.get(campo)
        if not valor or not str(valor).strip():
            raise ValueError(f"Falta el campo obligatorio '{campo}'. Debe proporcionar información válida.")

    if "@" not in datos_cliente["email"]:
        raise ValueError("El formato del correo electrónico es inválido.")

    id_temp = f"TMP-{len(_RESERVAS_TEMPORALES) + 1:04d}"
    
    reserva = ReservaTemporal(
        id_reserva_temp=id_temp,
        id_vehiculo=str(id_vehiculo).strip().upper(),
        nombre_cliente=str(datos_cliente["nombre"]).strip(),
        email=str(datos_cliente["email"]).strip().lower(),
        telefono=str(datos_cliente["telefono"]).strip()
    )

    _RESERVAS_TEMPORALES.append(reserva)

    return {
        "status": "ASOCIADO_CORRECTO",
        "reserva_temporal": reserva.to_dict()
    }

if __name__ == "__main__":
    print("Probando asociacion de cliente:")
    res = asociar_cliente_a_reserva_temporal("VEH-10", {"nombre": "Ana", "email": "ana@mail.com", "telefono": "600000000"})
    print(res)