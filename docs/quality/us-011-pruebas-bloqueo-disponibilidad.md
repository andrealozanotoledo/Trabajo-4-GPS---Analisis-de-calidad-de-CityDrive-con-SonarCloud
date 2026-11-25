# US-011 — Pruebas de bloqueo y disponibilidad

## 1. Identificación

- **Historia de usuario:** GC03-86 — US-011: Bloquear vehículo reservado.
- **Subtarea:** GC03-88 — ST-0112: Probar bloqueo y disponibilidad.
- **Responsable:** Borja Gómez Castaño.
- **Fecha de ejecución:** 05/11/2026.
- **Tiempo estimado:** 2 horas.

## 2. Objetivo

Verificar que el sistema bloquea un vehículo durante las fechas correspondientes a una reserva confirmada, rechaza solicitudes con períodos incompatibles y permite consultar su disponibilidad fuera del intervalo reservado.

También se comprueba que las reservas no confirmadas no generan bloqueos.

## 3. Entorno y componentes utilizados

Las pruebas se han realizado localmente con Python, utilizando la implementación de la rama `feature/GC03-86-us-011-bloquear-vehiculo-reservado`.

Archivos utilizados:

- `src/models/bloqueo_vehiculo.py`
- `src/services/bloqueo_service.py`
- `tests/test_bloqueo_disponibilidad.py`

La implementación del servicio almacena los bloqueos en memoria mediante `_HISTORIAL_BLOQUEOS`.

Vehículos de prueba:

- `VEH-01`: Disponible.
- `VEH-02`: Disponible.
- `VEH-03`: En mantenimiento.

## 4. Pruebas realizadas

### PT-01. Bloqueo de una reserva confirmada

Se crea una reserva confirmada para el vehículo `VEH-01`, del 01/12/2026 al 05/12/2026.

Se comprueba que el bloqueo se registra correctamente y que el vehículo deja de estar disponible dentro de ese intervalo.

**Resultado: CORRECTO.**

### PT-02. Rechazo de fechas solapadas

Se bloquea `VEH-01` del 01/12/2026 al 05/12/2026 y se intenta realizar otro bloqueo del 03/12/2026 al 08/12/2026.

El servicio rechaza la segunda operación mediante una excepción `ValueError`.

Se comprueba que el historial conserva únicamente el bloqueo original.

**Resultado: CORRECTO.**

### PT-03. Disponibilidad en fechas diferentes

Después de bloquear `VEH-01` del 01/12/2026 al 05/12/2026, se registra otro bloqueo del 10/12/2026 al 15/12/2026.

El servicio permite la operación porque los intervalos no se solapan.

**Resultado: CORRECTO.**

### PT-04. Rechazo de una reserva no confirmada

Se intenta bloquear `VEH-01` utilizando una reserva con estado `RECHAZADA`.

El servicio rechaza la operación y se comprueba que no se añade ningún bloqueo al historial.

**Resultado: CORRECTO.**

### PT-05. Vehículo en mantenimiento

Se intenta bloquear `VEH-03`, cuyo estado es `MANTENIMIENTO`.

El servicio rechaza correctamente la operación mediante una excepción `ValueError`.

**Resultado: CORRECTO.**

### PT-06. Comprobación de fechas límite

Se bloquea `VEH-01` del 01/12/2026 al 05/12/2026.

Se comprueba que el día 05/12/2026 sigue ocupado, mientras que una reserva que comienza el 06/12/2026 no presenta conflicto.

**Resultado: CORRECTO.**

### PT-07. Independencia entre vehículos

Se bloquea `VEH-01` durante un intervalo determinado y se consulta la disponibilidad de `VEH-02` para esas mismas fechas.

Se comprueba que el bloqueo de un vehículo no afecta a la disponibilidad del otro.

**Resultado: CORRECTO.**

## 5. Ejecución de las pruebas automatizadas

Se ha utilizado el siguiente comando:

```powershell
python -m unittest discover -s tests -p "test_bloqueo_disponibilidad.py" -v
```

Resultado obtenido:

```text
Ran 7 tests in 0.006s

OK
```

**Resumen de resultados:**

- Pruebas ejecutadas: 7.
- Pruebas superadas: 7.
- Fallos: 0.
- Errores: 0.

## 6. Verificación de los criterios de aceptación

| Criterio | Resultado |
|---|---|
| AC-01. Bloqueo durante las fechas de una reserva confirmada | Superado a nivel de servicio |
| AC-02. Rechazo de disponibilidad para fechas incompatibles | Superado a nivel de servicio |
| AC-03. Bloqueo limitado al intervalo reservado | Superado a nivel de servicio |
| AC-04. Solo las reservas confirmadas provocan bloqueos | Superado a nivel de servicio |

## 7. Limitaciones

Las pruebas verifican el funcionamiento del servicio y de su historial de bloqueos en memoria.

No se ha comprobado todavía la integración completa con la confirmación y el almacenamiento persistente de reservas, ni con la interfaz de búsqueda de vehículos.

Por tanto, los resultados obtenidos no deben interpretarse como una validación de extremo a extremo del sistema completo.

## 8. Conclusión

Se han ejecutado siete pruebas automatizadas de bloqueo y disponibilidad, todas con resultado correcto.

El servicio impide bloqueos con fechas incompatibles, respeta los límites temporales de las reservas y evita generar bloqueos para reservas no confirmadas.

Con estos resultados queda verificado el comportamiento del servicio correspondiente a la subtarea GC03-88. Las pruebas de integración del flujo completo deberán abordarse cuando estén disponibles los componentes correspondientes.