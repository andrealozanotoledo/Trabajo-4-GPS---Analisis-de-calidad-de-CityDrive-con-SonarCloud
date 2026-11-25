# US-013 — Pruebas de cambio de disponibilidad

## 1. Identificación

- **Historia de usuario:** GC03-42 — US-013: Informar de cambios de disponibilidad durante la reserva.
- **Subtarea:** GC03-97 — ST-0133: Probar cambio de disponibilidad.
- **Responsable:** Borja Gómez Castaño.
- **Fecha de ejecución:** 05/11/2026.
- **Estado:** Pruebas del servicio ejecutadas correctamente.

## 2. Objetivo

Comprobar que CityDrive detecta cuando un vehículo deja de estar disponible, informa al cliente y rechaza una solicitud de reserva incompatible sin registrarla.

También se verifica que una solicitud válida puede registrarse y que el rechazo de una nueva solicitud no modifica las reservas registradas anteriormente.

## 3. Entorno y componentes utilizados

Las pruebas se han ejecutado localmente mediante Python, utilizando los siguientes archivos:

- `src/models/aviso.py`
- `src/services/notificacion_service.py`
- `tests/test_cambio_disponibilidad.py`

Se ha utilizado la implementación correspondiente al commit `022e90c` de GC03-98.

El servicio mantiene en memoria los estados de los vehículos, los avisos generados y las reservas registradas.

## 4. Datos de prueba

Se han utilizado los siguientes identificadores ficticios:

- **Vehículos:** VEH-01 y VEH-02.
- **Clientes:** CLI-10 y CLI-20.
- **Reservas:** RES-100, RES-101, RES-102 y RES-103.

Los estados de disponibilidad utilizados han sido `DISPONIBLE` y `NO DISPONIBLE`.

Las pruebas automatizadas restablecen los datos en memoria antes de cada ejecución para evitar que unas pruebas afecten a otras.

## 5. Pruebas automatizadas realizadas

### PT-01. Generación de aviso de cambio de disponibilidad

Se modifica la disponibilidad de `VEH-01` a `NO DISPONIBLE` para el cliente `CLI-10`.

Se comprueba que el aviso generado contiene el identificador `AVIS-0001`, el vehículo y el cliente correspondientes, y un mensaje que informa del nuevo estado.

**Resultado: CORRECTO.**

### PT-02. Rechazo de una solicitud incompatible

Se modifica el estado de `VEH-01` a `NO DISPONIBLE` y se intenta validar una solicitud de reserva.

El servicio lanza una excepción `ValueError` indicando que la reserva es incompatible.

**Resultado: CORRECTO.**

### PT-03. Validación de un vehículo disponible

Se comprueba la disponibilidad de `VEH-01` cuando su estado es `DISPONIBLE`.

El servicio devuelve `DISPONIBLE_CONFIRMADO` junto con el identificador del vehículo.

**Resultado: CORRECTO.**

### PT-04. Generación de avisos independientes

Se generan dos avisos para vehículos y clientes diferentes.

Se comprueba que reciben los identificadores `AVIS-0001` y `AVIS-0002`, contienen los clientes correspondientes y presentan fechas válidas.

**Resultado: CORRECTO.**

### PT-05. Rechazo de una reserva incompatible sin registrarla

Se modifica el estado de `VEH-01` a `NO DISPONIBLE` y se intenta registrar la reserva `RES-101`.

Se comprueba que:

- La función rechaza la operación mediante `ValueError`.
- La reserva no se añade al registro en memoria.
- La lista de reservas registradas permanece vacía.

**Resultado: CORRECTO.**

### PT-06. Registro de una reserva válida

Se intenta registrar la reserva `RES-102` para `VEH-01` cuando el vehículo está disponible.

Se comprueba que:

- La operación devuelve `REGISTRADA`.
- La reserva aparece en el registro en memoria.
- Se conservan los identificadores correctos.
- La reserva queda con estado `CONFIRMADA`.

**Resultado: CORRECTO.**

### PT-07. Conservación de una reserva anterior ante un conflicto

Se registra inicialmente la reserva `RES-100` para `VEH-01`.

Posteriormente, el vehículo pasa a `NO DISPONIBLE` y se intenta registrar una nueva reserva, `RES-103`.

Se comprueba que:

- La segunda solicitud se rechaza.
- El historial conserva únicamente la reserva original.
- Los datos de `RES-100` permanecen sin modificaciones.

**Resultado: CORRECTO.**

## 6. Ejecución de las pruebas

Se ha utilizado el siguiente comando desde la raíz del proyecto:

```powershell
python -m unittest discover -s tests -p "test_cambio_disponibilidad.py" -v
```

Resultado obtenido:

```text
test_avisos_independientes ... ok
test_generar_aviso ... ok
test_rechazar_solicitud_incompatible ... ok
test_rechazo_conserva_reserva_anterior ... ok
test_reserva_incompatible_no_registrada ... ok
test_reserva_valida_registrada ... ok
test_validar_vehiculo_disponible ... ok

----------------------------------------------------------------------
Ran 7 tests in 0.002s

OK
```

**Resumen de ejecución:**

| Concepto | Resultado |
|---|---|
| Pruebas automatizadas ejecutadas | 7 |
| Pruebas superadas | 7 |
| Pruebas fallidas | 0 |
| Errores | 0 |
| Tiempo total | 0,002 segundos |
| Resultado global | OK |

Anteriormente también se habían realizado seis comprobaciones directas mediante comandos Python, todas con los resultados esperados.

## 7. Limitaciones

La implementación utiliza estructuras de datos en memoria para gestionar los estados de los vehículos, los avisos y las reservas.

Por tanto, las pruebas verifican que el servicio no añade reservas incompatibles a su registro en memoria, pero no comprueban el almacenamiento persistente en una base de datos.

Tampoco se han ejecutado pruebas completas desde la interfaz de CityDrive para verificar el retorno a la selección de fechas, la conservación de los filtros o la presentación del aviso durante la navegación.

Las pruebas tampoco verifican concurrencia entre solicitudes simultáneas.

Estas comprobaciones deberán realizarse durante la integración del flujo completo de reservas.

## 8. Conclusión

Se han ejecutado siete pruebas automatizadas del servicio de cambio de disponibilidad, todas con resultado correcto.

Los resultados confirman que el servicio genera avisos, detecta vehículos no disponibles, rechaza solicitudes incompatibles sin añadirlas al registro en memoria y conserva las reservas anteriores cuando se produce un conflicto.

Asimismo, se ha comprobado que una reserva válida puede registrarse correctamente.

Con los resultados obtenidos queda verificado el comportamiento del servicio correspondiente a GC03-97, dejando documentadas las limitaciones relacionadas con la integración completa del sistema.