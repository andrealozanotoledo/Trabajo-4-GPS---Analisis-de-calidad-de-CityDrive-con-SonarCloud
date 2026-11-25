# US-012 — Pruebas de concurrencia y bloqueo de reservas

## 1. Identificación

- **Historia de usuario:** GC03-40 — US-012: Evitar reservas solapadas.
- **Subtarea:** GC03-46 — ST-0122: Implementar pruebas unitarias de concurrencia y bloqueo.
- **Responsable:** Borja Gómez Castaño.
- **Fecha:** 07/11/2026.
- **Resultado:** 9 pruebas automatizadas superadas.

## 2. Objetivo

Comprobar que el sistema CityDrive evita registrar reservas incompatibles para un mismo vehículo y periodo de tiempo.

Se verifica tanto la detección de fechas solapadas como el comportamiento del sistema cuando varios hilos intentan reservar simultáneamente.

## 3. Componentes utilizados

- `src/citydrive/reservas/solapamiento.py`: implementación de comprobación y registro de reservas.
- `tests/test_solapamiento.py`: pruebas de validación de fechas y disponibilidad.
- `tests/test_gc03_46_concurrencia.py`: pruebas de concurrencia y bloqueo.

Las pruebas se han realizado en Python utilizando `unittest`, `ThreadPoolExecutor`, `Barrier` y un retraso artificial controlado mediante `unittest.mock.patch`.

No se ha modificado la implementación de los compañeros.

## 4. Pruebas unitarias de solapamiento

| Identificador | Caso de prueba | Resultado |
|---|---|---|
| PT-01 | Rechazar intervalos de fechas incorrectos | Correcto |
| PT-02 | Comprobar que las reservas canceladas no bloquean disponibilidad | Correcto |
| PT-03 | Permitir reservas sin solapamiento | Correcto |
| PT-04 | Detectar reservas solapadas | Correcto |
| PT-05 | Detectar solapamiento en una fecha límite compartida | Correcto |
| PT-06 | Diferenciar reservas de vehículos distintos | Correcto |

### Ejecución

Comando:

`python -m unittest discover -s tests -p "test_solapamiento.py" -v`

Resultado:

```text
Ran 6 tests in 0.003s

OK
```

Se han superado las seis pruebas de validación de fechas y disponibilidad.

## 5. Pruebas de concurrencia

Se utiliza un conjunto de ocho hilos para simular intentos simultáneos de registro.

La implementación utiliza `threading.Lock` para proteger conjuntamente la comprobación de disponibilidad y el registro de la reserva.

### PT-07. Reservas simultáneas del mismo vehículo

**Escenario:** ocho hilos intentan reservar el vehículo `VEH-001` del 10 al 12 de noviembre de 2026.

Se introduce un retraso artificial de 0,02 segundos durante la comprobación de disponibilidad para favorecer la aparición de posibles condiciones de carrera.

**Resultado esperado:**

- Una reserva registrada correctamente.
- Siete operaciones rechazadas.
- Una única reserva almacenada.

**Resultado obtenido:** correcto.

### PT-08. Reservas simultáneas de vehículos diferentes

**Escenario:** ocho hilos intentan reservar vehículos distintos para las mismas fechas.

**Resultado esperado:**

- Ocho reservas registradas.
- Ocho identificadores de vehículo diferentes.
- Ningún rechazo por solapamiento.

**Resultado obtenido:** correcto.

### PT-09. Reservas simultáneas en fechas no solapadas

**Escenario:** ocho hilos reservan el mismo vehículo en intervalos de fechas que no se solapan.

**Resultado esperado:**

- Ocho reservas registradas.
- Todas asociadas al mismo vehículo.
- Ningún rechazo por conflicto de fechas.

**Resultado obtenido:** correcto.

## 6. Resultados de concurrencia

Comando utilizado:

`python -m unittest discover -s tests -p "test_gc03_46_concurrencia.py" -v`

Resultado:

```text
Ran 3 tests in 0.197s

OK
```

| Concepto | Resultado |
|---|---|
| Pruebas de solapamiento | 6 |
| Pruebas de concurrencia | 3 |
| Total de pruebas | 9 |
| Pruebas superadas | 9 |
| Fallos | 0 |
| Errores | 0 |

## 7. Análisis del bloqueo

La función `registrar_reserva_si_disponible()` utiliza un bloqueo compartido de tipo `Lock`.

Este mecanismo impide que varios hilos ejecuten simultáneamente la sección que comprueba la disponibilidad y registra la reserva.

La prueba PT-07 ha confirmado que, en el escenario de ocho intentos concurrentes, solo se registra una reserva para el mismo vehículo y periodo.

Las pruebas PT-08 y PT-09 han confirmado que las operaciones válidas no se rechazan indebidamente cuando los vehículos son diferentes o las fechas no se solapan.

## 8. Limitaciones

Las pruebas se ejecutan en un único proceso Python y utilizan una lista de reservas almacenada en memoria.

No se han realizado pruebas entre varios procesos, servidores o instancias de una base de datos.

El bloqueo implementado es compartido a nivel del módulo Python, por lo que también serializa temporalmente las operaciones de vehículos diferentes.

Los resultados demuestran el funcionamiento del bloqueo en los escenarios locales ensayados, pero no garantizan el mismo comportamiento en una arquitectura distribuida.

## 9. Conclusiones

Se han ejecutado nueve pruebas automatizadas de GC03-46, todas con resultado satisfactorio.

Se ha verificado la detección de reservas solapadas, la validación de fechas y el comportamiento ante solicitudes concurrentes.

En particular, se ha confirmado que ocho intentos simultáneos de reservar el mismo vehículo y periodo producen una única reserva registrada.

**Las pruebas funcionales y de concurrencia de GC03-46 se consideran superadas dentro del entorno local utilizado.**