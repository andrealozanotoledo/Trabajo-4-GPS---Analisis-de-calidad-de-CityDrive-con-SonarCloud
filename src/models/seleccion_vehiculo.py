"""Modelo de datos compatible con los flujos de selección de vehículo."""

from datetime import datetime


class SeleccionVehiculo:
    def __init__(
        self,
        id_vehiculo: str,
        matricula: str = None,
        modelo: str = None,
        url_formulario: str = None,
        disponible: bool = True,
        id_seleccion: str = None,
        id_usuario: str = None,
        estado_disponibilidad: str = None,
        fecha_seleccion: str = None,
    ):
        self.id_vehiculo = id_vehiculo
        self.matricula = matricula
        self.modelo = modelo
        self.url_formulario = url_formulario
        self.disponible = disponible

        self.id_seleccion = id_seleccion
        self.id_usuario = id_usuario
        self.estado_disponibilidad = estado_disponibilidad
        self.fecha_seleccion = (
            fecha_seleccion if fecha_seleccion else datetime.now().isoformat()
        )

        if (
            id_seleccion is not None
            or id_usuario is not None
            or estado_disponibilidad is not None
        ):
            self._modo = "seleccion"
        else:
            self._modo = "reserva"

    def to_dict(self):
        if self._modo == "seleccion":
            return {
                "id_seleccion": self.id_seleccion,
                "id_vehiculo": self.id_vehiculo,
                "id_usuario": self.id_usuario,
                "estado_disponibilidad": self.estado_disponibilidad,
                "fecha_seleccion": self.fecha_seleccion,
            }

        return {
            "id_vehiculo": self.id_vehiculo,
            "matricula": self.matricula,
            "modelo": self.modelo,
            "url_formulario": self.url_formulario,
            "disponible": self.disponible,
        }
