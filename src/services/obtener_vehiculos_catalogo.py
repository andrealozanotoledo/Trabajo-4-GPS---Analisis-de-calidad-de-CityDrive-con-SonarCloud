from citydrive.services.catalogo import CatalogoVehiculos


def obtener_vehiculos_catalogo(catalogo: CatalogoVehiculos) -> list[dict]:
    if not isinstance(catalogo, CatalogoVehiculos):
        raise ValueError("Se necesita un catálogo de vehículos válido.")

    return catalogo.consultar_catalogo()