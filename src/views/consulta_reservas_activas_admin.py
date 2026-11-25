
from src.services.listado_reservas_service import filtrar_reservas_activas
from src.views.presentacion_reservas_activas import presentar_reservas_activas


def consultar_reservas_activas_admin(reservas):
    activas = filtrar_reservas_activas(reservas)

    reservas_para_vista = []

    for reserva in activas:
        reservas_para_vista.append({
            "referencia": reserva["id_reserva"],
            "vehiculo": reserva["id_vehiculo"],
            "fecha_inicio": reserva["fecha_inicio"],
            "fecha_fin": reserva["fecha_fin"]
        })

    return presentar_reservas_activas(reservas_para_vista)
