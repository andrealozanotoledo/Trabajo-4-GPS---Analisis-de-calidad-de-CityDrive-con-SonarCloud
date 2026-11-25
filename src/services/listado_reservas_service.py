"""Servicio para consultar y listar exclusivamente las reservas activas en la vista administrativa."""

from typing import List, Dict, Any
from src.models.reserva_activa import ReservaActiva

# Estados que se consideran activos en el sistema administrativo
_ESTADOS_ACTIVOS = {"CONFIRMADA", "EN_CURSO", "PENDIENTE"}
_ESTADOS_INACTIVOS = {"CANCELADA", "FINALIZADA"}

def filtrar_reservas_activas(reservas: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """Filtra una lista de reservas excluyendo las canceladas o finalizadas."""
    if not isinstance(reservas, list):
        return []

    activas = []
    for r in reservas:
        estado = str(r.get("estado", "")).strip().upper()
        if estado in _ESTADOS_ACTIVOS and estado not in _ESTADOS_INACTIVOS:
            activas.append(r)
    return activas

def presentar_reservas_activas(reservas: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """Punto de entrada para la presentación administrativa: filtra y devuelve solo las reservas activas."""
    return filtrar_reservas_activas(reservas)

if __name__ == "__main__":
    datos_prueba = [
        {"id_reserva": "RES-01", "id_vehiculo": "VEH-01", "cliente": "Juan Pérez", "estado": "CONFIRMADA"},
        {"id_reserva": "RES-02", "id_vehiculo": "VEH-02", "cliente": "Maria López", "estado": "CANCELADA"},
        {"id_reserva": "RES-03", "id_vehiculo": "VEH-03", "cliente": "Carlos Ruiz", "estado": "EN_CURSO"},
        {"id_reserva": "RES-04", "id_vehiculo": "VEH-04", "cliente": "Ana Gómez", "estado": "CANCELADA"},
    ]
    resultado = presentar_reservas_activas(datos_prueba)
    print("Reservas activas presentadas:", len(resultado))
    for r in resultado:
        print(f" - [{r['id_reserva']}] Estado: {r['estado']} | Cliente: {r['cliente']}")