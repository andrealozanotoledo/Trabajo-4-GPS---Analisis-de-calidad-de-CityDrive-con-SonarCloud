
import unittest

from src.citydrive.reservas.cancelacion import Reserva, cancelar_reserva


class TestCancelacionReservas(unittest.TestCase):

    def test_cancelar_reserva_activa(self):
        reserva = Reserva("RES-101", "activa")

        resultado = cancelar_reserva(reserva)

        self.assertEqual(resultado.estado, "cancelada")
        self.assertEqual(resultado.referencia, "RES-101")
        self.assertIs(resultado, reserva)

    def test_rechazar_reserva_cancelada(self):
        reserva = Reserva("RES-102", "cancelada")

        with self.assertRaisesRegex(
            ValueError, "Solo se puede cancelar una reserva activa."
        ):
            cancelar_reserva(reserva)

        self.assertEqual(reserva.estado, "cancelada")

    def test_rechazar_reserva_pendiente(self):
        reserva = Reserva("RES-103", "pendiente")

        with self.assertRaisesRegex(
            ValueError, "Solo se puede cancelar una reserva activa."
        ):
            cancelar_reserva(reserva)

        self.assertEqual(reserva.estado, "pendiente")

    def test_conservar_datos_tras_cancelacion_rechazada(self):
        reserva = Reserva("RES-104", "finalizada")

        with self.assertRaises(ValueError):
            cancelar_reserva(reserva)

        self.assertEqual(reserva.referencia, "RES-104")
        self.assertEqual(reserva.estado, "finalizada")

    def test_rechazar_referencia_vacia(self):
        reserva = Reserva("", "activa")

        with self.assertRaises(ValueError):
            cancelar_reserva(reserva)

        self.assertEqual(reserva.estado, "activa")


if __name__ == "__main__":
    unittest.main()
