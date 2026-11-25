# EP-003 — Creación de reservas

**Goals:** G-01, G-02  
**Baseline:** Catálogo V0 - Semana 2

## Boundary

Esta épica incluye la selección de un vehículo disponible, la introducción de los datos necesarios para realizar la reserva, la confirmación de la operación y la generación de una referencia identificativa.

Quedan fuera los pagos reales, la facturación, la integración con aseguradoras y cualquier operación física sobre el vehículo.

## Epic outcome

Permitir que el cliente complete de forma autónoma el proceso principal de CityDrive, pasando de la selección de un vehículo disponible a obtener una reserva confirmada e identificable.

## Stories

### US-007 — Seleccionar un vehículo disponible

> *Como cliente, quiero seleccionar uno de los vehículos disponibles para iniciar el proceso de reserva.*

- **Priority:** Must
- **Estimate:** 4 h-p
- **Uncertainty:** Baja
- **Predecessors:** US-002
- **Initial plan:** Pendiente de asignación en la planificación de la Semana 3.

#### Acceptance criteria

- **US-007-AC-01:** El usuario puede seleccionar uno de los vehículos mostrados como disponibles.
- **US-007-AC-02:** El vehículo seleccionado queda asociado al proceso de reserva.
- **US-007-AC-03:** No puede seleccionarse como reservable un vehículo no disponible.

#### Verification and constraints

- La selección debe realizarse sobre resultados de búsqueda válidos.
- El vehículo seleccionado debe conservarse durante el proceso de reserva.
- No se permitirá seleccionar vehículos fuera del catálogo ficticio de AutoRent.

---

### US-008 — Introducir los datos necesarios para la reserva

> *Como cliente, quiero introducir los datos necesarios para que AutoRent pueda registrar correctamente mi reserva.*

- **Priority:** Must
- **Estimate:** 6 h-p
- **Uncertainty:** Media
- **Predecessors:** US-007
- **Initial plan:** Pendiente de asignación en la planificación de la Semana 3.

#### Acceptance criteria

- **US-008-AC-01:** El usuario puede introducir como datos obligatorios su nombre y apellidos ficticios y un correo electrónico ficticio.
- **US-008-AC-02:** El sistema valida que el nombre y apellidos y el correo electrónico estén informados.
- **US-008-AC-03:** Si falta alguno de los datos obligatorios, el sistema informa al usuario indicando qué campo falta y no permite continuar con la confirmación.
- **US-008-AC-04:** Los datos válidos quedan asociados al vehículo y al rango de fechas seleccionados previamente y pueden utilizarse posteriormente para confirmar la reserva.

#### Verification and constraints

- Los campos de reserva siguen el modelo mínimo de datos sintéticos definido en `specs/product/goals.md`.
- El cliente introduce únicamente el nombre y apellidos y el correo electrónico; el vehículo y las fechas proceden de los pasos anteriores del proceso.
- La referencia se genera posteriormente en US-010 y el estado de la reserva se establece como resultado del proceso de confirmación.
- Se utilizarán únicamente datos ficticios durante el desarrollo y las pruebas.
- No se almacenarán datos bancarios ni documentación real.
- La validación se comprobará mediante pruebas funcionales deterministas en las que se omita cada uno de los campos obligatorios.
- Los mensajes de validación deben identificar el dato obligatorio que falta.
- Los campos se limitan a los necesarios para el escenario académico.

---

### US-009 — Confirmar una reserva

> *Como cliente, quiero confirmar los datos de mi reserva antes de finalizarla para comprobar que el vehículo y las fechas son correctos.*

- **Priority:** Must
- **Estimate:** 7 h-p
- **Uncertainty:** Media
- **Predecessors:** US-007, US-008, US-012
- **Initial plan:** Pendiente de asignación en la planificación de la Semana 3.

#### Acceptance criteria

- **US-009-AC-01:** Se muestran el vehículo seleccionado y las fechas de la reserva.
- **US-009-AC-02:** Se muestran los datos necesarios introducidos por el cliente.
- **US-009-AC-03:** El usuario puede confirmar la operación.
- **US-009-AC-04:** En el instante de la confirmación definitiva, el sistema vuelve a comprobar la disponibilidad del vehículo para el rango de fechas seleccionado.
- **US-009-AC-05:** Solo puede confirmarse una reserva para un mismo vehículo y un rango de fechas incompatible.
- **US-009-AC-06:** Si la revalidación es correcta, la reserva queda registrada y el vehículo deja de estar disponible para rangos incompatibles.
- **US-009-AC-07:** Si durante la confirmación el vehículo ha dejado de estar disponible, la reserva no se registra y se aplica el comportamiento definido en US-013.
- **US-009-AC-08:** La confirmación ofrece un resultado observable en la interfaz en menos de 2 segundos en el entorno local de pruebas.

#### Verification and constraints

- No puede registrarse una reserva sin vehículo, fechas y datos obligatorios.
- La comprobación final de disponibilidad y el registro de la reserva deben tratarse como una única operación desde el punto de vista funcional, evitando que dos confirmaciones incompatibles queden registradas.
- Si dos solicitudes intentan confirmar simultáneamente el mismo vehículo para fechas incompatibles, solo una podrá finalizar correctamente.
- La segunda solicitud deberá ser rechazada al detectar que el vehículo ya no está disponible.
- El tiempo de respuesta inferior a 2 segundos se comprobará en el entorno local de pruebas del proyecto.
- La verificación se realizará mediante pruebas funcionales deterministas utilizando datos sintéticos.
- No se requieren pruebas de carga o estrés propias de un entorno de producción.
- La verificación del flujo de confirmación servirá como evidencia para las métricas M-01 y M-02 definidas en `specs/product/goals.md`.
- No se realizará ningún pago real.
- No se generarán contratos reales.

---

### US-010 — Generar una referencia de reserva

> *Como cliente, quiero obtener una referencia única al finalizar la reserva para poder identificarla y consultarla posteriormente.*

- **Priority:** Must
- **Estimate:** 3 h-p
- **Uncertainty:** Baja
- **Predecessors:** US-009
- **Initial plan:** Pendiente de asignación en la planificación de la Semana 3.

#### Acceptance criteria

- **US-010-AC-01:** Cada reserva confirmada recibe una referencia.
- **US-010-AC-02:** La referencia es única dentro del sistema.
- **US-010-AC-03:** La referencia se muestra al usuario una vez finalizada la reserva.
- **US-010-AC-04:** La referencia permite localizar posteriormente la reserva.

#### Verification and constraints

- Una referencia no puede identificar más de una reserva.
- La generación debe evitar duplicados.
- El formato de referencia debe ser estable y legible, por ejemplo `CD-00015`.