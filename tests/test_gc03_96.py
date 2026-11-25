import unittest

from src.services.conflicto_disponibilidad import definir_conflicto_disponibilidad
from src.services import notificacion_service as servicio


class TestGC0396(unittest.TestCase):

    def setUp(self):
        servicio._ESTADO_VEHICULOS.clear()
        servicio._ESTADO_VEHICULOS.update({
            "VEH-01": "DISPONIBLE",
            "VEH-02": "NO DISPONIBLE"
        })
        servicio._BUZON_AVISOS.clear()
        servicio._RESERVAS_REGISTRADAS.clear()

    def test_mensaje_conflicto_claro(self):
        resultado = definir_conflicto_disponibilidad("veh-02")

        self.assertEqual(
            resultado["estado"], "CONFLICTO_DISPONIBILIDAD"
        )
        self.assertEqual(resultado["id_vehiculo"], "VEH-02")
        self.assertFalse(resultado["reserva_confirmada"])
        self.assertIn("VEH-02", resultado["mensaje"])
        self.assertIn("dejado de estar disponible", resultado["mensaje"])
        self.assertIn("Selecciona otro vehículo", resultado["accion_recomendada"])

    def test_aviso_al_cliente(self):
        aviso = servicio.emitir_aviso_cambio_disponibilidad(
            "VEH-02", "CLI-10", "NO DISPONIBLE"
        )

        self.assertEqual(aviso["id_cliente"], "CLI-10")
        self.assertIn("VEH-02", aviso["mensaje"])
        self.assertIn("NO DISPONIBLE", aviso["mensaje"])

    def test_conflicto_no_registra_reserva(self):
        with self.assertRaisesRegex(
            ValueError, "Reserva incompatible rechazada"
        ):
            servicio.intentar_registrar_reserva(
                "RES-201", "VEH-02", "CLI-10"
            )

        self.assertEqual(
            len(servicio.obtener_reservas_registradas()), 0
        )

    def test_identificador_obligatorio(self):
        with self.assertRaises(ValueError):
            definir_conflicto_disponibilidad("")


if __name__ == "__main__":
    unittest.main()