# US-020 — Pruebas de modificación manual de disponibilidad

## 1. Identificación

- **Historia de usuario:** GC03-34 — US-020: Modificar disponibilidad manual.
- **Subtarea:** GC03-77 — ST-0203: Probar disponibilidad manual.
- **Responsable:** Borja Gómez Castaño.
- **Fecha:** 07/11/2026.
- **Resultado:** Pruebas unitarias del servicio superadas.

## 2. Objetivo

Comprobar que el sistema CityDrive permite modificar manualmente el estado operativo de los vehículos, validando los estados permitidos y conservando correctamente los datos de cada vehículo.

Se comprueba también que los cambios se reflejan en consultas posteriores y que las operaciones inválidas no modifican el estado almacenado.

## 3. Componentes utilizados

- `src/citydrive/models/vehiculo.py`: modelo de vehículo.
- `src/citydrive/services/catalogo.py`: servicio que registra vehículos y modifica su estado operativo.
- `tests/test_gc03_77_disponibilidad_manual.py`: pruebas automatizadas desarrolladas para GC03-77.

Las pruebas se ejecutan mediante Python y `unittest`, utilizando vehículos ficticios registrados en memoria.

## 4. Datos de prueba

Se utilizan dos vehículos:

| Campo | Vehículo 1 | Vehículo 2 |
|---|---|---|
| Marca | Toyota | Ford |
| Modelo | Corolla | Transit |
| Categoría | COCHE | FURGONETA |
| Plazas | 5 | 3 |
| Capacidad de carga | 400 litros | 1000 kg |
| Transmisión | Manual | Automática |
| Estado inicial | disponible | disponible |

Cada vehículo dispone de un identificador generado automáticamente.

## 5. Casos de prueba

| Identificador | Prueba realizada | Resultado |
|---|---|---|
| PT-01 | Comprobar el estado inicial disponible | Correcto |
| PT-02 | Cambiar un vehículo a no disponible | Correcto |
| PT-03 | Volver a establecer el estado disponible | Correcto |
| PT-04 | Consultar el estado actualizado | Correcto |
| PT-05 | Rechazar un identificador inexistente | Correcto |
| PT-06 | Rechazar estados no permitidos | Correcto |
| PT-07 | Mantener el estado anterior tras un error | Correcto |
| PT-08 | Comprobar que otro vehículo no resulta afectado | Correcto |
| PT-09 | Conservar los datos del vehículo al cambiar su estado | Correcto |

### PT-01. Estado inicial

Se comprueba que los vehículos recién registrados presentan el estado `disponible`.

**Resultado:** correcto.

### PT-02. Cambio a no disponible

Se modifica el estado de un vehículo mediante `cambiar_estado_vehiculo()`.

**Resultado esperado:** el vehículo pasa a `no disponible`.

**Resultado:** correcto.

### PT-03. Restauración de disponibilidad

Se cambia un vehículo a `no disponible` y posteriormente a `disponible`.

**Resultado esperado:** el vehículo recupera el estado disponible.

**Resultado:** correcto.

### PT-04. Consulta posterior

Después de modificar la disponibilidad, se consulta el catálogo mediante `obtener_vehiculos()`.

**Resultado esperado:** aparece el estado operativo actualizado.

**Resultado:** correcto.

### PT-05. Vehículo inexistente

Se intenta modificar la disponibilidad de un identificador que no existe.

**Resultado esperado:** se produce una excepción `ValueError`.

**Resultado:** correcto.

### PT-06. Estado inválido

Se intenta asignar el estado `mantenimiento` y una cadena vacía.

**Resultado esperado:** ambos valores son rechazados mediante `ValueError`.

**Resultado:** correcto.

### PT-07. Conservación del estado tras un error

Se establece el estado `no disponible` y posteriormente se intenta asignar el valor inválido `averiado`.

**Resultado esperado:** se rechaza el cambio y el vehículo permanece como `no disponible`.

**Resultado:** correcto.

### PT-08. Independencia de los vehículos

Se modifica la disponibilidad del Toyota Corolla y se comprueba el estado de la Ford Transit.

**Resultado esperado:** la modificación solo afecta al vehículo seleccionado.

**Resultado:** correcto.

### PT-09. Conservación de datos

Se comprueba que modificar la disponibilidad no altera el identificador, la marca, el modelo, la categoría, las plazas, la capacidad de carga ni la transmisión.

**Resultado:** correcto.

## 6. Ejecución y resultados

Comando empleado:

`python -m unittest discover -s tests -p "test_gc03_77_disponibilidad_manual.py" -v`

Salida final:

```text
Ran 9 tests in 0.002s

OK
```

| Concepto | Resultado |
|---|---|
| Pruebas ejecutadas | 9 |
| Pruebas superadas | 9 |
| Fallos | 0 |
| Errores | 0 |
| Duración total | 0,002 segundos |

## 7. Alcance y limitaciones

Las nueve pruebas validan el funcionamiento del método `cambiar_estado_vehiculo()` y la consulta posterior de los objetos almacenados en memoria.

No se han realizado pruebas sobre una interfaz administrativa funcional. En la rama revisada, los archivos `src/models/cambio_disponibilidad_admin.py` y `src/services/gestion_disponibilidad_service.py` no contienen implementación.

Por tanto, las pruebas realizadas no permiten confirmar todavía la integración completa del cambio de disponibilidad en la vista administrativa, aunque la subtarea GC03-78 figure como terminada en Jira.

Tampoco se han realizado pruebas con bases de datos externas ni persistencia entre ejecuciones independientes del programa.

## 8. Conclusiones

Se han ejecutado nueve pruebas automatizadas con resultado satisfactorio.

Se ha verificado que el servicio permite cambiar la disponibilidad de los vehículos, recuperar el estado disponible, consultar los cambios realizados y rechazar operaciones inválidas.

También se ha comprobado que los cambios no afectan a otros vehículos y que los datos originales se conservan.

**El comportamiento del servicio queda validado en el entorno local probado.** La verificación de la integración con la vista administrativa queda fuera del alcance de estos resultados y deberá realizarse cuando exista una implementación funcional.