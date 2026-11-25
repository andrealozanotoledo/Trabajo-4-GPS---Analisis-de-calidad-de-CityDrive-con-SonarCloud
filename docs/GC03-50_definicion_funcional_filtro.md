
# GC03-50 - Definición funcional del filtro de vehículos

## Objetivo

Definir el comportamiento del filtrado por categoría de vehículo
y validar los mensajes mostrados cuando no existen resultados.

## Categorías disponibles

- COCHE
- FURGONETA
- TODOS

## Comportamiento esperado

1. El usuario realiza una búsqueda indicando un rango de fechas.
2. El sistema obtiene los vehículos disponibles para ese rango.
3. El usuario selecciona COCHE, FURGONETA o TODOS.
4. El filtro se aplica sobre los resultados de la búsqueda original.
5. Al cambiar de categoría, se conserva el rango de fechas.
6. La opción TODOS permite recuperar los resultados sin filtro de categoría.

## Validación de mensajes

- Sin coches disponibles: "No hay resultados para el filtro COCHE."
- Sin furgonetas disponibles: "No hay resultados para el filtro FURGONETA."
- Sin vehículos disponibles: se informa de que no hay resultados.
- Categoría incorrecta: "Tipo de vehículo no válido."

## Datos ficticios

Se contemplan los siguientes escenarios:

- Un coche disponible.
- Una furgoneta disponible.
- Un coche no disponible.
- Una categoría sin resultados.

## Pruebas realizadas

Archivo: tests/test_gc03_50.py

- Validación del mensaje sin coches disponibles.
- Validación del mensaje sin furgonetas disponibles.
- Validación cuando todos los vehículos están no disponibles.
- Validación de categoría incorrecta.

Resultado: 4 pruebas superadas.

## Observaciones pendientes

El servicio actual utiliza categorías SUV, SEDAN y COMPACTO,
mientras que la vista utiliza COCHE y FURGONETA.

Además, la implementación revisada todavía no permite verificar
la conservación del rango de fechas al cambiar de categoría.

Ambos aspectos deberán resolverse o integrarse antes de considerar
completamente validado el comportamiento funcional de US-004.
