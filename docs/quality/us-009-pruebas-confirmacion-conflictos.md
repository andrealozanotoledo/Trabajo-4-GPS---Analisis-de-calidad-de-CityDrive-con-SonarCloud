# US-009 — Pruebas de confirmación y conflictos

## 1. Identificación

- **Historia de usuario:** GC03-79 — US-009: Confirmar reserva.
- **Subtarea:** GC03-81 — ST-0092: Probar confirmación y conflictos.
- **Responsable:** Borja Gómez Castaño.
- **Estimación:** 2 horas.
- **Fecha de ejecución:** 07/11/2026.
- **Estado:** Pruebas automatizadas del servicio superadas.

## 2. Objetivo

Verificar que CityDrive permite confirmar reservas válidas y rechaza aquellas que generan conflictos de disponibilidad.

También se comprueba que el sistema revalida la disponibilidad antes de registrar una reserva, conserva las reservas anteriores cuando existe un conflicto y valida los datos obligatorios de la operación.

Las pruebas se realizan con datos ficticios y escenarios controlados, sobre la implementación Python del servicio de confirmación.

## 3. Componentes utilizados

Se han utilizado los siguientes archivos:

- `src/models/confirmacion_reserva.py`: modelo de los datos de confirmación.
- `src/services/confirmacion_service.py`: confirmación, registro y revalidación de reservas.
- `tests/test_confirmacion_conflictos.py`: pruebas automatizadas de la subtarea.

Se ha utilizado el módulo `unittest` de Python.

El servicio mantiene los registros de reservas confirmadas en una lista en memoria. Las pruebas restablecen los datos antes de cada ejecución para evitar interferencias entre casos.

## 4. Datos de prueba

Se han utilizado los siguientes datos ficticios:

- **Vehículos:** VEH-101, VEH-102 y VEH-104.
- **Clientes:** CLI-10.
- **Referencias de reserva:** RES-1001 y RES-1002.
- **Importe inicial:** 150,00 €.
- **Periodo inicial:** del 01/12/2026 al 05/12/2026.

Estados iniciales:

| Vehículo | Estado |
|---|---|
| VEH-101 | DISPONIBLE |
| VEH-102 | NO DISPONIBLE |
| VEH-104 | DISPONIBLE |

Los identificadores, fechas y estados se modifican en determinados casos para comprobar diferentes comportamientos.

## 5. Pruebas automatizadas realizadas

| Caso | Descripción | Resultado |
|---|---|---|
| PT-01 | Confirmación correcta de una reserva | Correcto |
| PT-02 | Rechazo de fechas solapadas | Correcto |
| PT-03 | Rechazo de vehículo no disponible | Correcto |
| PT-04 | Registro de reservas sin solapamiento | Correcto |
| PT-05 | Reservas de vehículos diferentes | Correcto |
| PT-06 | Conservación de una reserva ante un conflicto | Correcto |
| PT-07 | Rechazo de datos obligatorios ausentes | Correcto |
| PT-08 | Rechazo de importe no válido | Correcto |
| PT-09 | Revalidación ante un conflicto de fechas | Correcto |
| PT-10 | Revalidación ante un cambio de disponibilidad | Correcto |

### PT-01. Confirmación correcta

Se registra una reserva válida del vehículo VEH-101.

Se comprueba que:

- La operación devuelve el estado `CONFIRMADA`.
- Se genera el identificador `CONF-0001`.
- La referencia de la reserva es `RES-1001`.
- El registro aparece en la lista de reservas confirmadas.

**Resultado: CORRECTO.**

### PT-02. Conflicto por fechas solapadas

Se registra una reserva del vehículo VEH-101 del 01/12/2026 al 05/12/2026.

Posteriormente, se intenta confirmar otra reserva del mismo vehículo del 03/12/2026 al 07/12/2026.

**Resultado esperado:** rechazar la segunda reserva mediante una excepción por conflicto.

**Resultado obtenido: CORRECTO.**

### PT-03. Vehículo no disponible

Se intenta confirmar una reserva del vehículo VEH-102, cuyo estado es `NO DISPONIBLE`.

Se comprueba que la confirmación se rechaza y no se registra ninguna reserva.

**Resultado: CORRECTO.**

### PT-04. Reservas sin solapamiento

Se confirma una reserva del VEH-101 del 01/12/2026 al 05/12/2026.

Posteriormente, se registra otra reserva del mismo vehículo del 06/12/2026 al 09/12/2026.

Se comprueba que ambas reservas quedan confirmadas.

**Resultado: CORRECTO.**

### PT-05. Reservas de vehículos diferentes

Se registran dos reservas para VEH-101 y VEH-104 con fechas coincidentes.

Al tratarse de vehículos diferentes, ambas operaciones deben aceptarse.

**Resultado: CORRECTO.**

### PT-06. Conservación de reservas anteriores

Se registra una reserva válida y posteriormente se intenta registrar otra incompatible.

Se verifica que:

- La nueva reserva se rechaza.
- La lista conserva únicamente la reserva original.
- Los datos originales no se modifican.

**Resultado: CORRECTO.**

### PT-07. Dato obligatorio ausente

Se intenta confirmar una reserva sin indicar el identificador del cliente.

El servicio debe rechazar la operación mediante una excepción `ValueError`.

**Resultado: CORRECTO.**

### PT-08. Importe no válido

Se intenta confirmar una reserva con importe total igual a cero.

Se comprueba que el servicio rechaza la operación y no registra la reserva.

**Resultado: CORRECTO.**

### PT-09. Revalidación ante un conflicto

Después de confirmar una reserva, se ejecuta una nueva comprobación de disponibilidad para el mismo vehículo y un periodo solapado.

La función `revalidar_disponibilidad()` devuelve `False`.

**Resultado: CORRECTO.**

### PT-10. Revalidación ante un cambio de estado

Se modifica el estado del vehículo VEH-101 a `NO DISPONIBLE`.

Posteriormente, se ejecuta `revalidar_disponibilidad()`.

La función devuelve `False`, impidiendo que el vehículo se considere disponible.

**Resultado: CORRECTO.**

## 6. Ejecución de las pruebas

Comando utilizado desde la raíz del proyecto:

`python -m unittest discover -s tests -p "test_confirmacion_conflictos.py" -v`

Resultado obtenido:

```text
test_confirmacion_correcta ... ok
test_conflicto_no_modifica_reserva_anterior ... ok
test_rechazo_dato_obligatorio_ausente ... ok
test_rechazo_importe_no_valido ... ok
test_rechazo_por_fechas_solapadas ... ok
test_rechazo_vehiculo_no_disponible ... ok
test_reservas_de_vehiculos_diferentes ... ok
test_reservas_sin_solapamiento ... ok
test_revalidacion_detecta_cambio_estado ... ok
test_revalidacion_detecta_conflicto ... ok

----------------------------------------------------------------------
Ran 10 tests in 0.009s

OK
```

Resumen:

| Concepto | Resultado |
|---|---|
| Pruebas ejecutadas | 10 |
| Pruebas superadas | 10 |
| Fallos | 0 |
| Errores | 0 |
| Duración total del conjunto | 0,009 segundos |
| Resultado global | OK |

## 7. Limitaciones de las pruebas

Las pruebas se han ejecutado directamente sobre el servicio Python, utilizando datos ficticios y registros en memoria.

Por tanto, se han verificado los comportamientos de confirmación, revalidación y rechazo de conflictos, pero existen aspectos que no se han comprobado:

- **Confirmaciones simultáneas:** no se ha ejecutado una prueba con solicitudes concurrentes reales. No puede afirmarse que el servicio garantice atomicidad ante dos confirmaciones simultáneas.
- **Interfaz:** no se ha verificado la presentación de mensajes al usuario ni el retorno a la búsqueda después de un conflicto.
- **Base de datos:** no se ha probado el almacenamiento persistente de las reservas.
- **Rendimiento:** no se ha medido individualmente el tiempo de respuesta de la confirmación. Los 0,009 segundos corresponden a la duración total de las diez pruebas automatizadas.

Estas comprobaciones quedan pendientes para las pruebas de integración, concurrencia o rendimiento que correspondan.

## 8. Criterios relacionados

Las pruebas realizadas están relacionadas con los criterios de aceptación de:

- US-009: Confirmar reserva.
- US-012: Evitar reservas solapadas.
- US-013: Informar de cambios de disponibilidad.

Los resultados verifican los escenarios implementados en el servicio, pero no representan una validación completa de todos los criterios de aceptación de estas historias.

## 9. Conclusión

Se han ejecutado diez pruebas automatizadas, todas con resultado correcto.

Se ha comprobado que el servicio permite registrar reservas válidas, rechaza conflictos por solapamiento, detecta vehículos no disponibles y conserva los datos de las reservas anteriores cuando se intenta una confirmación incompatible.

Asimismo, se ha verificado la validación de datos obligatorios, la comprobación del importe y la revalidación de disponibilidad.

**Las pruebas funcionales del servicio correspondientes a GC03-81 han sido superadas**, quedando documentadas las limitaciones relacionadas con concurrencia, interfaz, persistencia y rendimiento.