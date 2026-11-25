
import unittest
from datetime import date

from disponibilidad import Vehiculo, Reserva
from fechas import RangoFechas
from seleccion_vehiculo import seleccionar_vehiculo


class TestGC0374(unittest.TestCase):

    def setUp(self):
        self.vehiculo = Vehiculo(
            identificador="VEH-01",
            marca="Toyota",
            modelo="Corolla",
            tipo="coche"
        )

        self.rango = RangoFechas(
            fecha_inicio=date(2026, 11, 10),
            fecha_fin=date(2026, 11, 12)
        )

    def test_seleccion_disponible(self):
        seleccion = seleccionar_vehiculo(
            self.vehiculo, [], self.rango
        )

        self.assertEqual(seleccion.vehiculo_id, "VEH-01")
        self.assertEqual(seleccion.rango_fechas, self.rango)

    def test_conservar_fechas(self):
        seleccion = seleccionar_vehiculo(
            self.vehiculo, [], self.rango
        )

        self.assertEqual(
            seleccion.rango_fechas.fecha_inicio,
            date(2026, 11, 10)
        )
        self.assertEqual(
            seleccion.rango_fechas.fecha_fin,
            date(2026, 11, 12)
        )

    def test_rechazar_vehiculo_reservado(self):
        reserva = Reserva(
            vehiculo_id="VEH-01",
            fecha_inicio=date(2026, 11, 11),
            fecha_fin=date(2026, 11, 14)
        )

        with self.assertRaisesRegex(
            ValueError, "no está disponible"
        ):
            seleccionar_vehiculo(
                self.vehiculo, [reserva], self.rango
            )

    def test_rechazar_vehiculo_no_disponible(self):
        self.vehiculo.estado = "no disponible"

        with self.assertRaisesRegex(
            ValueError, "no está disponible"
        ):
            seleccionar_vehiculo(
                self.vehiculo, [], self.rango
            )


if __name__ == "__main__":
    unittest.main()
