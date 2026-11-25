"""Servicio para gestionar la carga en formulario de administración, validación y guardado de cambios de vehículos."""

from datetime import datetime
from typing import Dict, Any, List
from src.models.modificacion_vehiculo import ModificacionVehiculo

# Repositorio de vehículos en catálogo simulado
_CATALOGO_VEHICULOS: Dict[str, ModificacionVehiculo] = {
    "VEH-01": ModificacionVehiculo("VEH-01", "Toyota", "Yaris", "COMPACTO", 35.0, "DISPONIBLE"),
    "VEH-02": ModificacionVehiculo("VEH-02", "Renault", "Clio", "SEDAN", 42.0, "DISPONIBLE"),
    "VEH-03": ModificacionVehiculo("VEH-03", "Nissan", "Qashqai", "SUV", 58.0, "MANTENIMIENTO")
}

_ESTADOS_VALIDOS = {"DISPONIBLE", "RESERVADO", "MANTENIMIENTO", "BAJA_TEMPORAL"}
_TIPOS_VALIDOS = {"COMPACTO", "SEDAN", "SUV", "FURGONETA"}

def obtener_datos_para_formulario(id_vehiculo: str) -> Dict[str, Any]:
    """Carga los datos actuales del vehículo para precargar el formulario administrativo."""
    if not id_vehiculo or not str(id_vehiculo).strip():
        raise ValueError("El identificador del vehículo es obligatorio para cargar el formulario.")

    id_vehiculo_norm = str(id_vehiculo).strip().upper()
    vehiculo = _CATALOGO_VEHICULOS.get(id_vehiculo_norm)

    if not vehiculo:
        raise ValueError(f"No se encontró ningún vehículo con identificador '{id_vehiculo}'.")

    return {
        "status": "CARGA_EXITOSA",
        "formulario": vehiculo.to_dict()
    }

def guardar_cambios_vehiculo(id_vehiculo: str, datos_formulario: Dict[str, Any]) -> Dict[str, Any]:
    """Valida los campos del formulario administrativo y persiste las modificaciones del vehículo."""
    if not id_vehiculo or not str(id_vehiculo).strip():
        raise ValueError("El identificador del vehículo es obligatorio.")

    id_vehiculo_norm = str(id_vehiculo).strip().upper()
    vehiculo_existente = _CATALOGO_VEHICULOS.get(id_vehiculo_norm)
    if not vehiculo_existente:
        raise ValueError(f"El vehículo con identificador '{id_vehiculo}' no existe en el sistema.")

    # Validación de campos requeridos
    campos_requeridos = ["marca", "modelo", "tipo", "precio_por_dia", "estado"]
    for campo in campos_requeridos:
        if campo not in datos_formulario or datos_formulario[campo] is None:
            raise ValueError(f"El campo '{campo}' es obligatorio en el formulario de edición.")
        if isinstance(datos_formulario[campo], str) and not datos_formulario[campo].strip():
            raise ValueError(f"El campo '{campo}' no puede estar vacío.")

    # Validación de precio
    try:
        precio = float(datos_formulario["precio_por_dia"])
        if precio <= 0:
            raise ValueError()
    except (ValueError, TypeError):
        raise ValueError("El precio por día debe ser un valor numérico superior a 0.")

    # Validación de tipo de vehículo
    tipo_norm = str(datos_formulario["tipo"]).strip().upper()
    if tipo_norm not in _TIPOS_VALIDOS:
        raise ValueError(f"Tipo de vehículo inválido: '{tipo_norm}'. Tipos permitidos: {', '.join(_TIPOS_VALIDOS)}.")

    # Validación de estado
    estado_norm = str(datos_formulario["estado"]).strip().upper()
    if estado_norm not in _ESTADOS_VALIDOS:
        raise ValueError(f"Estado de vehículo inválido: '{estado_norm}'. Estados válidos: {', '.join(_ESTADOS_VALIDOS)}.")

    # Persistencia de cambios actualizados
    vehiculo_actualizado = ModificacionVehiculo(
        id_vehiculo=id_vehiculo_norm,
        marca=str(datos_formulario["marca"]).strip(),
        modelo=str(datos_formulario["modelo"]).strip(),
        tipo=tipo_norm,
        precio_por_dia=precio,
        estado=estado_norm,
        fecha_actualizacion=datetime.now().isoformat()
    )

    _CATALOGO_VEHICULOS[id_vehiculo_norm] = vehiculo_actualizado

    return {
        "status": "GUARDADO_EXITOSO",
        "mensaje": f"Vehículo '{id_vehiculo_norm}' actualizado correctamente en el sistema.",
        "vehiculo": vehiculo_actualizado.to_dict()
    }

def listar_vehiculos_actualizados() -> List[Dict[str, Any]]:
    """Devuelve la lista actual del catálogo con las modificaciones consolidadas."""
    return [v.to_dict() for v in _CATALOGO_VEHICULOS.values()]

if __name__ == "__main__":
    print("--- 1. Cargar formulario de edición ---")
    datos_previos = obtener_datos_para_formulario("VEH-01")
    print("Datos precargados:", datos_previos["formulario"])

    print("\n--- 2. Guardar modificaciones válidas ---")
    nuevos_datos = {
        "marca": "Toyota",
        "modelo": "Yaris Cross Hybrid",
        "tipo": "SUV",
        "precio_por_dia": 49.5,
        "estado": "DISPONIBLE"
    }
    resultado = guardar_cambios_vehiculo("VEH-01", nuevos_datos)
    print(resultado["mensaje"])
    print("Vehículo actualizado:", resultado["vehiculo"])

    print("\n--- 3. Comprobación de rechazo por precio negativo ---")
    try:
        guardar_cambios_vehiculo("VEH-02", {**nuevos_datos, "precio_por_dia": -10})
    except ValueError as e:
        print("✔ Validación correcta de precio:", e)

    print("\n--- 4. Comprobación de rechazo por vehículo inexistente ---")
    try:
        guardar_cambios_vehiculo("VEH-999", nuevos_datos)
    except ValueError as e:
        print("✔ Validación correcta de existencia:", e)