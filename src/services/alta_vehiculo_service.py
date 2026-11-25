"""Servicio para validar campos obligatorios y procesar el alta de un vehículo."""

from typing import Dict, Any
from src.models.formulario_alta_vehiculo import FormularioAltaVehiculo

def validar_y_procesar_alta_vehiculo(datos: Dict[str, Any]) -> Dict[str, Any]:
    """Valida que los campos obligatorios estén presentes y procesa el formulario de alta."""
    campos_obligatorios = ["matricula", "marca", "modelo", "categoria", "precio_dia"]
    
    for campo in campos_obligatorios:
        if campo not in datos or datos[campo] is None or str(datos[campo]).strip() == "":
            raise ValueError(f"El campo obligatorio '{campo}' no puede estar vacío.")

    try:
        precio = float(datos["precio_dia"])
        if precio <= 0:
            raise ValueError("El precio por día debe ser un valor numérico positivo.")
    except (ValueError, TypeError) as e:
        raise ValueError(f"Error en el campo 'precio_dia': {e}")

    matricula_limpia = str(datos["matricula"]).strip().upper()
    if len(matricula_limpia) < 6:
        raise ValueError("La matrícula debe contener un formato válido.")

    vehiculo_alta = FormularioAltaVehiculo(
        matricula=matricula_limpia,
        marca=str(datos["marca"]).strip(),
        modelo=str(datos["modelo"]).strip(),
        categoria=str(datos["categoria"]).strip().upper(),
        precio_dia=precio
    )

    return {
        "status": "VALIDADO_CORRECTO",
        "vehiculo": vehiculo_alta.to_dict()
    }

if __name__ == "__main__":
    datos_ejemplo = {
        "matricula": "9876-XYZ",
        "marca": "Peugeot",
        "modelo": "208",
        "categoria": "COMPACTO",
        "precio_dia": 38.5
    }
    resultado = validar_y_procesar_alta_vehiculo(datos_ejemplo)
    print(f"Validación de alta completada: {resultado}")