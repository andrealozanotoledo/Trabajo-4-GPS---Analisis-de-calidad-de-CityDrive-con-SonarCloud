
from src.services.obtener_vehiculos_catalogo import obtener_vehiculos_catalogo


def mostrar_catalogo_admin(catalogo):
    vehiculos = obtener_vehiculos_catalogo(catalogo)

    if not vehiculos:
        return "No hay vehículos registrados en el catálogo."

    resultado = ["CATÁLOGO COMPLETO DE VEHÍCULOS"]

    for vehiculo in vehiculos:
        resultado.append(
            f"ID: {vehiculo['id']}\n"
            f"Marca: {vehiculo['marca']}\n"
            f"Modelo: {vehiculo['modelo']}\n"
            f"Categoría: {vehiculo['categoria']}\n"
            f"Plazas: {vehiculo['plazas']}\n"
            f"Capacidad de carga: {vehiculo['capacidad_carga']}\n"
            f"Transmisión: {vehiculo['transmision']}\n"
            f"Estado operativo: {vehiculo['estado_operativo']}\n"
        )

    return "\n".join(resultado)
