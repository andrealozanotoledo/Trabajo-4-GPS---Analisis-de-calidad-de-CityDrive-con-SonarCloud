
import unittest
from unittest.mock import Mock

from src.views.consulta_referencia import consultar_por_referencia


class TestGC0324(unittest.TestCase):

    def setUp(self):
        self.reservas = {
            "RES-001": {
                "vehiculo": "Toyota Corolla",
                "fecha_inicio": "2026-11-10",
                "fecha_fin": "2026-11-12"
            },
            "RES-002": {
                "vehiculo": "Renault Clio",
                "fecha_inicio": "2026-11-15",
                "fecha_fin": "2026-11-18"
            }
        }

    def buscar_reserva(self, referencia):
        return self.reservas.get(referencia)

    def test_referencia_con_espacios(self):
        resultado = consultar_por_referencia(
            "  RES-001  ", self.buscar_reserva
        )

        self.assertIn("RESERVA ENCONTRADA", resultado)
        self.assertIn("Referencia: RES-001", resultado)

    def test_espacios_se_eliminan_antes_de_buscar(self):
        buscador = Mock(return_value=self.reservas["RES-001"])

        consultar_por_referencia("  RES-001  ", buscador)

        buscador.assert_called_once_with("RES-001")

    def test_referencia_inexistente_muestra_mensaje(self):
        resultado = consultar_por_referencia(
            "RES-999", self.buscar_reserva
        )

        self.assertEqual(
            resultado,
            "No se ha encontrado ninguna reserva con esa referencia."
        )

    def test_referencia_vacia_no_ejecuta_busqueda(self):
        buscador = Mock()

        resultado = consultar_por_referencia("   ", buscador)

        self.assertEqual(
            resultado,
            "Debes introducir una referencia de reserva."
        )
        buscador.assert_not_called()

    def test_muestra_todos_los_datos_de_la_reserva(self):
        resultado = consultar_por_referencia(
            "RES-002", self.buscar_reserva
        )

        self.assertIn("RESERVA ENCONTRADA", resultado)
        self.assertIn("Referencia: RES-002", resultado)
        self.assertIn("Vehículo: Renault Clio", resultado)
        self.assertIn("Fecha de inicio: 2026-11-15", resultado)
        self.assertIn("Fecha de fin: 2026-11-18", resultado)

    def test_consulta_referencia_correcta(self):
        resultado = consultar_por_referencia(
            "RES-001", self.buscar_reserva
        )

        self.assertIn("Toyota Corolla", resultado)
        self.assertNotIn("Renault Clio", resultado)

    def test_referencia_inexistente_no_muestra_datos(self):
        resultado = consultar_por_referencia(
            "NO-EXISTE", self.buscar_reserva
        )

        self.assertNotIn("RESERVA ENCONTRADA", resultado)
        self.assertNotIn("Vehículo:", resultado)
        self.assertNotIn("Fecha de inicio:", resultado)


if __name__ == "__main__":
    unittest.main()
