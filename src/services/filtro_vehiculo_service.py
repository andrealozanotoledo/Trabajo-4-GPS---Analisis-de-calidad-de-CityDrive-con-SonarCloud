"""Servicio con la lógica de filtrado por tipo de vehículo (coche o furgoneta)."""

from typing import List, Dict, Optional
from src.models.vehiculo_filtro import VehiculoFiltro

# Simulación de catálogo de vehículos en memoria
_INVENTARIO_VEHICULOS = [
    VehiculoFiltro("VEH-01", "Seat", "Ibiza", "COCHE", True),
    VehiculoFiltro("VEH-02", "Renault", "Kangoo", "FURGONETA", True),
    VehiculoFiltro("VEH-03", "Ford", "Transit", "FURGONETA", True),
    VehiculoFiltro("VEH-04", "Toyota", "Corolla", "COCHE", True),
    VehiculoFiltro("VEH-05", "Citroën", "Berlingo", "FURGONETA", False),
]

def filtrar_vehiculos_por_tipo(tipo: Optional[str] = None) -> List[Dict]:
    """Filtra la lista de vehículos disponibles por tipo ('COCHE' o 'FURGONETA').
    
    Si el parámetro es None o está vacío, restaura y devuelve la lista completa.
    """
    if not tipo or tipo.strip() == "":
        # Restaurar lista completa
        return [v.to_dict() for v in _INVENTARIO_VEHICULOS]

    tipo_normalizado = tipo.strip().upper()
    tipos_validos = {"COCHE", "FURGONETA"}
    if tipo_normalizado not in tipos_validos:
        raise ValueError(f"Tipo de vehículo no válido: '{tipo}'. Permitidos: {', '.join(tipos_validos)}")

    return [
        v.to_dict() 
        for v in _INVENTARIO_VEHICULOS 
        if v.tipo == tipo_normalizado
    ]

if __name__ == "__main__":
    print("Probando filtrado de vehículos:")
    coches = filtrar_vehiculos_por_tipo("COCHE")
    print(f"Coches encontrados: {len(coches)}")

    furgonetas = filtrar_vehiculos_por_tipo("FURGONETA")
    print(f"Furgonetas encontradas: {len(furgonetas)}")

    todos = filtrar_vehiculos_por_tipo(None)
    print(f"Total vehículos restaurados sin filtro: {len(todos)}")