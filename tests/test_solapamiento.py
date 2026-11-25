
import unittest
from datetime import date

from src.citydrive.reservas.solapamiento import (
    Reserva,
    fechas_se_solapan,
    vehiculo_disponible,
)


class TestSolapamiento(unittest.TestCase):

    def test_reservas_solapadas(self):
        reservas = [
            Reserva("VEH-01", date(2026, 11, 10), date(2026, 11, 12))
        ]

        resultado = vehiculo_disponible(
            "VEH-01", date(2026, 11, 11), date(2026, 11, 14), reservas
        )

        self.assertFalse(resultado)

    def test_reservas_sin_solapamiento(self):
        reservas = [
            Reserva("VEH-01", date(2026, 11, 10), date(2026, 11, 12))
        ]

        resultado = vehiculo_disponible(
            "VEH-01", date(2026, 11, 13), date(2026, 11, 15), reservas
        )

        self.assertTrue(resultado)

    def test_vehiculos_diferentes(self):
        reservas = [
            Reserva("VEH-01", date(2026, 11, 10), date(2026, 11, 12))
        ]

        resultado = vehiculo_disponible(
            "VEH-02", date(2026, 11, 10), date(2026, 11, 12), reservas
        )

        self.assertTrue(resultado)

    def test_fechas_incorrectas(self):
        with self.assertRaises(ValueError):
            vehiculo_disponible(
                "VEH-01", date(2026, 11, 15), date(2026, 11, 10), []
            )

    def test_solapamiento_fecha_limite(self):
        resultado = fechas_se_solapan(
            date(2026, 11, 10),
            date(2026, 11, 12),
            date(2026, 11, 12),
            date(2026, 11, 15),
        )

        self.assertTrue(resultado)

    def test_reserva_cancelada_no_bloquea(self):
        reservas = [
            Reserva(
                "VEH-01",
                date(2026, 11, 10),
                date(2026, 11, 12),
                "cancelada",
            )
        ]

        resultado = vehiculo_disponible(
            "VEH-01", date(2026, 11, 11), date(2026, 11, 12), reservas
        )

        self.assertTrue(resultado)


if __name__ == "__main__":
    unittest.main()
