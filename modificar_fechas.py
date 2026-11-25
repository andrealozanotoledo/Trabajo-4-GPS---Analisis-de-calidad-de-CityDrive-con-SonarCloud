
from datetime import date

from mensajes_disponibilidad import mensaje_sin_disponibilidad


def recuperar_fechas_busqueda(fecha_inicio, fecha_fin):
    return {
        "fecha_inicio": fecha_inicio,
        "fecha_fin": fecha_fin
    }


def modificar_y_repetir_busqueda(fecha_inicio, fecha_fin, buscar_vehiculos):
    try:
        inicio = date.fromisoformat(fecha_inicio)
        fin = date.fromisoformat(fecha_fin)
    except (ValueError, TypeError):
        return "Las fechas introducidas no son válidas."

    if fin < inicio:
        return "La fecha de fin no puede ser anterior a la fecha de inicio."

    vehiculos = buscar_vehiculos(inicio, fin)

    mensaje = mensaje_sin_disponibilidad(vehiculos)

    if mensaje:
        return mensaje

    return vehiculos


def volver_a_modificar_fechas(fecha_inicio, fecha_fin, buscar_vehiculos):
    fechas = recuperar_fechas_busqueda(fecha_inicio, fecha_fin)

    print("MODIFICAR FECHAS DE BÚSQUEDA")
    print(f"Fecha de inicio anterior: {fechas['fecha_inicio']}")
    print(f"Fecha de fin anterior: {fechas['fecha_fin']}")

    nueva_fecha_inicio = input("Nueva fecha de inicio (AAAA-MM-DD): ")
    nueva_fecha_fin = input("Nueva fecha de fin (AAAA-MM-DD): ")

    return modificar_y_repetir_busqueda(
        nueva_fecha_inicio,
        nueva_fecha_fin,
        buscar_vehiculos
    )
