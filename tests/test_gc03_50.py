
import unittest
from unittest.mock import patch

from src.views.filtro_vehiculos import mostrar_filtro


class TestGC0350(unittest.TestCase):

    def test_mensaje_sin_coches_disponibles(self):
        with patch(
            "src.views.filtro_vehiculos.filtrar_por_tipo",
            return_value=[]
        ):
            resultado = mostrar_filtro("COCHE")

        self.assertEqual(
            resultado,
            "No hay resultados para el filtro COCHE."
        )

    def test_mensaje_sin_furgonetas_disponibles(self):
        with patch(
            "src.views.filtro_vehiculos.filtrar_por_tipo",
            return_value=[]
        ):
            resultado = mostrar_filtro("FURGONETA")

        self.assertEqual(
            resultado,
            "No hay resultados para el filtro FURGONETA."
        )

    def test_mensaje_si_todos_estan_no_disponibles(self):
        vehiculos = [
            {
                "id_vehiculo": "VEH-01",
                "modelo": "Toyota Yaris",
                "tipo": "COCHE",
                "disponible": False
            }
        ]

        with patch(
            "src.views.filtro_vehiculos.filtrar_por_tipo",
            return_value=vehiculos
        ):
            resultado = mostrar_filtro("COCHE")

        self.assertEqual(
            resultado,
            "No hay resultados para el filtro COCHE."
        )

    def test_categoria_invalida(self):
        resultado = mostrar_filtro("CAMION")

        self.assertEqual(
            resultado,
            "Tipo de vehículo no válido."
        )


if __name__ == "__main__":
    unittest.main()
