# US-016 — Pruebas de cancelación de reservas

## 1. Identificación

- **Proyecto:** CityDrive.
- **Historia de usuario:** GC03-13 — US-016: Cancelar reserva.
- **Subtarea:** GC03-58 — ST-0164: Probar cancelación de reservas.
- **Responsable:** Borja Gómez Castaño.
- **Fecha de realización:** 05/11/2026.
- **Última ejecución verificada:** 07/11/2026.
- **Actualización de documentación:** 08/11/2026.
- **Estado:** Pruebas ejecutadas y documentadas. Cuatro pruebas superadas y una fallida, con incidencia comunicada al responsable.

## 2. Objetivo

Comprobar mediante pruebas automatizadas que el sistema CityDrive permite cancelar reservas activas y rechaza aquellas que no cumplen las condiciones necesarias para su cancelación.

Se pretende verificar que:

- Una reserva activa puede cancelarse correctamente.
- Una reserva cancelada no puede cancelarse nuevamente.
- Una reserva pendiente no puede cancelarse.
- Una cancelación rechazada no modifica los datos de la reserva.
- Una reserva con referencia vacía se rechaza correctamente.

También se documentan los comportamientos pendientes de revisión y las limitaciones de la implementación disponible.

## 3. Componentes utilizados

Para realizar las pruebas se han utilizado los siguientes archivos:

- `src/citydrive/reservas/cancelacion.py`: implementación de la lógica de cancelación de reservas.
- `tests/test_cancelacion_reservas.py`: pruebas automatizadas desarrolladas para GC03-58.
- `src/services/cancelacion_disponibilidad_service.py`: servicio relacionado con el restablecimiento de disponibilidad del vehículo tras la cancelación.

Las pruebas se han desarrollado en Python utilizando el módulo `unittest`.

Se utilizan objetos de reserva almacenados en memoria, sin modificar la implementación desarrollada por otros integrantes del equipo.

## 4. Descripción de la funcionalidad

La implementación de cancelación utiliza una clase `Reserva` con los siguientes atributos:

| Atributo | Descripción |
|---|---|
| `referencia` | Identificador de la reserva |
| `estado` | Estado actual de la reserva |

El estado inicial de una reserva es `activa`.

La función `cancelar_reserva()` comprueba el estado de la reserva recibida.

Si la reserva está activa, modifica su estado a `cancelada` y devuelve el objeto actualizado.

Si la reserva no está activa, genera una excepción `ValueError` con un mensaje indicando que solo pueden cancelarse reservas activas.

En la versión comprobada, esta función no incluye una validación específica para impedir la cancelación de reservas con referencias vacías.

## 5. Casos de prueba

Se han desarrollado cinco pruebas automatizadas.

| Identificador | Caso de prueba | Resultado |
|---|---|---|
| PT-01 | Cancelar una reserva activa | Correcto |
| PT-02 | Rechazar una reserva ya cancelada | Correcto |
| PT-03 | Rechazar una reserva pendiente | Correcto |
| PT-04 | Conservar los datos tras una cancelación rechazada | Correcto |
| PT-05 | Rechazar una reserva con referencia vacía | Fallido |

### PT-01. Cancelación de una reserva activa

**Objetivo:** comprobar que una reserva activa puede cancelarse correctamente.

**Procedimiento:**

Se crea una reserva con una referencia válida y estado `activa`.

Se ejecuta la función `cancelar_reserva()`.

**Resultado esperado:**

La operación se completa correctamente y el estado de la reserva cambia a `cancelada`.

La referencia de la reserva se conserva.

**Resultado obtenido: CORRECTO.**

La reserva activa se cancela correctamente y mantiene su referencia.

### PT-02. Rechazo de una reserva ya cancelada

**Objetivo:** comprobar que no se puede cancelar dos veces una misma reserva.

**Procedimiento:**

Se utiliza una reserva que ya presenta el estado `cancelada`.

Se intenta ejecutar nuevamente la operación de cancelación.

**Resultado esperado:**

La función genera una excepción `ValueError` y la reserva conserva su estado.

**Resultado obtenido: CORRECTO.**

El sistema rechaza correctamente una segunda cancelación.

### PT-03. Rechazo de una reserva pendiente

**Objetivo:** comprobar que una reserva pendiente no puede cancelarse mediante la función implementada.

**Procedimiento:**

Se crea una reserva con estado `pendiente` y se intenta cancelar.

**Resultado esperado:**

La operación genera una excepción `ValueError` y no modifica el estado de la reserva.

**Resultado obtenido: CORRECTO.**

La cancelación se rechaza sin modificar los datos de la reserva.

### PT-04. Conservación de datos tras una cancelación rechazada

**Objetivo:** comprobar que una operación de cancelación inválida no altera los datos originales.

**Procedimiento:**

Se intenta cancelar una reserva cuyo estado no permite realizar la operación.

Se comprueba la información de la reserva después de producirse la excepción.

**Resultado esperado:**

La operación es rechazada y se conservan los datos originales.

**Resultado obtenido: CORRECTO.**

La reserva mantiene sus datos después del intento de cancelación rechazado.

### PT-05. Rechazo de una referencia vacía

**Objetivo:** comprobar que una reserva con referencia vacía no puede cancelarse.

**Procedimiento:**

Se crea una reserva activa cuya referencia es una cadena vacía.

Se ejecuta la función `cancelar_reserva()` y se comprueba si genera una excepción `ValueError`.

**Resultado esperado:**

La función rechaza la operación y conserva el estado `activa`.

**Resultado obtenido: FALLIDO.**

La función permite cancelar una reserva activa cuya referencia está vacía.

La prueba devuelve el siguiente error:

```text
FAIL: test_rechazar_referencia_vacia

AssertionError: ValueError not raised
```

Este comportamiento se ha identificado como una incidencia de validación y se ha comunicado al responsable de la implementación.

## 6. Ejecución de las pruebas automatizadas

Las pruebas se han ejecutado desde la raíz del proyecto utilizando el siguiente comando:

```powershell
python -m unittest discover -s tests -p "test_cancelacion_reservas.py" -v
```

La última ejecución verificada produjo:

```text
test_cancelar_reserva_activa ... ok
test_conservar_datos_tras_cancelacion_rechazada ... ok
test_rechazar_referencia_vacia ... FAIL
test_rechazar_reserva_cancelada ... ok
test_rechazar_reserva_pendiente ... ok

----------------------------------------------------------------------
Ran 5 tests in 0.005s

FAILED (failures=1)
```

### Resumen de resultados

| Concepto | Resultado |
|---|---|
| Pruebas automatizadas ejecutadas | 5 |
| Pruebas superadas | 4 |
| Pruebas fallidas | 1 |
| Errores de ejecución adicionales | 0 |
| Duración de la última ejecución verificada | 0,005 segundos |
| Resultado global | FAILED |

La ejecución confirma que cuatro casos funcionan según lo esperado y que existe un comportamiento pendiente de revisión relacionado con las referencias vacías.

## 7. Incidencias y limitaciones detectadas

### INC-01. Cancelación de reservas con referencia vacía

**Componente afectado:**

`src/citydrive/reservas/cancelacion.py`

**Descripción:**

La función `cancelar_reserva()` comprueba que el estado sea `activa`, pero no valida que la referencia de la reserva tenga un valor válido.

Por tanto, una reserva activa con una referencia vacía puede cancelarse.

**Resultado de la prueba:**

```text
AssertionError: ValueError not raised
```

**Causa identificada:**

La implementación comprueba el estado de la reserva, pero no realiza una validación específica de su referencia.

**Comunicación de la incidencia:**

La incidencia se ha comunicado a Óscar Peña Tienza mediante un comentario en Jira, en la subtarea **GC03-57 — Implementar lógica de cancelación de reservas**.

**Estado de la incidencia: PENDIENTE DE CORRECCIÓN O ACLARACIÓN.**

La incidencia no se ha ocultado ni se ha eliminado la prueba que la detecta.

### INC-02. Validación de reservas inexistentes

La función `cancelar_reserva()` recibe directamente un objeto `Reserva`.

No realiza una búsqueda de reservas por referencia ni comprueba su existencia en un almacenamiento de reservas.

Por tanto, no se ha podido verificar mediante estas pruebas el flujo completo de cancelación de una referencia inexistente.

Esta comprobación requiere integrar la lógica de cancelación con el mecanismo de consulta o almacenamiento de reservas.

**Estado: PENDIENTE DE VERIFICACIÓN DE INTEGRACIÓN.**

### INC-03. Actualización de disponibilidad del vehículo

Existe una implementación específica para restablecer la disponibilidad de un vehículo después de cancelar una reserva.

Sin embargo, las cinco pruebas automatizadas de GC03-58 se centran en la lógica de cancelación del objeto `Reserva`.

No se ha verificado mediante esta batería de pruebas un flujo completo que conecte la cancelación con el restablecimiento de disponibilidad del vehículo.

**Estado: PENDIENTE DE VERIFICACIÓN DE INTEGRACIÓN.**

## 8. Alcance de las pruebas

Las pruebas automatizadas se han realizado sobre objetos Python almacenados en memoria.

Se ha comprobado el comportamiento de la función de cancelación ante distintos estados de reserva y ante una referencia vacía.

No se han realizado pruebas completas sobre una interfaz de usuario, una base de datos persistente o un flujo integrado de consulta, cancelación y actualización de disponibilidad.

Por tanto, los resultados permiten evaluar la lógica de cancelación implementada, pero no garantizan el funcionamiento completo de US-016 en un entorno de producción.

## 9. Resumen de resultados

| Comprobación | Resultado |
|---|---|
| Cancelación de reserva activa | Correcto |
| Rechazo de reserva ya cancelada | Correcto |
| Rechazo de reserva pendiente | Correcto |
| Conservación de datos ante una cancelación rechazada | Correcto |
| Rechazo de referencia vacía | Fallido |
| Rechazo de referencia inexistente | Pendiente de verificación de integración |
| Liberación de disponibilidad tras cancelar | Pendiente de verificación de integración |

Se ha identificado y registrado una incidencia reproducible que deberá revisarse antes de considerar completamente validada la funcionalidad.

## 10. Conclusión

Se han desarrollado y ejecutado cinco pruebas automatizadas correspondientes a la lógica de cancelación de reservas de CityDrive.

Cuatro pruebas se han superado correctamente, confirmando que las reservas activas pueden cancelarse y que las reservas en estados no permitidos son rechazadas sin modificar sus datos originales.

La quinta prueba ha fallado al comprobar el rechazo de una reserva con referencia vacía. La función permite cancelar dicha reserva, por lo que se ha registrado el comportamiento y se ha comunicado al responsable de la implementación mediante Jira GC03-57.

También quedan pendientes las verificaciones del flujo completo de cancelación relacionadas con la búsqueda de reservas y la actualización de disponibilidad de los vehículos.

**La ejecución y documentación de las pruebas correspondientes a GC03-58 se consideran finalizadas, dejando constancia de los resultados obtenidos y de la incidencia conocida.**

La finalización del trabajo de pruebas no implica que todos los criterios de aceptación de US-016 estén superados. Será necesario corregir o aclarar la validación de referencias vacías, repetir la prueba fallida y completar las verificaciones de integración pendientes.

Los archivos de pruebas y documentación se incorporan al repositorio para conservar las evidencias y facilitar las comprobaciones posteriores.