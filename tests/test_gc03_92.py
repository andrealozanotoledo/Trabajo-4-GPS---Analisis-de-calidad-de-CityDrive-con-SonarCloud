
import unittest

from src.views.consulta_reservas_activas_admin import (
    consultar_reservas_activas_admin
)


class TestGC0392(unittest.TestCase):

    def setUp(self):
        self.reservas = [
            {
                "id_reserva": "RES-001",
                "id_vehiculo": "VEH-01",
                "cliente": "Ana",
                "fecha_inicio": "2026-11-10",
                "fecha_fin": "2026-11-12",
                "estado": "CONFIRMADA"
            },
            {
                "id_reserva": "RES-002",
                "id_vehiculo": "VEH-02",
                "cliente": "Luis",
                "fecha_inicio": "2026-11-13",
                "fecha_fin": "2026-11-15",
                "estado": "CANCELADA"
            },
            {
                "id_reserva": "RES-003",
                "id_vehiculo": "VEH-03",
                "cliente": "Marta",
                "fecha_inicio": "2026-11-16",
                "fecha_fin": "2026-11-18",
                "estado": "EN_CURSO"
            },
            {
                "id_reserva": "RES-004",
                "id_vehiculo": "VEH-04",
                "cliente": "Pedro",
                "fecha_inicio": "2026-11-19",
                "fecha_fin": "2026-11-21",
                "estado": "FINALIZADA"
            },
            {
                "id_reserva": "RES-005",
                "id_vehiculo": "VEH-05",
                "cliente": "Lucia",
                "fecha_inicio": "2026-11-22",
                "fecha_fin": "2026-11-24",
                "estado": "PENDIENTE"
            }
        ]

    def test_muestra_reservas_activas(self):
        resultado = consultar_reservas_activas_admin(self.reservas)

        self.assertIn("RES-001", resultado)
        self.assertIn("RES-003", resultado)
        self.assertIn("RES-005", resultado)

    def test_excluye_reservas_canceladas(self):
        resultado = consultar_reservas_activas_admin(self.reservas)

        self.assertNotIn("RES-002", resultado)
        self.assertNotIn("VEH-02", resultado)

    def test_excluye_reservas_finalizadas(self):
        resultado = consultar_reservas_activas_admin(self.reservas)

        self.assertNotIn("RES-004", resultado)
        self.assertNotIn("VEH-04", resultado)

    def test_muestra_datos_correctos(self):
        resultado = consultar_reservas_activas_admin(self.reservas)

        self.assertIn("Referencia: RES-001", resultado)
        self.assertIn("Vehículo: VEH-01", resultado)
        self.assertIn("Fecha de inicio: 2026-11-10", resultado)
        self.assertIn("Fecha de fin: 2026-11-12", resultado)

    def test_no_hay_reservas_activas(self):
        reservas = [
            self.reservas[1],
            self.reservas[3]
        ]

        resultado = consultar_reservas_activas_admin(reservas)

        self.assertEqual(resultado, "No hay reservas activas.")

    def test_lista_vacia(self):
        resultado = consultar_reservas_activas_admin([])

        self.assertEqual(resultado, "No hay reservas activas.")

    def test_estados_minusculas_y_espacios(self):
        reservas = [
            {
                **self.reservas[0],
                "estado": "  confirmada  "
            },
            {
                **self.reservas[1],
                "estado": "  cancelada  "
            }
        ]

        resultado = consultar_reservas_activas_admin(reservas)

        self.assertIn("RES-001", resultado)
        self.assertNotIn("RES-002", resultado)

    def test_no_modifica_reservas_originales(self):
        originales = [r.copy() for r in self.reservas]

        consultar_reservas_activas_admin(self.reservas)

        self.assertEqual(self.reservas, originales)


if __name__ == "__main__":
    unittest.main()
