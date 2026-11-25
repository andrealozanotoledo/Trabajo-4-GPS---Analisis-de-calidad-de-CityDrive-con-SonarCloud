
import unittest

from referencia_reserva import generar_referencia
from mostrar_referencia import mostrar_referencia
from src.services import confirmacion_service


class TestGC0385Integracion(unittest.TestCase):

    def setUp(self):
        self.reservas_originales = (
            confirmacion_service._RESERVAS_CONFIRMADAS[:]
        )
        confirmacion_service._RESERVAS_CONFIRMADAS.clear()

    def tearDown(self):
        confirmacion_service._RESERVAS_CONFIRMADAS.clear()
        confirmacion_service._RESERVAS_CONFIRMADAS.extend(
            self.reservas_originales
        )

    def crear_reserva(self, referencia, vehiculo="VEH-101"):
        return {
            "id_reserva": referencia,
            "id_vehiculo": vehiculo,
            "id_cliente": "CLI-001",
            "importe_total": 150.0,
            "fecha_inicio": "2026-12-10",
            "fecha_fin": "2026-12-12"
        }

    def test_referencia_se_conserva_al_confirmar(self):
        referencia = generar_referencia(set())

        resultado = confirmacion_service.confirmar_y_registrar_reserva(
            self.crear_reserva(referencia)
        )

        self.assertEqual(resultado["estado"], "CONFIRMADA")
        self.assertEqual(
            resultado["detalle"]["id_reserva"],
            referencia
        )

    def test_referencia_identifica_reserva_registrada(self):
        referencia = generar_referencia(set())

        confirmacion_service.confirmar_y_registrar_reserva(
            self.crear_reserva(referencia)
        )

        reservas = confirmacion_service.obtener_reservas_confirmadas()

        encontrada = next(
            (r for r in reservas if r["id_reserva"] == referencia),
            None
        )

        self.assertIsNotNone(encontrada)
        self.assertEqual(encontrada["id_vehiculo"], "VEH-101")
        self.assertEqual(encontrada["id_cliente"], "CLI-001")

    def test_referencia_mostrada_corresponde_a_reserva(self):
        referencia = generar_referencia(set())

        confirmacion_service.confirmar_y_registrar_reserva(
            self.crear_reserva(referencia)
        )

        mensaje = mostrar_referencia(referencia)
        reservas = confirmacion_service.obtener_reservas_confirmadas()

        referencias_registradas = {
            reserva["id_reserva"] for reserva in reservas
        }

        self.assertIn(referencia, mensaje)
        self.assertIn(referencia, referencias_registradas)

    def test_referencia_inexistente_no_identifica_reserva(self):
        reservas = confirmacion_service.obtener_reservas_confirmadas()

        encontrada = next(
            (r for r in reservas if r["id_reserva"] == "RES-INEXISTENTE"),
            None
        )

        self.assertIsNone(encontrada)

    def test_dos_reservas_tienen_referencias_diferentes(self):
        referencia1 = generar_referencia(set())
        referencia2 = generar_referencia({referencia1})

        confirmacion_service.confirmar_y_registrar_reserva(
            self.crear_reserva(referencia1, "VEH-101")
        )

        confirmacion_service.confirmar_y_registrar_reserva(
            self.crear_reserva(referencia2, "VEH-104")
        )

        reservas = confirmacion_service.obtener_reservas_confirmadas()

        referencias = {r["id_reserva"] for r in reservas}

        self.assertEqual(len(referencias), 2)
        self.assertIn(referencia1, referencias)
        self.assertIn(referencia2, referencias)


if __name__ == "__main__":
    unittest.main()
