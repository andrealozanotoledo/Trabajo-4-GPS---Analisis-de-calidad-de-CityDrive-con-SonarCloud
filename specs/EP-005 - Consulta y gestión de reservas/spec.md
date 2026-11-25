# EP-005 — Consulta y gestión de reservas

**Goals:** G-01, G-02  
**Baseline:** Catálogo V0 - Semana 2

## Boundary

Esta épica incluye la consulta de una reserva mediante su referencia, la visualización de sus datos, la posibilidad de cancelarla y la consulta de las reservas activas por parte del personal de AutoRent.

En el MVP, la referencia única de la reserva actúa como mecanismo funcional para que el cliente consulte y cancele una reserva individual. Las funciones destinadas al personal de AutoRent se presentan mediante una vista administrativa diferenciada dentro del prototipo.

Quedan fuera los reembolsos, pagos, modificaciones contractuales, cualquier gestión relacionada con aseguradoras y la implementación de sistemas complejos o externos de autenticación y gestión de identidades.

## Epic outcome

Permitir que el cliente pueda consultar y gestionar de forma básica una reserva ya realizada y que el personal de AutoRent tenga visibilidad sobre las reservas activas.

## Stories

### US-014 — Consultar una reserva mediante su referencia

> *Como cliente, quiero introducir la referencia de mi reserva para poder consultarla posteriormente.*

- **Priority:** Must
- **Estimate:** 4 h-p
- **Uncertainty:** Baja
- **Predecessors:** US-010
- **Initial plan:** Pendiente de asignación en la planificación de la Semana 3.

#### Acceptance criteria

- **US-014-AC-01:** El usuario puede introducir una referencia de reserva.
- **US-014-AC-02:** Si la referencia existe, el sistema recupera únicamente la reserva asociada a esa referencia.
- **US-014-AC-03:** Si la referencia no existe, se muestra un mensaje indicando que no se ha encontrado ninguna reserva asociada.
- **US-014-AC-04:** La consulta no modifica los datos almacenados.
- **US-014-AC-05:** La consulta ofrece una respuesta observable en la interfaz en menos de 2 segundos en el entorno local de pruebas.

#### Verification and constraints

- Cada referencia debe identificar una única reserva.
- En el MVP, disponer de la referencia válida permite consultar esa reserva individual.
- No se implementará autenticación adicional del cliente ni integración con sistemas externos de identidad.
- Las reservas y referencias utilizadas serán ficticias.
- El tiempo de respuesta inferior a 2 segundos se comprobará en el entorno local de pruebas del proyecto.
- Se comprobarán mediante pruebas funcionales deterministas tanto una referencia existente como una inexistente.
- No se requieren pruebas de carga o estrés propias de un entorno de producción.

---

### US-015 — Visualizar los datos de una reserva

> *Como cliente, quiero visualizar el vehículo, las fechas y el estado de mi reserva para comprobar su información.*

- **Priority:** Should
- **Estimate:** 4 h-p
- **Uncertainty:** Baja
- **Predecessors:** US-014
- **Initial plan:** Pendiente de asignación en la planificación de la Semana 3.

#### Acceptance criteria

- **US-015-AC-01:** Se muestra el vehículo asociado a la reserva.
- **US-015-AC-02:** Se muestran las fechas de inicio y fin.
- **US-015-AC-03:** Se muestra el estado actual de la reserva.
- **US-015-AC-04:** La información corresponde exclusivamente a la referencia consultada.
- **US-015-AC-05:** Cada dato mostrado aparece identificado de forma que el usuario puede distinguir el vehículo, las fechas y el estado de la reserva.
- **US-015-AC-06:** La visualización ofrece una respuesta observable en la interfaz en menos de 2 segundos en el entorno local de pruebas.

#### Verification and constraints

- Solo se mostrará información perteneciente a la reserva localizada mediante la referencia introducida.
- No se mostrarán datos de otras reservas.
- No se mostrarán datos sensibles reales.
- El tiempo de respuesta inferior a 2 segundos se comprobará en el entorno local de pruebas del proyecto.
- La verificación se realizará mediante pruebas funcionales deterministas utilizando reservas y datos sintéticos.
- No se requieren pruebas de carga o estrés propias de un entorno de producción.

---

### US-016 — Cancelar una reserva

> *Como cliente, quiero cancelar una reserva existente para liberar el vehículo cuando ya no vaya a necesitarlo.*

- **Priority:** Should
- **Estimate:** 5 h-p
- **Uncertainty:** Media
- **Predecessors:** US-014
- **Initial plan:** Pendiente de asignación en la planificación de la Semana 3.

#### Acceptance criteria

- **US-016-AC-01:** El usuario puede solicitar la cancelación de la reserva localizada mediante una referencia válida.
- **US-016-AC-02:** Una reserva cancelada deja de considerarse activa.
- **US-016-AC-03:** Las fechas correspondientes vuelven a quedar disponibles si no existe otro conflicto.
- **US-016-AC-04:** Si la cancelación finaliza correctamente, el sistema muestra un mensaje indicando que la reserva ha sido cancelada.
- **US-016-AC-05:** Si la reserva ya no puede cancelarse porque no existe o no está activa, el sistema informa de que la operación no puede realizarse y no modifica la disponibilidad.

#### Verification and constraints

- En el MVP, disponer de la referencia válida permite solicitar la cancelación de esa reserva individual.
- No se implementará una comprobación adicional de identidad del cliente.
- La cancelación no implica reembolsos ni operaciones de pago.
- Solo podrán cancelarse reservas existentes y activas.
- La actualización debe mantener coherente la disponibilidad del vehículo.
- Se verificarán mediante pruebas funcionales deterministas los casos de cancelación correcta y de reserva no cancelable utilizando datos sintéticos.
- Los mensajes deberán permitir identificar si la cancelación se ha realizado o por qué no ha podido completarse.

---

### US-017 — Consultar las reservas activas

> *Como personal de AutoRent, quiero consultar las reservas activas para conocer qué vehículos están comprometidos y durante qué fechas.*

- **Priority:** Must
- **Estimate:** 5 h-p
- **Uncertainty:** Media
- **Predecessors:** US-009
- **Initial plan:** Pendiente de asignación en la planificación de la Semana 3.

#### Acceptance criteria

- **US-017-AC-01:** El personal puede acceder desde la vista administrativa del prototipo a una lista de reservas activas.
- **US-017-AC-02:** Cada reserva muestra al menos el vehículo y las fechas asociadas.
- **US-017-AC-03:** Las reservas canceladas no se consideran activas.
- **US-017-AC-04:** La información coincide con las reservas almacenadas.
- **US-017-AC-05:** La vista administrativa está diferenciada de las funciones destinadas al cliente.

#### Verification and constraints

- La consulta está orientada exclusivamente a las funciones simuladas del personal de AutoRent.
- En el MVP no se implementará un sistema complejo o externo de autenticación y gestión de identidades para diferenciar al personal.
- La separación entre cliente y personal se representará mediante vistas o accesos funcionales diferenciados dentro del prototipo.
- Se utilizarán únicamente datos ficticios.
- No incluye facturación, pagos ni información de aseguradoras.