# US-015 — Pruebas de visualización de reservas

## 1. Identificación

- **Historia de usuario:** GC03-25 — US-015: Visualizar datos de reserva.
- **Subtarea:** GC03-76 — ST-0153: Probar visualización de reservas.
- **Responsable:** Borja Gómez Castaño.
- **Fecha:** 07/11/2026.
- **Resultado:** 8 pruebas automatizadas superadas.

## 2. Objetivo

Comprobar que la información de las reservas se presenta correctamente, mostrando la referencia, el vehículo asociado, las fechas de inicio y fin y el estado actual.

También se comprueba que los datos de distintas reservas no se mezclan, que los cambios se reflejan en consultas posteriores y que la visualización no modifica la información original.

## 3. Componentes utilizados

- `src/views/informacion_reserva.py`: función de presentación de la información de reserva.
- `tests/test_gc03_27.py`: pruebas de presentación existentes.
- `tests/test_gc03_76_visualizacion_reservas.py`: pruebas adicionales de GC03-76.

Las pruebas se han desarrollado en Python utilizando `unittest` y datos ficticios.

No se ha modificado la implementación desarrollada por otros integrantes del equipo.

## 4. Datos de prueba

Se utilizan dos reservas:

| Campo | Reserva 1 | Reserva 2 |
|---|---|---|
| Referencia | RES-001 | RES-002 |
| Vehículo | Toyota Corolla | Ford Focus |
| Fecha de inicio | 2026-11-10 | 2026-11-15 |
| Fecha de fin | 2026-11-12 | 2026-11-20 |
| Estado | confirmada | pendiente |

Estos datos permiten verificar el comportamiento de la función con reservas que contienen información diferente.

## 5. Casos de prueba

| Identificador | Descripción | Resultado |
|---|---|---|
| PT-01 | Visualizar dos reservas diferentes | Correcto |
| PT-02 | Comprobar que las consultas sucesivas no mezclan datos | Correcto |
| PT-03 | Visualizar un estado actualizado | Correcto |
| PT-04 | Visualizar fechas actualizadas | Correcto |
| PT-05 | Evitar mostrar campos adicionales | Correcto |
| PT-06 | Comprobar que la visualización no modifica la reserva | Correcto |
| PT-07 | Rechazar reservas sin campos obligatorios | Correcto |
| PT-08 | Distinguir reservas del mismo vehículo | Correcto |

### PT-01. Visualización de dos reservas

Se presenta la información de dos reservas con referencias, vehículos, fechas y estados diferentes.

**Resultado esperado:** cada resultado contiene exclusivamente los valores correspondientes a su reserva.

**Resultado obtenido:** correcto.

### PT-02. Consultas sucesivas

Se consulta una reserva, después otra diferente y finalmente se vuelve a consultar la primera.

**Resultado esperado:** los datos de la primera reserva permanecen iguales y no se mezclan con los de la segunda.

**Resultado obtenido:** correcto.

### PT-03. Estado actualizado

Se modifica el estado de una reserva de `confirmada` a `cancelada` antes de volver a presentar sus datos.

**Resultado esperado:** se muestra el nuevo estado.

**Resultado obtenido:** correcto.

### PT-04. Fechas actualizadas

Se modifican las fechas de inicio y fin de una reserva.

**Resultado esperado:** la siguiente visualización presenta las fechas actualizadas.

**Resultado obtenido:** correcto.

### PT-05. Campos adicionales

Se añaden a los datos de entrada los campos `cliente` y `precio`.

**Resultado esperado:** la función devuelve únicamente los cinco campos previstos para la visualización.

**Resultado obtenido:** correcto.

### PT-06. Conservación de los datos originales

Se guarda una copia de la reserva antes de realizar la consulta.

**Resultado esperado:** la visualización no modifica el diccionario original.

**Resultado obtenido:** correcto.

### PT-07. Campos obligatorios

Se elimina individualmente cada uno de los cinco campos obligatorios y se intenta presentar la reserva incompleta.

**Resultado esperado:** todas las entradas incompletas producen una excepción `ValueError`.

**Resultado obtenido:** correcto.

### PT-08. Reservas del mismo vehículo

Se utilizan dos reservas con el mismo vehículo, pero diferentes referencias, fechas y estados.

**Resultado esperado:** cada reserva conserva su información y se distingue correctamente de la otra.

**Resultado obtenido:** correcto.

## 6. Ejecución de las pruebas

Se ejecuta el siguiente comando desde la raíz del proyecto:

`python -m unittest discover -s tests -p "test_gc03_76_visualizacion_reservas.py" -v`

Resultado obtenido:

```text
Ran 8 tests in 0.003s

OK
```

| Concepto | Resultado |
|---|---|
| Pruebas ejecutadas | 8 |
| Pruebas superadas | 8 |
| Fallos | 0 |
| Errores | 0 |
| Duración total | 0,003 segundos |

## 7. Relación con las pruebas existentes

El archivo `tests/test_gc03_27.py`, desarrollado previamente por Andrea, contiene cuatro pruebas que verifican la presentación de los datos, las etiquetas y el rechazo de reservas vacías o incompletas.

Las ocho pruebas de GC03-76 complementan esas comprobaciones mediante escenarios con varias reservas, datos actualizados y conservación de la información.

## 8. Alcance y limitaciones

Las pruebas se realizan directamente sobre la función `definir_informacion_reserva()`, utilizando diccionarios Python.

La función recibe una reserva como parámetro y devuelve un diccionario con cinco etiquetas descriptivas.

Por tanto, estas pruebas verifican la preparación de los datos para su presentación, pero no comprueban una interfaz gráfica ni la recuperación de reservas desde una base de datos.

Tampoco se prueba el proceso completo de búsqueda de una reserva por referencia, ya que dicho proceso no forma parte de la función utilizada.

## 9. Conclusiones

Las ocho pruebas automatizadas de GC03-76 se han ejecutado satisfactoriamente.

Se ha comprobado que la función presenta correctamente los datos de las reservas, conserva la separación entre distintas consultas y refleja las modificaciones de fechas y estados.

Asimismo, se ha verificado que la presentación no altera los datos originales y rechaza reservas incompletas.

**La lógica de preparación de datos para la visualización queda validada en los escenarios probados**, con las limitaciones indicadas respecto a la interfaz y al proceso de búsqueda por referencia.