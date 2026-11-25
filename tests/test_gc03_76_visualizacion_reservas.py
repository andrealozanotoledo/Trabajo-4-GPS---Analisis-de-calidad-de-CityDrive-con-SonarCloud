
import unittest

from src.views.informacion_reserva import definir_informacion_reserva


class TestGC0376VisualizacionReservas(unittest.TestCase):

    def setUp(self):
        self.reserva_1 = {
            "referencia": "RES-001",
            "vehiculo": "Toyota Corolla",
            "fecha_inicio": "2026-11-10",
            "fecha_fin": "2026-11-12",
            "estado": "confirmada"
        }

        self.reserva_2 = {
            "referencia": "RES-002",
            "vehiculo": "Ford Focus",
            "fecha_inicio": "2026-11-15",
            "fecha_fin": "2026-11-20",
            "estado": "pendiente"
        }

    def test_visualizar_dos_reservas_diferentes(self):
        resultado_1 = definir_informacion_reserva(self.reserva_1)
        resultado_2 = definir_informacion_reserva(self.reserva_2)

        self.assertEqual(resultado_1["Referencia"], "RES-001")
        self.assertEqual(resultado_1["Vehículo"], "Toyota Corolla")
        self.assertEqual(resultado_1["Fecha de inicio"], "2026-11-10")
        self.assertEqual(resultado_1["Fecha de fin"], "2026-11-12")
        self.assertEqual(resultado_1["Estado de la reserva"], "confirmada")

        self.assertEqual(resultado_2["Referencia"], "RES-002")
        self.assertEqual(resultado_2["Vehículo"], "Ford Focus")
        self.assertEqual(resultado_2["Fecha de inicio"], "2026-11-15")
        self.assertEqual(resultado_2["Fecha de fin"], "2026-11-20")
        self.assertEqual(resultado_2["Estado de la reserva"], "pendiente")

    def test_consultas_sucesivas_no_mezclan_datos(self):
        primera_consulta = definir_informacion_reserva(self.reserva_1)

        definir_informacion_reserva(self.reserva_2)

        segunda_consulta = definir_informacion_reserva(self.reserva_1)

        self.assertEqual(primera_consulta, segunda_consulta)
        self.assertEqual(segunda_consulta["Referencia"], "RES-001")
        self.assertEqual(segunda_consulta["Vehículo"], "Toyota Corolla")

    def test_visualizar_estado_actualizado(self):
        self.reserva_1["estado"] = "cancelada"

        resultado = definir_informacion_reserva(self.reserva_1)

        self.assertEqual(
            resultado["Estado de la reserva"], "cancelada"
        )

    def test_visualizar_fechas_actualizadas(self):
        self.reserva_1["fecha_inicio"] = "2026-11-18"
        self.reserva_1["fecha_fin"] = "2026-11-22"

        resultado = definir_informacion_reserva(self.reserva_1)

        self.assertEqual(
            resultado["Fecha de inicio"], "2026-11-18"
        )
        self.assertEqual(
            resultado["Fecha de fin"], "2026-11-22"
        )

    def test_no_mostrar_campos_adicionales(self):
        self.reserva_1["cliente"] = "Cliente de prueba"
        self.reserva_1["precio"] = 150

        resultado = definir_informacion_reserva(self.reserva_1)

        self.assertEqual(len(resultado), 5)
        self.assertNotIn("cliente", resultado)
        self.assertNotIn("precio", resultado)
        self.assertNotIn("Cliente", resultado)
        self.assertNotIn("Precio", resultado)

    def test_visualizacion_no_modifica_reserva_original(self):
        datos_originales = self.reserva_1.copy()

        definir_informacion_reserva(self.reserva_1)

        self.assertEqual(self.reserva_1, datos_originales)

    def test_rechazar_cualquier_campo_obligatorio_ausente(self):
        campos_obligatorios = (
            "referencia",
            "vehiculo",
            "fecha_inicio",
            "fecha_fin",
            "estado"
        )

        for campo in campos_obligatorios:
            with self.subTest(campo=campo):
                reserva_incompleta = self.reserva_1.copy()
                del reserva_incompleta[campo]

                with self.assertRaisesRegex(
                    ValueError, "Faltan datos obligatorios"
                ):
                    definir_informacion_reserva(reserva_incompleta)

    def test_distinguir_reservas_del_mismo_vehiculo(self):
        self.reserva_2["vehiculo"] = "Toyota Corolla"

        resultado_1 = definir_informacion_reserva(self.reserva_1)
        resultado_2 = definir_informacion_reserva(self.reserva_2)

        self.assertEqual(
            resultado_1["Vehículo"], resultado_2["Vehículo"]
        )
        self.assertNotEqual(
            resultado_1["Referencia"], resultado_2["Referencia"]
        )
        self.assertNotEqual(
            resultado_1["Fecha de inicio"],
            resultado_2["Fecha de inicio"]
        )
        self.assertNotEqual(
            resultado_1["Estado de la reserva"],
            resultado_2["Estado de la reserva"]
        )


if __name__ == "__main__":
    unittest.main()
