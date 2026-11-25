
import unittest
from concurrent.futures import ThreadPoolExecutor
from datetime import date, timedelta
from threading import Barrier
from time import sleep
from unittest.mock import patch

from src.citydrive.reservas.solapamiento import (
    registrar_reserva_si_disponible,
    vehiculo_disponible
)


class TestGC0346Concurrencia(unittest.TestCase):

    def test_reservas_simultaneas_mismo_vehiculo(self):
        reservas = []
        barrera = Barrier(8)

        def comprobar_con_retraso(*args, **kwargs):
            sleep(0.02)
            return vehiculo_disponible(*args, **kwargs)

        def intentar_reservar(_):
            barrera.wait(timeout=10)

            try:
                registrar_reserva_si_disponible(
                    "VEH-001",
                    date(2026, 11, 10),
                    date(2026, 11, 12),
                    reservas
                )
                return "registrada"
            except ValueError:
                return "rechazada"

        with patch(
            "src.citydrive.reservas.solapamiento.vehiculo_disponible",
            side_effect=comprobar_con_retraso
        ):
            with ThreadPoolExecutor(max_workers=8) as executor:
                resultados = list(
                    executor.map(intentar_reservar, range(8))
                )

        self.assertEqual(resultados.count("registrada"), 1)
        self.assertEqual(resultados.count("rechazada"), 7)
        self.assertEqual(len(reservas), 1)

    def test_reservas_simultaneas_vehiculos_diferentes(self):
        reservas = []
        barrera = Barrier(8)

        def registrar(i):
            barrera.wait(timeout=10)

            return registrar_reserva_si_disponible(
                f"VEH-{i:03}",
                date(2026, 11, 10),
                date(2026, 11, 12),
                reservas
            )

        with ThreadPoolExecutor(max_workers=8) as executor:
            resultados = list(executor.map(registrar, range(8)))

        self.assertEqual(len(resultados), 8)
        self.assertEqual(len(reservas), 8)
        self.assertEqual(
            len({r.vehiculo_id for r in reservas}), 8
        )

    def test_reservas_simultaneas_fechas_no_solapadas(self):
        reservas = []
        barrera = Barrier(8)

        def registrar(i):
            inicio = date(2026, 11, 1) + timedelta(days=i * 2)
            fin = inicio + timedelta(days=1)

            barrera.wait(timeout=10)

            return registrar_reserva_si_disponible(
                "VEH-001",
                inicio,
                fin,
                reservas
            )

        with ThreadPoolExecutor(max_workers=8) as executor:
            resultados = list(executor.map(registrar, range(8)))

        self.assertEqual(len(resultados), 8)
        self.assertEqual(len(reservas), 8)
        self.assertTrue(
            all(r.vehiculo_id == "VEH-001" for r in reservas)
        )


if __name__ == "__main__":
    unittest.main()
