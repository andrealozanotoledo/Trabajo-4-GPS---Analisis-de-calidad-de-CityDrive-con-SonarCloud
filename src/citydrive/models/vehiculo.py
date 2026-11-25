from dataclasses import dataclass, field
from uuid import uuid4


def generar_id_vehiculo() -> str:
    """Genera automáticamente un identificador único para un vehículo."""
    return f"VEH-{uuid4().hex[:8].upper()}"


@dataclass
class Vehiculo:
    marca: str
    modelo: str
    categoria: str
    plazas: int
    capacidad_carga: str
    transmision: str
    estado_operativo: str = "disponible"
    id: str = field(default_factory=generar_id_vehiculo, init=False)