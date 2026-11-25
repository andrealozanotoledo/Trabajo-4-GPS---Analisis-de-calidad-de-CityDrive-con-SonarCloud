from citydrive.services.catalogo import CatalogoVehiculos
from src.views.catalogo_admin import mostrar_catalogo_admin


def menu_administrativo(catalogo):
    if not isinstance(catalogo, CatalogoVehiculos):
        return "Catálogo no válido."

    return (
        "MENÚ ADMINISTRATIVO\n"
        "1. Consultar catálogo completo\n"
    )


def consultar_desde_menu(catalogo, opcion):
    if opcion == "1":
        return mostrar_catalogo_admin(catalogo)

    return "Opción no válida."
