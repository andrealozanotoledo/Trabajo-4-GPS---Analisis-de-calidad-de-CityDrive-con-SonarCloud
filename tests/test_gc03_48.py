
import unittest
from datetime import date
from unittest.mock import patch, Mock

from modificar_fechas import (
    recuperar_fechas_busqueda,
    modificar_y_repetir_busqueda,
    volver_a_modificar_fechas
)


class TestGC0348(unittest.TestCase):

    def test_recuperar_fechas_anteriores(self):
        resultado = recuperar_fechas_busqueda(
            "2026-11-10", "2026-11-12"
        )

        self.assertEqual(resultado["fecha_inicio"], "2026-11-10")
        self.assertEqual(resultado["fecha_fin"], "2026-11-12")

    def test_repetir_busqueda_con_nuevas_fechas(self):
        buscar = Mock(return_value=["Toyota Corolla"])

        resultado = modificar_y_repetir_busqueda(
            "2026-11-15", "2026-11-18", buscar
        )

        self.assertEqual(resultado, ["Toyota Corolla"])
        buscar.assert_called_once_with(
            date(2026, 11, 15),
            date(2026, 11, 18)
        )

    def test_nuevo_rango_sin_disponibilidad(self):
        buscar = Mock(return_value=[])

        resultado = modificar_y_repetir_busqueda(
            "2026-11-15", "2026-11-18", buscar
        )

        self.assertEqual(
            resultado,
            "No existen vehículos disponibles para las fechas seleccionadas."
        )
        buscar.assert_called_once()

    def test_fechas_invalidas(self):
        buscar = Mock()

        resultado = modificar_y_repetir_busqueda(
            "fecha-incorrecta", "2026-11-18", buscar
        )

        self.assertEqual(
            resultado,
            "Las fechas introducidas no son válidas."
        )
        buscar.assert_not_called()

    def test_fecha_fin_anterior(self):
        buscar = Mock()

        resultado = modificar_y_repetir_busqueda(
            "2026-11-20", "2026-11-15", buscar
        )

        self.assertEqual(
            resultado,
            "La fecha de fin no puede ser anterior a la fecha de inicio."
        )
        buscar.assert_not_called()

    @patch("builtins.input", side_effect=["2026-11-15", "2026-11-18"])
    def test_volver_modificar_fechas(self, entrada):
        buscar = Mock(return_value=["Ford Transit"])

        resultado = volver_a_modificar_fechas(
            "2026-11-10", "2026-11-12", buscar
        )

        self.assertEqual(resultado, ["Ford Transit"])
        self.assertEqual(entrada.call_count, 2)

        buscar.assert_called_once_with(
            date(2026, 11, 15),
            date(2026, 11, 18)
        )


if __name__ == "__main__":
    unittest.main()
