
import sys
import time
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from citydrive.services.catalogo import CatalogoVehiculos
from src.views.catalogo_admin import mostrar_catalogo_admin
from src.views.menu_admin import menu_administrativo, consultar_desde_menu


class TestGC0321(unittest.TestCase):

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

    def test_consultar_todos_los_vehiculos(self):
        resultado = mostrar_catalogo_admin(self.catalogo)

        self.assertIn("Toyota", resultado)
        self.assertIn("Corolla", resultado)
        self.assertIn("Ford", resultado)
        self.assertIn("Transit", resultado)

    def test_mostrar_todos_los_campos(self):
        resultado = mostrar_catalogo_admin(self.catalogo)

        for campo in (
            "ID:", "Marca:", "Modelo:", "Categoría:",
            "Plazas:", "Capacidad de carga:",
            "Transmisión:", "Estado operativo:"
        ):
            self.assertIn(campo, resultado)

        self.assertIn(self.coche.id, resultado)
        self.assertIn(self.furgoneta.id, resultado)

    def test_mostrar_estado_operativo(self):
        resultado = mostrar_catalogo_admin(self.catalogo)

        self.assertIn("Estado operativo: disponible", resultado)
        self.assertIn("Estado operativo: no disponible", resultado)

    def test_coincidencia_con_datos_almacenados(self):
        resultado = mostrar_catalogo_admin(self.catalogo)

        for vehiculo in self.catalogo.consultar_catalogo():
            self.assertIn(vehiculo["id"], resultado)
            self.assertIn(vehiculo["marca"], resultado)
            self.assertIn(vehiculo["modelo"], resultado)
            self.assertIn(vehiculo["categoria"], resultado)
            self.assertIn(str(vehiculo["plazas"]), resultado)
            self.assertIn(vehiculo["capacidad_carga"], resultado)
            self.assertIn(vehiculo["transmision"], resultado)
            self.assertIn(vehiculo["estado_operativo"], resultado)

    def test_catalogo_vacio(self):
        resultado = mostrar_catalogo_admin(CatalogoVehiculos())

        self.assertEqual(
            resultado,
            "No hay vehículos registrados en el catálogo."
        )

    def test_tiempo_de_respuesta(self):
        inicio = time.perf_counter()

        resultado = mostrar_catalogo_admin(self.catalogo)

        duracion = time.perf_counter() - inicio

        self.assertTrue(resultado)
        self.assertLess(duracion, 2)

    def test_acceso_menu_administrativo(self):
        resultado = menu_administrativo(self.catalogo)

        self.assertIn("MENÚ ADMINISTRATIVO", resultado)
        self.assertIn("1. Consultar catálogo completo", resultado)

    def test_consultar_catalogo_desde_menu(self):
        resultado = consultar_desde_menu(self.catalogo, "1")

        self.assertIn("CATÁLOGO COMPLETO DE VEHÍCULOS", resultado)
        self.assertIn("Toyota", resultado)
        self.assertIn("Ford", resultado)

    def test_opcion_menu_invalida(self):
        resultado = consultar_desde_menu(self.catalogo, "9")

        self.assertEqual(resultado, "Opción no válida.")

    def test_catalogo_invalido_en_menu(self):
        resultado = menu_administrativo(None)

        self.assertEqual(resultado, "Catálogo no válido.")


if __name__ == "__main__":
    unittest.main()

import sys
import time
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from citydrive.services.catalogo import CatalogoVehiculos
from src.views.catalogo_admin import mostrar_catalogo_admin
from src.views.menu_admin import menu_administrativo, consultar_desde_menu


class TestGC0321(unittest.TestCase):

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

    def test_consultar_todos_los_vehiculos(self):
        resultado = mostrar_catalogo_admin(self.catalogo)

        self.assertIn("Toyota", resultado)
        self.assertIn("Corolla", resultado)
        self.assertIn("Ford", resultado)
        self.assertIn("Transit", resultado)

    def test_mostrar_todos_los_campos(self):
        resultado = mostrar_catalogo_admin(self.catalogo)

        for campo in (
            "ID:", "Marca:", "Modelo:", "Categoría:",
            "Plazas:", "Capacidad de carga:",
            "Transmisión:", "Estado operativo:"
        ):
            self.assertIn(campo, resultado)

        self.assertIn(self.coche.id, resultado)
        self.assertIn(self.furgoneta.id, resultado)

    def test_mostrar_estado_operativo(self):
        resultado = mostrar_catalogo_admin(self.catalogo)

        self.assertIn("Estado operativo: disponible", resultado)
        self.assertIn("Estado operativo: no disponible", resultado)

    def test_coincidencia_con_datos_almacenados(self):
        resultado = mostrar_catalogo_admin(self.catalogo)

        for vehiculo in self.catalogo.consultar_catalogo():
            self.assertIn(vehiculo["id"], resultado)
            self.assertIn(vehiculo["marca"], resultado)
            self.assertIn(vehiculo["modelo"], resultado)
            self.assertIn(vehiculo["categoria"], resultado)
            self.assertIn(str(vehiculo["plazas"]), resultado)
            self.assertIn(vehiculo["capacidad_carga"], resultado)
            self.assertIn(vehiculo["transmision"], resultado)
            self.assertIn(vehiculo["estado_operativo"], resultado)

    def test_catalogo_vacio(self):
        resultado = mostrar_catalogo_admin(CatalogoVehiculos())

        self.assertEqual(
            resultado,
            "No hay vehículos registrados en el catálogo."
        )

    def test_tiempo_de_respuesta(self):
        inicio = time.perf_counter()

        resultado = mostrar_catalogo_admin(self.catalogo)

        duracion = time.perf_counter() - inicio

        self.assertTrue(resultado)
        self.assertLess(duracion, 2)

    def test_acceso_menu_administrativo(self):
        resultado = menu_administrativo(self.catalogo)

        self.assertIn("MENÚ ADMINISTRATIVO", resultado)
        self.assertIn("1. Consultar catálogo completo", resultado)

    def test_consultar_catalogo_desde_menu(self):
        resultado = consultar_desde_menu(self.catalogo, "1")

        self.assertIn("CATÁLOGO COMPLETO DE VEHÍCULOS", resultado)
        self.assertIn("Toyota", resultado)
        self.assertIn("Ford", resultado)

    def test_opcion_menu_invalida(self):
        resultado = consultar_desde_menu(self.catalogo, "9")

        self.assertEqual(resultado, "Opción no válida.")

    def test_catalogo_invalido_en_menu(self):
        resultado = menu_administrativo(None)

        self.assertEqual(resultado, "Catálogo no válido.")


if __name__ == "__main__":
    unittest.main()
