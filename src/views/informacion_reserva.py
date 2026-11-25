def definir_informacion_reserva(reserva: dict) -> dict:
    if not reserva:
        raise ValueError("No se ha encontrado una reserva válida.")

    campos = (
        "referencia",
        "vehiculo",
        "fecha_inicio",
        "fecha_fin",
        "estado"
    )

    if any(campo not in reserva for campo in campos):
        raise ValueError("Faltan datos obligatorios de la reserva.")

    return {
        "Referencia": reserva["referencia"],
        "Vehículo": reserva["vehiculo"],
        "Fecha de inicio": reserva["fecha_inicio"],
        "Fecha de fin": reserva["fecha_fin"],
        "Estado de la reserva": reserva["estado"]
    }