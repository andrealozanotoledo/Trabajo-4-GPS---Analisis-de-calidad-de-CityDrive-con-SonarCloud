
from src.services.filtro_vehiculo_service import (
    filtrar_vehiculos_por_tipo as filtrar_por_tipo
)


def mostrar_filtro(tipo="TODOS"):
    tipo = tipo.strip().upper()

    if tipo not in ("COCHE", "FURGONETA", "TODOS"):
        return "Tipo de vehículo no válido."

    if tipo == "TODOS":
        vehiculos = filtrar_por_tipo(None)
    else:
        vehiculos = filtrar_por_tipo(tipo)

    vehiculos = [v for v in vehiculos if v["disponible"]]

    if not vehiculos:
        return f"No hay resultados para el filtro {tipo}."

    resultado = ["VEHÍCULOS DISPONIBLES"]

    for vehiculo in vehiculos:
        resultado.append(
            f"{vehiculo['id_vehiculo']} - "
            f"{vehiculo['modelo']} - "
            f"{vehiculo['tipo']}"
        )

    return "\n".join(resultado)


def seleccionar_filtro():
    print("FILTRAR VEHÍCULOS")
    print("1. Coche")
    print("2. Furgoneta")
    print("3. Todos los vehículos")

    opcion = input("Selecciona una opción: ").strip()

    opciones = {
        "1": "COCHE",
        "2": "FURGONETA",
        "3": "TODOS"
    }

    return mostrar_filtro(opciones.get(opcion, ""))


if __name__ == "__main__":
    print(seleccionar_filtro())
