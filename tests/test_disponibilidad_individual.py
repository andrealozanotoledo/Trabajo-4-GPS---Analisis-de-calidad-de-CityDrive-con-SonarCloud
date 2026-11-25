
import unittest
from datetime import date
from time import perf_counter

from disponibilidad import Vehiculo, Reserva
from disponibilidad_individual import comprobar_disponibilidad_vehiculo
from fechas import RangoFechas


class TestDisponibilidadIndividual(unittest.TestCase):

    def setUp(self):
        self.vehiculo = Vehiculo(
            "VEH-01", "Toyota", "Corolla", "Turismo", "disponible"
        )
        self.rango = RangoFechas(
            date(2026, 11, 10), date(2026, 11, 14)
        )

    def test_vehiculo_disponible_sin_reservas(self):
        resultado = comprobar_disponibilidad_vehiculo(
            self.vehiculo, [], self.rango
        )
        self.assertTrue(resultado)

    def test_reserva_activa_con_fechas_solapadas(self):
        reservas = [
            Reserva(
                "VEH-01",
                date(2026, 11, 12),
                date(2026, 11, 16),
                "activa"
            )
        ]
        resultado = comprobar_disponibilidad_vehiculo(
            self.vehiculo, reservas, self.rango
        )
        self.assertFalse(resultado)

    def test_vehiculo_inactivo(self):
        self.vehiculo.estado = "inactivo"
        resultado = comprobar_disponibilidad_vehiculo(
            self.vehiculo, [], self.rango
        )
        self.assertFalse(resultado)

    def test_reserva_fuera_del_rango(self):
        reservas = [
            Reserva(
                "VEH-01",
                date(2026, 11, 20),
                date(2026, 11, 25),
                "activa"
            )
        ]
        resultado = comprobar_disponibilidad_vehiculo(
            self.vehiculo, reservas, self.rango
        )
        self.assertTrue(resultado)

    def test_reserva_cancelada_no_bloquea(self):
        reservas = [
            Reserva(
                "VEH-01",
                date(2026, 11, 12),
                date(2026, 11, 16),
                "cancelada"
            )
        ]
        resultado = comprobar_disponibilidad_vehiculo(
            self.vehiculo, reservas, self.rango
        )
        self.assertTrue(resultado)

    def test_reserva_de_otro_vehiculo_no_bloquea(self):
        reservas = [
            Reserva(
                "VEH-02",
                date(2026, 11, 12),
                date(2026, 11, 16),
                "activa"
            )
        ]
        resultado = comprobar_disponibilidad_vehiculo(
            self.vehiculo, reservas, self.rango
        )
        self.assertTrue(resultado)

    def test_rango_de_fechas_invalido(self):
        rango = RangoFechas(
            date(2026, 11, 15),
            date(2026, 11, 10)
        )
        with self.assertRaises(ValueError):
            comprobar_disponibilidad_vehiculo(
                self.vehiculo, [], rango
            )

    def test_tiempo_respuesta_inferior_dos_segundos(self):
        reservas = [
            Reserva(
                f"VEH-{i:04d}",
                date(2026, 11, 10),
                date(2026, 11, 14),
                "activa"
            )
            for i in range(2, 1002)
        ]

        inicio = perf_counter()
        resultado = comprobar_disponibilidad_vehiculo(
            self.vehiculo, reservas, self.rango
        )
        tiempo = perf_counter() - inicio

        self.assertTrue(resultado)
        self.assertLess(tiempo, 2.0)


if __name__ == "__main__":
    unittest.main()
