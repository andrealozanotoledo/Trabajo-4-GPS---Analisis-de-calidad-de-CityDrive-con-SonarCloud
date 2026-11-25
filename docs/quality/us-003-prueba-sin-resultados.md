# US-003 — Prueba determinista sin resultados

## 1. Identificación

- Historia de usuario: US-003 — Informar si no hay disponibilidad.
- Clave Jira de la historia: GC03-28.
- Subtarea: GC03-49 — T-014: Preparar prueba determinista sin resultados.
- Responsable: Borja.
- Tiempo estimado: 1 hora.
- Estado de la prueba: Preparada, pendiente de ejecución.

## 2. Objetivo

Preparar una prueba funcional determinista para comprobar que el sistema CityDrive informa correctamente al usuario cuando no existen vehículos disponibles para las fechas seleccionadas y permite modificar la búsqueda.

## 3. Datos de prueba

Se utilizará un conjunto de datos sintéticos y controlados, sin información de clientes reales.

Rango de búsqueda inicial:

- Fecha de inicio: 10/11/2026.
- Fecha de fin: 12/11/2026.

Vehículos de prueba propuestos:

| Vehículo | Situación | Disponibilidad esperada |
|---|---|---|
| V-001 | Reservado del 09/11/2026 al 13/11/2026 | No disponible |
| V-002 | Marcado manualmente como no disponible | No disponible |
| V-003 | Reservado del 10/11/2026 al 14/11/2026 | No disponible |

Con estos datos, ninguno de los vehículos debe aparecer como disponible durante el rango seleccionado.

Los vehículos y reservas son datos propuestos para la futura ejecución; no se han cargado todavía en la aplicación.

## 4. Procedimiento de prueba

1. Preparar el catálogo de pruebas con los tres vehículos indicados.
2. Acceder al formulario de búsqueda de vehículos.
3. Introducir las fechas 10/11/2026 y 12/11/2026.
4. Ejecutar la búsqueda.
5. Comprobar que no aparece ningún vehículo disponible.
6. Verificar que el sistema muestra un mensaje informativo indicando que no hay vehículos disponibles para las fechas seleccionadas.
7. Comprobar que es posible volver al formulario y modificar las fechas.
8. Introducir un nuevo rango válido y repetir la búsqueda.

## 5. Resultados esperados

- US-003-AC-01: Cuando la consulta devuelve cero vehículos, aparece un mensaje informativo visible.
- US-003-AC-02: El mensaje indica explícitamente que no existen vehículos disponibles para las fechas seleccionadas.
- US-003-AC-03: El usuario puede modificar las fechas y ejecutar una nueva búsqueda.
- No se muestran vehículos ocupados o marcados como no disponibles como alternativas válidas.

## 6. Estado y ejecución

La prueba queda documentada con sus datos de entrada, procedimiento y resultados esperados.

La ejecución funcional se realizará cuando estén disponibles la implementación de la búsqueda y el entorno de pruebas.

No se registran resultados de ejecución ni se consideran verificados los criterios de aceptación hasta realizar la prueba sobre la aplicación.