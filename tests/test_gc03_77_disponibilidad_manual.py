
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from citydrive.services.catalogo import CatalogoVehiculos


class TestDisponibilidadManual(unittest.TestCase):

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

    def test_estado_inicial_disponible(self):
        self.assertEqual(self.coche.estado_operativo, "disponible")
        self.assertEqual(self.furgoneta.estado_operativo, "disponible")

    def test_cambiar_a_no_disponible(self):
        resultado = self.catalogo.cambiar_estado_vehiculo(
            self.coche.id, "no disponible"
        )

        self.assertEqual(resultado.estado_operativo, "no disponible")
        self.assertEqual(self.coche.estado_operativo, "no disponible")

    def test_volver_a_disponible(self):
        self.catalogo.cambiar_estado_vehiculo(
            self.coche.id, "no disponible"
        )

        resultado = self.catalogo.cambiar_estado_vehiculo(
            self.coche.id, "disponible"
        )

        self.assertEqual(resultado.estado_operativo, "disponible")

    def test_estado_actualizado_en_consultas_posteriores(self):
        self.catalogo.cambiar_estado_vehiculo(
            self.coche.id, "no disponible"
        )

        vehiculos = self.catalogo.obtener_vehiculos()

        coche_consultado = next(
            v for v in vehiculos if v.id == self.coche.id
        )

        self.assertEqual(
            coche_consultado.estado_operativo, "no disponible"
        )

    def test_rechazar_vehiculo_inexistente(self):
        with self.assertRaises(ValueError):
            self.catalogo.cambiar_estado_vehiculo(
                "VEH-INEXISTENTE", "no disponible"
            )

    def test_rechazar_estado_no_permitido(self):
        with self.assertRaises(ValueError):
            self.catalogo.cambiar_estado_vehiculo(
                self.coche.id, "mantenimiento"
            )

        with self.assertRaises(ValueError):
            self.catalogo.cambiar_estado_vehiculo(
                self.coche.id, ""
            )

    def test_error_no_modifica_estado_anterior(self):
        self.catalogo.cambiar_estado_vehiculo(
            self.coche.id, "no disponible"
        )

        with self.assertRaises(ValueError):
            self.catalogo.cambiar_estado_vehiculo(
                self.coche.id, "averiado"
            )

        self.assertEqual(
            self.coche.estado_operativo, "no disponible"
        )

    def test_cambio_no_afecta_a_otros_vehiculos(self):
        self.catalogo.cambiar_estado_vehiculo(
            self.coche.id, "no disponible"
        )

        self.assertEqual(
            self.coche.estado_operativo, "no disponible"
        )

        self.assertEqual(
            self.furgoneta.estado_operativo, "disponible"
        )

    def test_cambio_no_modifica_datos_del_vehiculo(self):
        id_original = self.coche.id

        self.catalogo.cambiar_estado_vehiculo(
            self.coche.id, "no disponible"
        )

        self.assertEqual(self.coche.id, id_original)
        self.assertEqual(self.coche.marca, "Toyota")
        self.assertEqual(self.coche.modelo, "Corolla")
        self.assertEqual(self.coche.categoria, "COCHE")
        self.assertEqual(self.coche.plazas, 5)
        self.assertEqual(self.coche.capacidad_carga, "400 litros")
        self.assertEqual(self.coche.transmision, "Manual")


if __name__ == "__main__":
    unittest.main()
