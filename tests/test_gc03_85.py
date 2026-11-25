
import unittest

from referencia_reserva import generar_referencia
from mostrar_referencia import mostrar_referencia


class TestGC0385(unittest.TestCase):

    def test_generar_referencia_valida(self):
        referencia = generar_referencia(set())

        self.assertTrue(referencia.startswith("RES-"))
        self.assertEqual(len(referencia), 16)

    def test_mostrar_referencia_generada(self):
        referencia = generar_referencia(set())

        resultado = mostrar_referencia(referencia)

        self.assertIn("Reserva confirmada correctamente", resultado)
        self.assertIn(referencia, resultado)

    def test_referencia_no_repetida(self):
        referencia_original = generar_referencia(set())
        referencias_existentes = {referencia_original}

        nueva_referencia = generar_referencia(referencias_existentes)

        self.assertNotEqual(referencia_original, nueva_referencia)
        self.assertNotIn(nueva_referencia, referencias_existentes)

    def test_referencia_invalida(self):
        resultado = mostrar_referencia("REFERENCIA-INCORRECTA")

        self.assertEqual(
            resultado,
            "No se ha generado una referencia válida."
        )

    def test_referencia_no_generada(self):
        resultado = mostrar_referencia(None)

        self.assertEqual(
            resultado,
            "No se ha generado una referencia válida."
        )

    def test_referencia_permanece_igual(self):
        referencia = generar_referencia(set())

        primer_resultado = mostrar_referencia(referencia)
        segundo_resultado = mostrar_referencia(referencia)

        self.assertEqual(primer_resultado, segundo_resultado)


if __name__ == "__main__":
    unittest.main()
