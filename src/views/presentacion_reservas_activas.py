def presentar_reservas_activas(reservas):
    if not reservas:
        return "No hay reservas activas."

    lineas = ["RESERVAS ACTIVAS"]

    for reserva in reservas:
        lineas.append(
            f"Referencia: {reserva['referencia']}\n"
            f"Vehículo: {reserva['vehiculo']}\n"
            f"Fecha de inicio: {reserva['fecha_inicio']}\n"
            f"Fecha de fin: {reserva['fecha_fin']}\n"
        )

    return "\n".join(lineas)