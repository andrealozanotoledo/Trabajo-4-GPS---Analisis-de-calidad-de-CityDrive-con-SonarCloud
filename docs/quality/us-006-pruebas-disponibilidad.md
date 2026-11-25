# US-006 — Pruebas funcionales de disponibilidad y rendimiento

## 1. Identificación

- **Historia de usuario:** GC03-66 — US-006: Visualizar la disponibilidad del vehículo seleccionado.
- **Subtarea:** GC03-69 — Pruebas funcionales de disponibilidad y validación del rendimiento.
- **Fecha:** 05/11/2026.
- **Estado:** Pruebas automatizadas de la lógica de disponibilidad superadas.

## 2. Objetivo

Verificar que la comprobación individual de disponibilidad distingue correctamente entre vehículos disponibles, vehículos con reservas activas solapadas y vehículos inactivos.

También se comprueba que el tiempo de ejecución de la consulta es inferior a dos segundos en el entorno local.

## 3. Componentes utilizados

Se han utilizado los siguientes archivos del proyecto:

- `disponibilidad.py`: definición de vehículos, reservas y comprobación de solapamientos.
- `disponibilidad_individual.py`: función de comprobación individual de disponibilidad.
- `fechas.py`: definición y validación del rango de fechas.
- `tests/test_disponibilidad_individual.py`: pruebas automatizadas de la subtarea.

Las pruebas se ejecutan mediante `unittest`, utilizando datos ficticios y sin modificar el código de implementación de los compañeros.

## 4. Casos de prueba

| Caso | Descripción | Resultado |
|---|---|---|
| PT-01 | Vehículo disponible sin reservas | Correcto |
| PT-02 | Reserva activa con fechas solapadas | Correcto |
| PT-03 | Vehículo inactivo | Correcto |
| PT-04 | Reserva fuera del rango solicitado | Correcto |
| PT-05 | Reserva cancelada que no bloquea la disponibilidad | Correcto |
| PT-06 | Reserva de otro vehículo que no afecta a la consulta | Correcto |
| PT-07 | Rechazo de un rango de fechas inválido | Correcto |
| PT-08 | Tiempo de respuesta inferior a dos segundos | Correcto |

### 4.1. Vehículo disponible

Se realiza la consulta sobre un vehículo operativo sin reservas.

**Resultado esperado:** el servicio devuelve `True`.

**Resultado obtenido:** correcto.

### 4.2. Reserva activa con solapamiento

Se introduce una reserva activa cuyo periodo coincide parcialmente con las fechas solicitadas.

**Resultado esperado:** el servicio devuelve `False`.

**Resultado obtenido:** correcto.

### 4.3. Vehículo inactivo

Se modifica el estado del vehículo a `inactivo`.

**Resultado esperado:** el servicio devuelve `False`.

**Resultado obtenido:** correcto.

### 4.4. Reservas no incompatibles

Se comprueba que una reserva fuera del intervalo, una reserva cancelada y una reserva correspondiente a otro vehículo no bloquean la disponibilidad.

**Resultado esperado:** el servicio devuelve `True` en los tres casos.

**Resultado obtenido:** correcto.

### 4.5. Validación de fechas

Se introduce un rango con fecha de fin anterior a la fecha de inicio.

**Resultado esperado:** el servicio lanza una excepción `ValueError`.

**Resultado obtenido:** correcto.

### 4.6. Rendimiento

Se realiza una comprobación individual utilizando una colección de 1000 reservas pertenecientes a otros vehículos.

Se mide el tiempo de ejecución con `perf_counter()` y se verifica que sea inferior a dos segundos.

**Resultado esperado:** consulta completada en menos de dos segundos.

**Resultado obtenido:** correcto.

## 5. Ejecución

Comando utilizado:

```powershell
python -m unittest discover -s tests -p "test_disponibilidad_individual.py" -v
```

Resultado:

```text
Ran 8 tests in 0.003s

OK
```

Las ocho pruebas finalizaron correctamente, sin fallos ni errores.

## 6. Limitaciones

Las pruebas verifican directamente la función Python `comprobar_disponibilidad_vehiculo()`, por lo que los resultados corresponden a la lógica del servicio.

La prueba de rendimiento mide una ejecución local de dicha función. El tiempo total de 0,003 segundos corresponde al conjunto de pruebas y no debe interpretarse como el tiempo de carga de la interfaz.

No se ha verificado todavía la representación visual del indicador de disponibilidad, ya que los archivos `src/models/indicador_disponibilidad.py` y `src/services/indicador_disponibilidad_service.py` están vacíos en la versión revisada.

Por tanto, la validación de la integración visual completa queda pendiente.

## 7. Conclusión

Se han ejecutado ocho pruebas automatizadas, todas con resultado correcto.

La implementación comprueba correctamente la disponibilidad individual en los escenarios analizados, teniendo en cuenta el estado operativo del vehículo, las reservas activas y el rango de fechas.

También supera la comprobación local de rendimiento inferior a dos segundos.

Queda validado el comportamiento de la lógica de disponibilidad en los casos probados, con la limitación de que la integración visual todavía no ha sido verificada.