
import sys
import unittest
from pathlib import Path
from datetime import date

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from citydrive.services.catalogo import CatalogoVehiculos
from disponibilidad import (
    Vehiculo as VehiculoBusqueda,
    consultar_vehiculos_disponibles
)
from fechas import RangoFechas


class TestGC0335(unittest.TestCase):

    def setUp(self):
        self.catalogo = CatalogoVehiculos()

        self.vehiculo = self.catalogo.registrar_vehiculo(
            marca="Toyota",
            modelo="Corolla",
            categoria="COCHE",
            plazas=5,
            capacidad_carga="400 litros",
            transmision="Manual"
        )

    def test_estado_inicial_disponible(self):
        self.assertEqual(
            self.vehiculo.estado_operativo,
            "disponible"
        )

    def test_cambiar_a_no_disponible(self):
        resultado = self.catalogo.cambiar_estado_vehiculo(
            self.vehiculo.id,
            "no disponible"
        )

        self.assertEqual(
            resultado.estado_operativo,
            "no disponible"
        )

    def test_volver_a_disponible(self):
        self.catalogo.cambiar_estado_vehiculo(
            self.vehiculo.id,
            "no disponible"
        )

        resultado = self.catalogo.cambiar_estado_vehiculo(
            self.vehiculo.id,
            "disponible"
        )

        self.assertEqual(
            resultado.estado_operativo,
            "disponible"
        )

    def test_estado_se_conserva_en_catalogo(self):
        self.catalogo.cambiar_estado_vehiculo(
            self.vehiculo.id,
            "no disponible"
        )

        vehiculos = self.catalogo.obtener_vehiculos()

        self.assertEqual(
            vehiculos[0].estado_operativo,
            "no disponible"
        )

    def test_estado_invalido(self):
        with self.assertRaises(ValueError):
            self.catalogo.cambiar_estado_vehiculo(
                self.vehiculo.id,
                "averiado"
            )

        self.assertEqual(
            self.vehiculo.estado_operativo,
            "disponible"
        )

    def test_vehiculo_inexistente(self):
        with self.assertRaises(ValueError):
            self.catalogo.cambiar_estado_vehiculo(
                "VEH-INEXISTENTE",
                "no disponible"
            )

    def test_consulta_refleja_nuevo_estado(self):
        self.catalogo.cambiar_estado_vehiculo(
            self.vehiculo.id,
            "no disponible"
        )

        vehiculos = self.catalogo.obtener_vehiculos()

        self.assertEqual(
            vehiculos[0].estado_operativo,
            "no disponible"
        )

    def test_vehiculo_no_disponible_no_es_reservable(self):
        self.catalogo.cambiar_estado_vehiculo(
            self.vehiculo.id,
            "no disponible"
        )

        vehiculo_busqueda = VehiculoBusqueda(
            identificador=self.vehiculo.id,
            marca=self.vehiculo.marca,
            modelo=self.vehiculo.modelo,
            tipo=self.vehiculo.categoria,
            estado=self.vehiculo.estado_operativo
        )

        rango = RangoFechas(
            fecha_inicio=date(2026, 11, 10),
            fecha_fin=date(2026, 11, 12)
        )

        resultado = consultar_vehiculos_disponibles(
            [vehiculo_busqueda],
            [],
            rango
        )

        self.assertEqual(resultado, [])


if __name__ == "__main__":
    unittest.main()
