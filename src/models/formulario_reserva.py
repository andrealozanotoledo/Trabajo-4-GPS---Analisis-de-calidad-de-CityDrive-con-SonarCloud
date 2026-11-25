
from dataclasses import dataclass


@dataclass
class FormularioReserva:
    nombre: str
    apellidos: str
    correo: str

    def validar(self) -> tuple[bool, str]:
        if not self.nombre.strip():
            return False, "Debes introducir el nombre."

        if not self.apellidos.strip():
            return False, "Debes introducir los apellidos."

        if not self.correo.strip():
            return False, "Debes introducir el correo electrónico."

        return True, "Los datos del formulario son válidos."
