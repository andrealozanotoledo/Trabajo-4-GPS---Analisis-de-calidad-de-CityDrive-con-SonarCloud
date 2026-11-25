# US-002 — Pruebas de resultados de disponibilidad

## 1. Identificación

- Historia de usuario: GC03-102 — US-002: Consultar vehículos disponibles.
- Subtarea: GC03-105 — ST-0023: Probar resultados de disponibilidad.
- Responsable: Borja Gómez Castaño.
- Tiempo estimado: 2 horas.
- Estado: Pruebas de la subtarea ejecutadas correctamente.

## 2. Objetivo

Comprobar que CityDrive presenta correctamente los resultados de una búsqueda de vehículos disponibles y excluye aquellos que tengan reservas incompatibles o estén marcados como no disponibles.

Las pruebas se han realizado con datos ficticios y escenarios controlados, utilizando las funciones implementadas en Python.

## 3. Archivos utilizados

- `disponibilidad.py`: consulta y filtrado de vehículos según fechas, reservas y estado.
- `fechas.py`: definición y validación del rango de fechas.
- `presentacion_resultados.py`: presentación textual de los vehículos encontrados.

## 4. Casos de prueba ejecutados

### CP-01. Búsqueda sin resultados

**Entrada:** Lista vacía de vehículos.

**Resultado esperado:** Mostrar un mensaje indicando que no existen vehículos disponibles para las fechas seleccionadas.

**Resultado obtenido:**

No existen vehículos disponibles para las fechas seleccionadas.

**Estado: CORRECTO.**

### CP-02. Presentación de varios vehículos

**Datos de entrada:**

- V-001 — Toyota Corolla — Coche.
- V-002 — Ford Transit — Furgoneta.

**Resultado esperado:** Mostrar los vehículos recibidos con su marca, modelo, tipo e identificador.

**Resultado obtenido:**

Vehículos disponibles:

Toyota Corolla (Coche) - ID: V-001

Ford Transit (Furgoneta) - ID: V-002

**Estado: CORRECTO.**

### CP-03. Exclusión de un vehículo con reserva incompatible

**Datos de entrada:**

- Vehículo: VEH-01 — Toyota Corolla.
- Reserva activa: del 10/11/2026 al 12/11/2026.
- Rango consultado: del 11/11/2026 al 14/11/2026.

**Resultado esperado:** El vehículo no debe aparecer disponible porque las fechas se solapan.

**Resultado obtenido:**

`[]`

La comprobación automática mostró `PRUEBA SUPERADA`.

**Estado: CORRECTO.**

### CP-04. Exclusión de un vehículo en mantenimiento

**Datos de entrada:**

- Vehículo: VEH-03 — Ford Focus.
- Estado: mantenimiento.
- Rango consultado: del 11/11/2026 al 14/11/2026.
- Reservas existentes: ninguna.

**Resultado esperado:** El vehículo no debe aparecer disponible porque su estado no permite reservarlo.

**Resultado obtenido:**

`[]`

La comprobación automática mostró `PRUEBA SUPERADA`.

**Estado: CORRECTO.**

### CP-05. Disponibilidad fuera del periodo reservado

**Datos de entrada:**

- Vehículo: VEH-01 — Toyota Corolla.
- Reserva activa: del 10/11/2026 al 12/11/2026.
- Rango consultado: del 13/11/2026 al 15/11/2026.

**Resultado esperado:** El vehículo debe aparecer disponible porque no existe solapamiento entre los intervalos.

**Resultado obtenido:** Se devolvió VEH-01 con estado disponible.

La comprobación automática mostró `PRUEBA SUPERADA`.

**Estado: CORRECTO.**

### CP-06. Filtrado combinado de varios vehículos

**Datos de entrada:**

- VEH-01 — Toyota Corolla: reserva activa del 10/11/2026 al 12/11/2026.
- VEH-02 — Ford Focus: disponible y sin reservas.
- VEH-03 — Seat Ibiza: en mantenimiento.
- Rango consultado: del 11/11/2026 al 14/11/2026.

**Resultado esperado:** Mostrar únicamente VEH-02, excluyendo VEH-01 por solapamiento y VEH-03 por mantenimiento.

**Resultado obtenido:** La función devolvió exclusivamente VEH-02.

La comprobación automática mostró `PRUEBA SUPERADA`.

**Estado: CORRECTO.**

## 5. Resumen de resultados

| Caso | Descripción | Resultado |
|---|---|---|
| CP-01 | Mensaje cuando no hay resultados | Correcto |
| CP-02 | Presentación de varios vehículos | Correcto |
| CP-03 | Exclusión por reserva incompatible | Correcto |
| CP-04 | Exclusión por mantenimiento | Correcto |
| CP-05 | Disponibilidad fuera de las fechas reservadas | Correcto |
| CP-06 | Filtrado combinado de vehículos | Correcto |

**Total: 6 pruebas ejecutadas, 6 superadas y 0 fallidas.**

## 6. Observaciones

Las pruebas se han ejecutado directamente sobre las funciones Python mediante comandos en terminal y datos sintéticos.

Para verificar los resultados del filtrado se han utilizado comprobaciones automáticas con `assert`, que finalizaron correctamente.

Estas pruebas validan el comportamiento de las funciones de presentación y consulta de disponibilidad en los escenarios definidos.

No se ha medido el tiempo de respuesta ni se ha realizado una prueba completa de extremo a extremo con una base de datos. Estas comprobaciones requieren pruebas adicionales de integración y rendimiento.

## 7. Conclusión

Los seis casos ejecutados han obtenido los resultados esperados.

Se ha comprobado que las funciones permiten presentar vehículos disponibles, informar cuando no existen resultados y excluir vehículos con reservas incompatibles o estados que impiden su reserva.

También se ha verificado que un vehículo puede aparecer disponible cuando su reserva corresponde a un periodo distinto al solicitado.

Con estos resultados se consideran superadas las pruebas funcionales definidas para la subtarea GC03-105, dentro del alcance de las funciones y los datos sintéticos utilizados.