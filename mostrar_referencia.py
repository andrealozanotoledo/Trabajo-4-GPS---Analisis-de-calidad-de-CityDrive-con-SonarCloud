def mostrar_referencia(referencia):
    if not isinstance(referencia, str):
        return "No se ha generado una referencia válida."

    if not referencia.startswith("RES-") or len(referencia) != 16:
        return "No se ha generado una referencia válida."

    return f"Reserva confirmada correctamente. Tu referencia es: {referencia}"