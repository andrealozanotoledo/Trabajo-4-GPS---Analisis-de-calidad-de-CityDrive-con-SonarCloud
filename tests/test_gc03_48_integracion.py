
import unittest
from datetime import date
from unittest.mock import patch

from disponibilidad import (
    Vehiculo,
    Reserva,
    consultar_vehiculos_disponibles
)
from fechas import RangoFechas
from modificar_fechas import (
    modificar_y_repetir_busqueda,
    volver_a_modificar_fechas
)


class TestGC0348Integracion(unittest.TestCase):

    def setUp(self):
        self.vehiculos = [
            Vehiculo("VEH-01", "Toyota", "Corolla", "COCHE"),
            Vehiculo("VEH-02", "Renault", "Kangoo", "FURGONETA")
        ]

        self.reservas = [
            Reserva(
                "VEH-01",
                date(2026, 11, 10),
                date(2026, 11, 12)
            )
        ]

    def buscar_vehiculos(self, inicio, fin):
        rango = RangoFechas(inicio, fin)

        return consultar_vehiculos_disponibles(
            self.vehiculos,
            self.reservas,
            rango
        )

    def test_busqueda_inicial_con_reserva(self):
        resultado = self.buscar_vehiculos(
            date(2026, 11, 10),
            date(2026, 11, 12)
        )

        self.assertEqual(len(resultado), 1)
        self.assertEqual(resultado[0].identificador, "VEH-02")

    def test_modificar_fechas_recupera_vehiculo(self):
        resultado = modificar_y_repetir_busqueda(
            "2026-11-15",
            "2026-11-18",
            self.buscar_vehiculos
        )

        self.assertEqual(len(resultado), 2)
        self.assertEqual(
            {v.identificador for v in resultado},
            {"VEH-01", "VEH-02"}
        )

    def test_modificar_fechas_con_nueva_reserva(self):
        resultado = modificar_y_repetir_busqueda(
            "2026-11-11",
            "2026-11-14",
            self.buscar_vehiculos
        )

        self.assertEqual(len(resultado), 1)
        self.assertEqual(resultado[0].identificador, "VEH-02")

    def test_fechas_invertidas_no_ejecutan_busqueda(self):
        with patch.object(
            self,
            "buscar_vehiculos"
        ) as buscador:
            resultado = modificar_y_repetir_busqueda(
                "2026-11-18",
                "2026-11-15",
                buscador
            )

            buscador.assert_not_called()

        self.assertIn("no puede ser anterior", resultado)

    def test_volver_a_modificar_desde_interfaz(self):
        with patch(
            "builtins.input",
            side_effect=["2026-11-15", "2026-11-18"]
        ):
            resultado = volver_a_modificar_fechas(
                "2026-11-10",
                "2026-11-12",
                self.buscar_vehiculos
            )

        self.assertEqual(len(resultado), 2)


if __name__ == "__main__":
    unittest.main()
