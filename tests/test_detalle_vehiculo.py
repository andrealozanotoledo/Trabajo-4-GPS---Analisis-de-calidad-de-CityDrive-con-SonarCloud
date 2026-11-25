
import unittest
from time import perf_counter

from detalle_vehiculo import VehiculoDetalle, mostrar_detalle_vehiculo


class TestDetalleVehiculo(unittest.TestCase):

    def setUp(self):
        self.catalogo = {
            "V-001": VehiculoDetalle(
                "V-001", "Toyota", "Corolla", "Turismo",
                5, "471 litros", "Automática", "Disponible"
            ),
            "V-002": VehiculoDetalle(
                "V-002", "Ford", "Transit", "Furgoneta",
                3, "8 m3", "Manual", "Disponible"
            )
        }

    def test_datos_vehiculo_seleccionado(self):
        vehiculo = self.catalogo["V-001"]
        resultado = mostrar_detalle_vehiculo(vehiculo)

        self.assertIn("Identificador: V-001", resultado)
        self.assertIn("Marca: Toyota", resultado)
        self.assertIn("Modelo: Corolla", resultado)
        self.assertIn("Categoría: Turismo", resultado)
        self.assertIn("Plazas: 5", resultado)
        self.assertIn("Capacidad de maletero/carga: 471 litros", resultado)
        self.assertIn("Transmisión: Automática", resultado)
        self.assertIn("Estado operativo: Disponible", resultado)

    def test_datos_exactos(self):
        vehiculo = self.catalogo["V-001"]
        resultado = mostrar_detalle_vehiculo(vehiculo)

        esperado = (
            "CARACTERÍSTICAS DEL VEHÍCULO\n"
            "Identificador: V-001\n"
            "Marca: Toyota\n"
            "Modelo: Corolla\n"
            "Categoría: Turismo\n"
            "Plazas: 5\n"
            "Capacidad de maletero/carga: 471 litros\n"
            "Transmisión: Automática\n"
            "Estado operativo: Disponible"
        )

        self.assertEqual(resultado, esperado)

    def test_vehiculos_diferentes(self):
        primero = mostrar_detalle_vehiculo(self.catalogo["V-001"])
        segundo = mostrar_detalle_vehiculo(self.catalogo["V-002"])

        self.assertIn("Toyota", primero)
        self.assertNotIn("Ford", primero)
        self.assertIn("Ford", segundo)
        self.assertNotIn("Toyota", segundo)
        self.assertIn("Identificador: V-002", segundo)

    def test_tiempo_respuesta(self):
        vehiculo = self.catalogo["V-001"]

        inicio = perf_counter()
        resultado = mostrar_detalle_vehiculo(vehiculo)
        tiempo = perf_counter() - inicio

        self.assertTrue(resultado)
        self.assertLess(tiempo, 2.0)
        print(f"\nTiempo de respuesta local: {tiempo:.6f} segundos")


if __name__ == "__main__":
    unittest.main()
