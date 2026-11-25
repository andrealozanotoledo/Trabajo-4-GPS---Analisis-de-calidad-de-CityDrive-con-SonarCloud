
import unittest

from src.services import confirmacion_service as servicio


class TestConfirmacionConflictos(unittest.TestCase):

    def setUp(self):
        servicio._RESERVAS_CONFIRMADAS.clear()
        servicio._ESTADO_VEHICULOS_CONFIRMACION.clear()
        servicio._ESTADO_VEHICULOS_CONFIRMACION.update({
            "VEH-101": "DISPONIBLE",
            "VEH-102": "NO DISPONIBLE",
            "VEH-104": "DISPONIBLE"
        })

        self.datos = {
            "id_reserva": "RES-1001",
            "id_vehiculo": "VEH-101",
            "id_cliente": "CLI-10",
            "importe_total": 150.0,
            "fecha_inicio": "2026-12-01",
            "fecha_fin": "2026-12-05"
        }

    def test_confirmacion_correcta(self):
        resultado = servicio.confirmar_y_registrar_reserva(
            self.datos
        )

        self.assertEqual(resultado["estado"], "CONFIRMADA")
        self.assertEqual(
            resultado["detalle"]["id_confirmacion"],
            "CONF-0001"
        )
        self.assertEqual(
            resultado["detalle"]["id_reserva"],
            "RES-1001"
        )
        self.assertEqual(
            len(servicio.obtener_reservas_confirmadas()),
            1
        )

    def test_rechazo_por_fechas_solapadas(self):
        servicio.confirmar_y_registrar_reserva(self.datos)

        nuevos_datos = self.datos.copy()
        nuevos_datos["id_reserva"] = "RES-1002"
        nuevos_datos["fecha_inicio"] = "2026-12-03"
        nuevos_datos["fecha_fin"] = "2026-12-07"

        with self.assertRaisesRegex(ValueError, "Conflicto"):
            servicio.confirmar_y_registrar_reserva(nuevos_datos)

    def test_rechazo_vehiculo_no_disponible(self):
        datos = self.datos.copy()
        datos["id_vehiculo"] = "VEH-102"

        with self.assertRaises(ValueError):
            servicio.confirmar_y_registrar_reserva(datos)

        self.assertEqual(
            len(servicio.obtener_reservas_confirmadas()),
            0
        )

    def test_reservas_sin_solapamiento(self):
        servicio.confirmar_y_registrar_reserva(self.datos)

        nuevos_datos = self.datos.copy()
        nuevos_datos["id_reserva"] = "RES-1002"
        nuevos_datos["fecha_inicio"] = "2026-12-06"
        nuevos_datos["fecha_fin"] = "2026-12-09"

        resultado = servicio.confirmar_y_registrar_reserva(
            nuevos_datos
        )

        self.assertEqual(resultado["estado"], "CONFIRMADA")
        self.assertEqual(
            len(servicio.obtener_reservas_confirmadas()),
            2
        )

    def test_reservas_de_vehiculos_diferentes(self):
        servicio.confirmar_y_registrar_reserva(self.datos)

        nuevos_datos = self.datos.copy()
        nuevos_datos["id_reserva"] = "RES-1002"
        nuevos_datos["id_vehiculo"] = "VEH-104"

        resultado = servicio.confirmar_y_registrar_reserva(
            nuevos_datos
        )

        self.assertEqual(resultado["estado"], "CONFIRMADA")
        self.assertEqual(
            len(servicio.obtener_reservas_confirmadas()),
            2
        )

    def test_conflicto_no_modifica_reserva_anterior(self):
        servicio.confirmar_y_registrar_reserva(self.datos)

        reserva_original = (
            servicio.obtener_reservas_confirmadas()[0].copy()
        )

        nuevos_datos = self.datos.copy()
        nuevos_datos["id_reserva"] = "RES-1002"

        with self.assertRaises(ValueError):
            servicio.confirmar_y_registrar_reserva(nuevos_datos)

        reservas = servicio.obtener_reservas_confirmadas()

        self.assertEqual(len(reservas), 1)
        self.assertEqual(reservas[0], reserva_original)

    def test_rechazo_dato_obligatorio_ausente(self):
        datos = self.datos.copy()
        del datos["id_cliente"]

        with self.assertRaisesRegex(ValueError, "id_cliente"):
            servicio.confirmar_y_registrar_reserva(datos)

    def test_rechazo_importe_no_valido(self):
        datos = self.datos.copy()
        datos["importe_total"] = 0

        with self.assertRaises(ValueError):
            servicio.confirmar_y_registrar_reserva(datos)

        self.assertEqual(
            len(servicio.obtener_reservas_confirmadas()),
            0
        )

    def test_revalidacion_detecta_conflicto(self):
        servicio.confirmar_y_registrar_reserva(self.datos)

        resultado = servicio.revalidar_disponibilidad(
            "VEH-101",
            "2026-12-02",
            "2026-12-04"
        )

        self.assertFalse(resultado)

    def test_revalidacion_detecta_cambio_estado(self):
        servicio._ESTADO_VEHICULOS_CONFIRMACION[
            "VEH-101"
        ] = "NO DISPONIBLE"

        resultado = servicio.revalidar_disponibilidad(
            "VEH-101",
            "2026-12-01",
            "2026-12-05"
        )

        self.assertFalse(resultado)


if __name__ == "__main__":
    unittest.main()
