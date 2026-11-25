
import unittest

from src.views.consulta_referencia import consultar_por_referencia


class TestGC03109(unittest.TestCase):

    def setUp(self):
        self.reservas = {
            "RES-001": {
                "vehiculo": "Toyota Corolla",
                "fecha_inicio": "2026-11-10",
                "fecha_fin": "2026-11-12"
            }
        }

    def buscar_reserva(self, referencia):
        return self.reservas.get(referencia)

    def test_referencia_existente(self):
        resultado = consultar_por_referencia(
            "RES-001", self.buscar_reserva
        )

        self.assertIn("RESERVA ENCONTRADA", resultado)
        self.assertIn("RES-001", resultado)
        self.assertIn("Toyota Corolla", resultado)

    def test_referencia_inexistente(self):
        resultado = consultar_por_referencia(
            "RES-999", self.buscar_reserva
        )

        self.assertEqual(
            resultado,
            "No se ha encontrado ninguna reserva con esa referencia."
        )

    def test_referencia_vacia(self):
        resultado = consultar_por_referencia(
            "   ", self.buscar_reserva
        )

        self.assertEqual(
            resultado,
            "Debes introducir una referencia de reserva."
        )

    def test_consulta_no_modifica_reserva(self):
        reserva_original = self.reservas["RES-001"].copy()

        consultar_por_referencia(
            "RES-001", self.buscar_reserva
        )

        self.assertEqual(
            self.reservas["RES-001"],
            reserva_original
        )


if __name__ == "__main__":
    unittest.main()
