
import unittest

from src.views.informacion_reserva import definir_informacion_reserva


class TestGC0327(unittest.TestCase):

    def setUp(self):
        self.reserva = {
            "referencia": "RES-001",
            "vehiculo": "Toyota Corolla",
            "fecha_inicio": "2026-11-10",
            "fecha_fin": "2026-11-12",
            "estado": "confirmada"
        }

    def test_mostrar_datos_reserva(self):
        resultado = definir_informacion_reserva(self.reserva)

        self.assertEqual(resultado["Referencia"], "RES-001")
        self.assertEqual(resultado["Vehículo"], "Toyota Corolla")
        self.assertEqual(resultado["Fecha de inicio"], "2026-11-10")
        self.assertEqual(resultado["Fecha de fin"], "2026-11-12")
        self.assertEqual(resultado["Estado de la reserva"], "confirmada")

    def test_etiquetas_claras(self):
        resultado = definir_informacion_reserva(self.reserva)

        self.assertEqual(
            list(resultado.keys()),
            [
                "Referencia",
                "Vehículo",
                "Fecha de inicio",
                "Fecha de fin",
                "Estado de la reserva"
            ]
        )

    def test_reserva_vacia(self):
        with self.assertRaisesRegex(
            ValueError, "No se ha encontrado una reserva válida"
        ):
            definir_informacion_reserva({})

    def test_reserva_incompleta(self):
        reserva = self.reserva.copy()
        del reserva["vehiculo"]

        with self.assertRaisesRegex(
            ValueError, "Faltan datos obligatorios"
        ):
            definir_informacion_reserva(reserva)


if __name__ == "__main__":
    unittest.main()
