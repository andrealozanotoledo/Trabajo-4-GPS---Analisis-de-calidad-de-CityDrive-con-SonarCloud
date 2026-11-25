def consultar_por_referencia(referencia, buscar_reserva):
    referencia = referencia.strip()

    if not referencia:
        return "Debes introducir una referencia de reserva."

    reserva = buscar_reserva(referencia)

    if reserva is None:
        return "No se ha encontrado ninguna reserva con esa referencia."

    return (
        "RESERVA ENCONTRADA\n"
        f"Referencia: {referencia}\n"
        f"Vehículo: {reserva['vehiculo']}\n"
        f"Fecha de inicio: {reserva['fecha_inicio']}\n"
        f"Fecha de fin: {reserva['fecha_fin']}"
    )