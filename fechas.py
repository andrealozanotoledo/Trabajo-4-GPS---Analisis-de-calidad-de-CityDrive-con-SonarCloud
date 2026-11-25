
from dataclasses import dataclass
from datetime import date


@dataclass
class RangoFechas:
    fecha_inicio: date | None = None
    fecha_fin: date | None = None

    def validar(self) -> tuple[bool, str]:
        if self.fecha_inicio is None:
            return False, "Debes introducir una fecha de inicio."

        if self.fecha_fin is None:
            return False, "Debes introducir una fecha de fin."

        if not isinstance(self.fecha_inicio, date):
            return False, "La fecha de inicio no es válida."

        if not isinstance(self.fecha_fin, date):
            return False, "La fecha de fin no es válida."

        if self.fecha_fin < self.fecha_inicio:
            return False, "La fecha de fin no puede ser anterior a la fecha de inicio."

        return True, "El rango de fechas es válido."
