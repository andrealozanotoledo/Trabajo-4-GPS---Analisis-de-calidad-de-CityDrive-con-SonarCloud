def definir_conflicto_disponibilidad(id_vehiculo: str) -> dict:
    if not id_vehiculo or not id_vehiculo.strip():
        raise ValueError("El identificador del vehículo es obligatorio.")

    id_vehiculo = id_vehiculo.strip().upper()

    return {
        "estado": "CONFLICTO_DISPONIBILIDAD",
        "id_vehiculo": id_vehiculo,
        "reserva_confirmada": False,
        "mensaje": (
            f"El vehículo {id_vehiculo} ha dejado de estar disponible "
            "antes de confirmar la reserva."
        ),
        "accion_recomendada": (
            "Selecciona otro vehículo disponible para continuar "
            "con tu reserva."
        )
    }