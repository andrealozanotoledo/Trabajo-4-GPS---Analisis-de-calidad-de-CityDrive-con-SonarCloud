"""Servicio para consultar y presentar el catálogo completo con el estado operativo de los vehículos."""

from typing import List, Dict, Any, Optional
from src.models.vehiculo_disponible import VehiculoDisponible

# Catálogo global con toda la flota y sus estados operativos
_FLOTA_COMPLETA: List[VehiculoDisponible] = [
    VehiculoDisponible("VEH-01", "Toyota", "Yaris", "COMPACTO", 35.0, "DISPONIBLE", "1234-ABC", 5),
    VehiculoDisponible("VEH-02", "Renault", "Clio", "SEDAN", 42.0, "RESERVADO", "5678-DEF", 5),
    VehiculoDisponible("VEH-03", "Nissan", "Qashqai", "SUV", 58.0, "MANTENIMIENTO", "9012-GHI", 5),
    VehiculoDisponible("VEH-04", "Peugeot", "208", "COMPACTO", 32.0, "DISPONIBLE", "3456-JKL", 5),
    VehiculoDisponible("VEH-05", "Mercedes-Benz", "Vito", "FURGONETA", 75.0, "BAJA_TEMPORAL", "7890-MNP", 9),
    VehiculoDisponible("VEH-06", "Tesla", "Model 3", "SEDAN", 65.0, "DISPONIBLE", "2345-QRS", 5)
]

def obtener_catalogo_completo() -> List[Dict[str, Any]]:
    """Devuelve la información completa y el estado operativo de todos los vehículos de la flota."""
    return [vehiculo.to_dict() for vehiculo in _FLOTA_COMPLETA]

def consultar_vehiculo_por_id(id_vehiculo: str) -> Optional[Dict[str, Any]]:
    """Consulta la información y el estado operativo de un vehículo específico por su identificador."""
    if not id_vehiculo or not str(id_vehiculo).strip():
        raise ValueError("El identificador del vehículo es obligatorio.")

    id_vehiculo_norm = str(id_vehiculo).strip().upper()
    for vehiculo in _FLOTA_COMPLETA:
        if vehiculo.id_vehiculo == id_vehiculo_norm:
            return vehiculo.to_dict()

    return None

def obtener_resumen_estados_operativos() -> Dict[str, int]:
    """Genera un resumen estadístico del número de vehículos por estado operativo."""
    conteo: Dict[str, int] = {}
    for vehiculo in _FLOTA_COMPLETA:
        estado = vehiculo.estado_operativo
        conteo[estado] = conteo.get(estado, 0) + 1
    return conteo

if __name__ == "__main__":
    print("--- 1. Consulta del catálogo completo ---")
    catalogo = obtener_catalogo_completo()
    print(f"Total vehículos en catálogo: {len(catalogo)}")
    for v in catalogo:
        print(f"[{v['id_vehiculo']}] {v['marca']} {v['modelo']} | Tipo: {v['tipo']} | Estado: {v['estado_operativo']} | Tarifa: {v['precio_por_dia']}€/día")

    print("\n--- 2. Resumen de estados operativos ---")
    resumen = obtener_resumen_estados_operativos()
    print("Conteo operativo:", resumen)

    print("\n--- 3. Búsqueda individual ---")
    detalle = consultar_vehiculo_por_id("VEH-03")
    print("Detalle VEH-03:", detalle)