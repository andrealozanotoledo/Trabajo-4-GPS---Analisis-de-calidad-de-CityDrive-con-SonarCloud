"""Pruebas funcionales para verificar el alta de vehículos y la validación de campos obligatorios."""

from src.services.alta_vehiculo_service import validar_y_procesar_alta_vehiculo

def probar_alta_vehiculo_valida():
    """Caso 1: Registro válido con todos los campos obligatorios informados."""
    datos_validos = {
        "matricula": "1234-BBB",
        "marca": "Toyota",
        "modelo": "Yaris",
        "categoria": "UTILITARIO",
        "precio_dia": 40.0
    }
    resultado = validar_y_procesar_alta_vehiculo(datos_validos)
    assert resultado["status"] == "VALIDADO_CORRECTO"
    assert resultado["vehiculo"]["matricula"] == "1234-BBB"
    print("✔ Caso de prueba 1 (Alta válida): SUPERADO")

def probar_alta_vehiculo_campo_ausente():
    """Caso 2: Registro inválido al faltar un campo obligatorio (marca vacía)."""
    datos_invalidos = {
        "matricula": "1234-BBB",
        "marca": "",  # Campo obligatorio ausente
        "modelo": "Yaris",
        "categoria": "UTILITARIO",
        "precio_dia": 40.0
    }
    error_detectado = False
    try:
        validar_y_procesar_alta_vehiculo(datos_invalidos)
    except ValueError as e:
        error_detectado = True
        print(f"✔ Caso de prueba 2 (Campo ausente): SUPERADO -> Error capturado: {e}")
    
    assert error_detectado, "Fallo: El sistema debía haber impedido el alta por falta de datos obligatorios."

if __name__ == "__main__":
    print("Iniciando pruebas funcionales de alta de vehículo...")
    probar_alta_vehiculo_valida()
    probar_alta_vehiculo_campo_ausente()
    print("Todas las pruebas funcionales han finalizado con éxito.")