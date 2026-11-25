"""Modelo de datos para los campos del formulario de alta de vehículos."""

class FormularioAltaVehiculo:
    def __init__(self, matricula: str, marca: str, modelo: str, categoria: str, precio_dia: float):
        self.matricula = matricula
        self.marca = marca
        self.modelo = modelo
        self.categoria = categoria
        self.precio_dia = precio_dia

    def to_dict(self):
        return {
            "matricula": self.matricula,
            "marca": self.marca,
            "modelo": self.modelo,
            "categoria": self.categoria,
            "precio_dia": self.precio_dia
        }