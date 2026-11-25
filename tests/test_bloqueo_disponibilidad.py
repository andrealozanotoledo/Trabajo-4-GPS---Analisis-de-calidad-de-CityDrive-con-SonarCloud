
import unittest

from src.services import bloqueo_service as servicio


class TestBloqueoDisponibilidad(unittest.TestCase):

    def setUp(self):
        servicio._HISTORIAL_BLOQUEOS.clear()

    def test_bloqueo_reserva_confirmada(self):
        resultado = servicio.bloquear_vehiculo_para_reserva(
            "VEH-01", "RES-100", "2026-12-01", "2026-12-05"
        )
        self.assertEqual(resultado["status"], "BLOQUEO_CONFIRMADO")
        self.assertFalse(
            servicio.esta_vehiculo_disponible_en_fechas(
                "VEH-01", "2026-12-02", "2026-12-04"
            )
        )

    def test_rechazar_fechas_solapadas(self):
        servicio.bloquear_vehiculo_para_reserva(
            "VEH-01", "RES-100", "2026-12-01", "2026-12-05"
        )
        with self.assertRaises(ValueError):
            servicio.bloquear_vehiculo_para_reserva(
                "VEH-01", "RES-101", "2026-12-03", "2026-12-08"
            )
        self.assertEqual(len(servicio._HISTORIAL_BLOQUEOS), 1)

    def test_permitir_fechas_diferentes(self):
        servicio.bloquear_vehiculo_para_reserva(
            "VEH-01", "RES-100", "2026-12-01", "2026-12-05"
        )
        resultado = servicio.bloquear_vehiculo_para_reserva(
            "VEH-01", "RES-101", "2026-12-10", "2026-12-15"
        )
        self.assertEqual(resultado["status"], "BLOQUEO_CONFIRMADO")
        self.assertEqual(len(servicio._HISTORIAL_BLOQUEOS), 2)

    def test_reserva_no_confirmada(self):
        with self.assertRaises(ValueError):
            servicio.bloquear_vehiculo_para_reserva(
                "VEH-01", "RES-100", "2026-12-01",
                "2026-12-05", "RECHAZADA"
            )
        self.assertEqual(len(servicio._HISTORIAL_BLOQUEOS), 0)

    def test_vehiculo_en_mantenimiento(self):
        with self.assertRaises(ValueError):
            servicio.bloquear_vehiculo_para_reserva(
                "VEH-03", "RES-100", "2026-12-01", "2026-12-05"
            )

    def test_fechas_limite_incluidas(self):
        servicio.bloquear_vehiculo_para_reserva(
            "VEH-01", "RES-100", "2026-12-01", "2026-12-05"
        )
        self.assertFalse(
            servicio.esta_vehiculo_disponible_en_fechas(
                "VEH-01", "2026-12-05", "2026-12-10"
            )
        )
        self.assertTrue(
            servicio.esta_vehiculo_disponible_en_fechas(
                "VEH-01", "2026-12-06", "2026-12-10"
            )
        )

    def test_vehiculos_independientes(self):
        servicio.bloquear_vehiculo_para_reserva(
            "VEH-01", "RES-100", "2026-12-01", "2026-12-05"
        )
        self.assertTrue(
            servicio.esta_vehiculo_disponible_en_fechas(
                "VEH-02", "2026-12-01", "2026-12-05"
            )
        )


if __name__ == "__main__":
    unittest.main()
