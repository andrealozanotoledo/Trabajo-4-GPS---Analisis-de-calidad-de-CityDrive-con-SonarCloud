
import sys
import unittest
from pathlib import Path
from time import perf_counter

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from citydrive.services.catalogo import CatalogoVehiculos
from src.services.obtener_vehiculos_catalogo import obtener_vehiculos_catalogo


class TestCatalogoRendimiento(unittest.TestCase):

    def setUp(self):
        self.catalogo = CatalogoVehiculos()

        self.coche = self.catalogo.registrar_vehiculo(
            marca="Toyota",
            modelo="Corolla",
            categoria="COCHE",
            plazas=5,
            capacidad_carga="400 litros",
            transmision="Manual"
        )

        self.furgoneta = self.catalogo.registrar_vehiculo(
            marca="Ford",
            modelo="Transit",
            categoria="FURGONETA",
            plazas=3,
            capacidad_carga="1000 kg",
            transmision="Automática"
        )

        self.furgoneta.estado_operativo = "no disponible"

    def test_obtener_todos_los_vehiculos(self):
        resultado = obtener_vehiculos_catalogo(self.catalogo)

        self.assertEqual(len(resultado), 2)
        self.assertEqual(
            {v["id"] for v in resultado},
            {self.coche.id, self.furgoneta.id}
        )

    def test_conservar_todos_los_datos(self):
        resultado = obtener_vehiculos_catalogo(self.catalogo)

        coche = next(
            v for v in resultado if v["id"] == self.coche.id
        )

        self.assertEqual(coche["marca"], "Toyota")
        self.assertEqual(coche["modelo"], "Corolla")
        self.assertEqual(coche["categoria"], "COCHE")
        self.assertEqual(coche["plazas"], 5)
        self.assertEqual(coche["capacidad_carga"], "400 litros")
        self.assertEqual(coche["transmision"], "Manual")
        self.assertEqual(coche["estado_operativo"], "disponible")

    def test_incluir_vehiculos_no_disponibles(self):
        resultado = obtener_vehiculos_catalogo(self.catalogo)

        furgoneta = next(
            v for v in resultado if v["id"] == self.furgoneta.id
        )

        self.assertEqual(
            furgoneta["estado_operativo"],
            "no disponible"
        )
        self.assertEqual(len(resultado), 2)

    def test_actualizar_estado_en_consultas_posteriores(self):
        self.coche.estado_operativo = "mantenimiento"

        resultado = obtener_vehiculos_catalogo(self.catalogo)

        coche = next(
            v for v in resultado if v["id"] == self.coche.id
        )

        self.assertEqual(
            coche["estado_operativo"],
            "mantenimiento"
        )

    def test_rechazar_catalogo_invalido(self):
        with self.assertRaises(ValueError):
            obtener_vehiculos_catalogo(None)

        with self.assertRaises(ValueError):
            obtener_vehiculos_catalogo([])

    def test_consulta_no_modifica_vehiculos(self):
        datos_antes = obtener_vehiculos_catalogo(self.catalogo)

        obtener_vehiculos_catalogo(self.catalogo)

        datos_despues = obtener_vehiculos_catalogo(self.catalogo)

        self.assertEqual(datos_antes, datos_despues)
        self.assertEqual(len(self.catalogo.obtener_vehiculos()), 2)

    def test_rendimiento_catalogo_grande(self):
        catalogo_grande = CatalogoVehiculos()

        for i in range(400):
            vehiculo = catalogo_grande.registrar_vehiculo(
                marca="Seat",
                modelo=f"Ibiza-{i}",
                categoria="COCHE",
                plazas=5,
                capacidad_carga="350 litros",
                transmision="Manual"
            )

            if i % 2 == 0:
                vehiculo.estado_operativo = "no disponible"

        inicio = perf_counter()

        resultado = obtener_vehiculos_catalogo(catalogo_grande)

        tiempo = perf_counter() - inicio

        self.assertEqual(len(resultado), 400)
        self.assertEqual(
            sum(
                v["estado_operativo"] == "disponible"
                for v in resultado
            ),
            200
        )
        self.assertLess(tiempo, 2.0)


if __name__ == "__main__":
    unittest.main()
