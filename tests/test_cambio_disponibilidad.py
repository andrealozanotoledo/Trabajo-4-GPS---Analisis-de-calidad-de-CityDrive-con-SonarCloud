
import unittest
from datetime import datetime

from src.services import notificacion_service as servicio


class TestCambioDisponibilidad(unittest.TestCase):

    def setUp(self):
        servicio._ESTADO_VEHICULOS.clear()
        servicio._ESTADO_VEHICULOS.update({
            "VEH-01": "DISPONIBLE",
            "VEH-02": "NO DISPONIBLE"
        })
        servicio._BUZON_AVISOS.clear()
        servicio._RESERVAS_REGISTRADAS.clear()

    def test_generar_aviso(self):
        aviso = servicio.emitir_aviso_cambio_disponibilidad(
            "VEH-01", "CLI-10", "NO DISPONIBLE"
        )

        self.assertEqual(aviso["id_aviso"], "AVIS-0001")
        self.assertEqual(aviso["id_vehiculo"], "VEH-01")
        self.assertEqual(aviso["id_cliente"], "CLI-10")
        self.assertIn("NO DISPONIBLE", aviso["mensaje"])

    def test_rechazar_solicitud_incompatible(self):
        servicio.emitir_aviso_cambio_disponibilidad(
            "VEH-01", "CLI-10", "NO DISPONIBLE"
        )

        with self.assertRaisesRegex(
            ValueError, "Reserva incompatible rechazada"
        ):
            servicio.validar_disponibilidad_para_reserva(
                "VEH-01", "CLI-10"
            )

    def test_validar_vehiculo_disponible(self):
        resultado = servicio.validar_disponibilidad_para_reserva(
            "VEH-01", "CLI-10"
        )

        self.assertEqual(
            resultado["status"], "DISPONIBLE_CONFIRMADO"
        )
        self.assertEqual(resultado["id_vehiculo"], "VEH-01")

    def test_avisos_independientes(self):
        aviso1 = servicio.emitir_aviso_cambio_disponibilidad(
            "VEH-01", "CLI-10", "NO DISPONIBLE"
        )
        aviso2 = servicio.emitir_aviso_cambio_disponibilidad(
            "VEH-02", "CLI-20", "DISPONIBLE"
        )

        self.assertEqual(aviso1["id_aviso"], "AVIS-0001")
        self.assertEqual(aviso2["id_aviso"], "AVIS-0002")
        self.assertEqual(aviso1["id_cliente"], "CLI-10")
        self.assertEqual(aviso2["id_cliente"], "CLI-20")

        datetime.fromisoformat(aviso1["fecha"])
        datetime.fromisoformat(aviso2["fecha"])

    def test_reserva_incompatible_no_registrada(self):
        servicio.emitir_aviso_cambio_disponibilidad(
            "VEH-01", "CLI-10", "NO DISPONIBLE"
        )

        with self.assertRaises(ValueError):
            servicio.intentar_registrar_reserva(
                "RES-101", "VEH-01", "CLI-10"
            )

        reservas = servicio.obtener_reservas_registradas()
        self.assertEqual(len(reservas), 0)

    def test_reserva_valida_registrada(self):
        resultado = servicio.intentar_registrar_reserva(
            "RES-102", "VEH-01", "CLI-10"
        )

        reservas = servicio.obtener_reservas_registradas()

        self.assertEqual(resultado["status"], "REGISTRADA")
        self.assertEqual(len(reservas), 1)
        self.assertEqual(reservas[0]["id_reserva"], "RES-102")
        self.assertEqual(reservas[0]["id_vehiculo"], "VEH-01")
        self.assertEqual(reservas[0]["estado"], "CONFIRMADA")

    def test_rechazo_conserva_reserva_anterior(self):
        servicio.intentar_registrar_reserva(
            "RES-100", "VEH-01", "CLI-10"
        )

        reserva_original = (
            servicio.obtener_reservas_registradas()[0].copy()
        )

        servicio.emitir_aviso_cambio_disponibilidad(
            "VEH-01", "CLI-20", "NO DISPONIBLE"
        )

        with self.assertRaises(ValueError):
            servicio.intentar_registrar_reserva(
                "RES-103", "VEH-01", "CLI-20"
            )

        reservas = servicio.obtener_reservas_registradas()

        self.assertEqual(len(reservas), 1)
        self.assertEqual(reservas[0], reserva_original)


if __name__ == "__main__":
    unittest.main()
