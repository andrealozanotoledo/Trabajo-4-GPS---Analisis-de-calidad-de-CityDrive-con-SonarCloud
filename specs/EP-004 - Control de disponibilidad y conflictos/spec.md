# EP-004 — Control de disponibilidad y conflictos

**Goals:** G-01, G-02, G-03  
**Baseline:** Catálogo V0 - Semana 2

## Boundary

Esta épica incluye el bloqueo del vehículo durante las fechas reservadas, la prevención de reservas que se solapen sobre un mismo vehículo y la gestión del caso en el que un vehículo deje de estar disponible mientras un usuario está realizando una reserva.

Quedan fuera los sistemas externos de sincronización de flotas y cualquier integración con hardware o dispositivos IoT.

## Epic outcome

Garantizar que las reservas registradas sean coherentes con la disponibilidad real de la flota y evitar que un mismo vehículo pueda quedar reservado simultáneamente para periodos incompatibles.

## Stories

### US-011 — Bloquear el vehículo para las fechas reservadas

> *Como sistema, quiero marcar como no disponible un vehículo durante las fechas de una reserva confirmada para evitar que pueda volver a reservarse en ese mismo periodo.*

- **Priority:** Must
- **Estimate:** 5 h-p
- **Uncertainty:** Media
- **Predecessors:** US-009, US-012
- **Initial plan:** Pendiente de asignación en la planificación de la Semana 3.

#### Acceptance criteria

- **US-011-AC-01:** Tras confirmarse correctamente una reserva, el vehículo queda ocupado durante las fechas reservadas.
- **US-011-AC-02:** Una búsqueda posterior no ofrece el vehículo como disponible durante un periodo incompatible con una reserva activa.
- **US-011-AC-03:** El bloqueo afecta únicamente al intervalo de fechas reservado.
- **US-011-AC-04:** Solo las reservas confirmadas correctamente modifican la disponibilidad del vehículo.

#### Verification and constraints

- La disponibilidad debe mantenerse coherente con las reservas confirmadas almacenadas.
- Un mismo vehículo no puede quedar asociado a dos reservas activas con periodos incompatibles.
- El bloqueo no implica una modificación física del vehículo.
- No se utilizarán sistemas externos de flotas ni dispositivos IoT.

---

### US-012 — Evitar reservas solapadas

> *Como cliente, quiero que el sistema impida reservar un vehículo ocupado durante alguna de las fechas seleccionadas para evitar conflictos entre reservas.*

- **Priority:** Must
- **Estimate:** 7 h-p
- **Uncertainty:** Alta
- **Predecessors:** US-007
- **Initial plan:** Pendiente de asignación en la planificación de la Semana 3.

#### Acceptance criteria

- **US-012-AC-01:** Antes del registro definitivo de una reserva, el sistema comprueba las reservas activas existentes para el mismo vehículo.
- **US-012-AC-02:** Si existe un solapamiento con una reserva activa, la nueva reserva no se registra.
- **US-012-AC-03:** Si dos solicitudes intentan confirmar simultáneamente el mismo vehículo para periodos incompatibles, solo una de ellas puede quedar registrada correctamente.
- **US-012-AC-04:** La solicitud que detecte que el vehículo ya no está disponible será rechazada.
- **US-012-AC-05:** Dos reservas del mismo vehículo pueden existir únicamente cuando sus periodos no se solapan.

#### Verification and constraints

- Un vehículo no puede tener dos reservas activas que compartan al menos un día.
- Las fechas de inicio y fin se consideran incluidas en el periodo reservado.
- Si una reserva finaliza el día 12, una nueva reserva del mismo vehículo podrá comenzar como mínimo el día 13.
- La comprobación de disponibilidad utilizada para registrar la reserva debe utilizar el estado actual de las reservas almacenadas en CityDrive.
- Desde el punto de vista funcional, la comprobación definitiva y el registro deben impedir que dos solicitudes incompatibles finalicen ambas correctamente.
- Solo se consideran las reservas almacenadas dentro de CityDrive.

---

### US-013 — Informar de cambios de disponibilidad durante la reserva

> *Como cliente, quiero ser informado si el vehículo deja de estar disponible antes de confirmar la reserva para poder seleccionar otra alternativa.*

- **Priority:** Should
- **Estimate:** 4 h-p
- **Uncertainty:** Media
- **Predecessors:** US-012
- **Initial plan:** Pendiente de asignación en la planificación de la Semana 3.

#### Acceptance criteria

- **US-013-AC-01:** Si la comprobación final de disponibilidad detecta que el vehículo ya no está disponible para las fechas seleccionadas, la reserva no se confirma.
- **US-013-AC-02:** El usuario recibe un mensaje indicando que el vehículo ha dejado de estar disponible para el periodo seleccionado.
- **US-013-AC-03:** El usuario puede volver a la selección de fechas y realizar una nueva búsqueda.
- **US-013-AC-04:** Si el usuario había aplicado filtros en la búsqueda anterior, estos se conservan al volver al proceso de búsqueda.
- **US-013-AC-05:** El rechazo de la reserva no modifica ni elimina la reserva que provocó el conflicto.

#### Verification and constraints

- Esta historia se aplica exclusivamente cuando la disponibilidad cambia durante el flujo de reserva después de que el vehículo hubiera sido mostrado previamente como disponible.
- No se debe crear una reserva cuando la disponibilidad haya cambiado.
- La comprobación debe utilizar la información actual del propio sistema.
- Si dos usuarios intentan confirmar simultáneamente reservas incompatibles, el usuario cuya reserva no pueda registrarse debe recibir este comportamiento de información.
- Al regresar a la búsqueda se mantiene el contexto de filtrado utilizado previamente, cuando exista.
- La búsqueda general de vehículos disponibles corresponde a US-002.
- La consulta ordinaria de disponibilidad de un vehículo concreto corresponde a US-006.
- La responsabilidad de esta historia es informar y permitir recuperar el flujo cuando la revalidación definitiva detecta un conflicto.