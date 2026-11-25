from uuid import uuid4


def generar_referencia(referencias_existentes):
    while True:
        referencia = f"RES-{uuid4().hex[:12].upper()}"

        if referencia not in referencias_existentes:
            return referencia
        