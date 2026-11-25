
import unittest
from unittest.mock import patch

from src.views.filtro_vehiculos import mostrar_filtro, seleccionar_filtro
from src.services.filtro_vehiculo_service import filtrar_vehiculos_por_tipo


class TestGC0352(unittest.TestCase):

    def setUp(self):
        self.vehiculos = [
            {
                "id_vehiculo": "VEH-01",
                "modelo": "Toyota Yaris",
                "tipo": "COCHE",
                "disponible": True
            },
            {
                "id_vehiculo": "VEH-02",
                "modelo": "Ford Transit",
                "tipo": "FURGONETA",
                "disponible": True
            },
            {
                "id_vehiculo": "VEH-03",
                "modelo": "Peugeot 208",
                "tipo": "COCHE",
                "disponible": False
            }
        ]

    def filtrar_simulado(self, tipo):
        if tipo is None or tipo == "TODOS":
            return self.vehiculos

        return [
            v for v in self.vehiculos
            if v["tipo"] == tipo
        ]

    def test_seleccionar_coche(self):
        with patch(
            "src.views.filtro_vehiculos.filtrar_por_tipo",
            side_effect=self.filtrar_simulado
        ):
            resultado = mostrar_filtro("COCHE")

        self.assertIn("Toyota Yaris", resultado)
        self.assertNotIn("Ford Transit", resultado)

    def test_seleccionar_furgoneta(self):
        with patch(
            "src.views.filtro_vehiculos.filtrar_por_tipo",
            side_effect=self.filtrar_simulado
        ):
            resultado = mostrar_filtro("FURGONETA")

        self.assertIn("Ford Transit", resultado)
        self.assertNotIn("Toyota Yaris", resultado)

    def test_solo_vehiculos_disponibles(self):
        with patch(
            "src.views.filtro_vehiculos.filtrar_por_tipo",
            side_effect=self.filtrar_simulado
        ):
            resultado = mostrar_filtro("TODOS")

        self.assertNotIn("Peugeot 208", resultado)

    def test_eliminar_filtro(self):
        with patch(
            "src.views.filtro_vehiculos.filtrar_por_tipo",
            side_effect=self.filtrar_simulado
        ):
            resultado = mostrar_filtro("TODOS")

        self.assertIn("Toyota Yaris", resultado)
        self.assertIn("Ford Transit", resultado)

    def test_tipo_sin_resultados(self):
        with patch(
            "src.views.filtro_vehiculos.filtrar_por_tipo",
            return_value=[]
        ):
            resultado = mostrar_filtro("FURGONETA")

        self.assertEqual(
            resultado,
            "No hay resultados para el filtro FURGONETA."
        )

    def test_tipo_invalido(self):
        resultado = mostrar_filtro("MOTO")

        self.assertEqual(resultado, "Tipo de vehículo no válido.")

    def test_integracion_coches(self):
        resultado = mostrar_filtro("COCHE")

        self.assertIn("Ibiza", resultado)
        self.assertIn("Corolla", resultado)
        self.assertNotIn("Kangoo", resultado)

    def test_integracion_furgonetas(self):
        resultado = mostrar_filtro("FURGONETA")

        self.assertIn("Kangoo", resultado)
        self.assertIn("Transit", resultado)
        self.assertNotIn("Berlingo", resultado)
        self.assertNotIn("Ibiza", resultado)

    def test_integracion_eliminar_filtro(self):
        resultado = mostrar_filtro("TODOS")

        self.assertIn("Ibiza", resultado)
        self.assertIn("Kangoo", resultado)
        self.assertIn("Transit", resultado)
        self.assertIn("Corolla", resultado)
        self.assertNotIn("Berlingo", resultado)

    def test_servicio_rechaza_tipo_invalido(self):
        with self.assertRaises(ValueError):
            filtrar_vehiculos_por_tipo("MOTO")

    def test_menu_selecciona_furgoneta(self):
        with patch("builtins.input", return_value="2"):
            resultado = seleccionar_filtro()

        self.assertIn("Kangoo", resultado)
        self.assertNotIn("Ibiza", resultado)


if __name__ == "__main__":
    unittest.main()
