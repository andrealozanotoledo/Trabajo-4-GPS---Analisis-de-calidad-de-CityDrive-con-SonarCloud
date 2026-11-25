from src.citydrive.reservas.cancelacion import Reserva, cancelar_reserva


def probar_cancelacion(referencia, estado):
    reserva = Reserva(referencia, estado)

    if estado == "activa":
        resultado = cancelar_reserva(reserva)
        assert resultado.estado == "cancelada"
        print(f"{referencia}: cancelada correctamente")
    else:
        try:
            cancelar_reserva(reserva)
            raise AssertionError("Se ha permitido una cancelacion no valida")
        except ValueError as error:
            assert str(error) == "Solo se puede cancelar una reserva activa."
            assert reserva.estado == estado
            print(f"{referencia}: {error}")


probar_cancelacion("RES-001", "activa")
probar_cancelacion("RES-002", "cancelada")
probar_cancelacion("RES-003", "pendiente")

print("Todas las pruebas superadas.")