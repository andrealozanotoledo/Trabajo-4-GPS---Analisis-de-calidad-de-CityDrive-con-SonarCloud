# EP-006 — Gestión del catálogo de vehículos

**Goals:** G-02, G-03  
**Baseline:** Catálogo V0 - Semana 2

## Boundary

Esta épica incluye las operaciones básicas necesarias para que el personal de AutoRent pueda mantener el catálogo utilizado por CityDrive: registrar vehículos, modificar su información, cambiar su estado de disponibilidad y consultar el catálogo completo.

Estas funciones se realizarán desde una vista administrativa diferenciada de las funciones destinadas al cliente dentro del prototipo.

Quedan fuera la gestión mecánica del vehículo, la localización GPS, el mantenimiento físico de la flota, las integraciones con sistemas externos y la implementación de sistemas complejos o externos de autenticación y gestión de identidades.

## Epic outcome

Proporcionar al personal de AutoRent las funciones mínimas necesarias para mantener actualizado el catálogo de vehículos del que depende el proceso de búsqueda y reserva de CityDrive.

## Stories

### US-018 — Dar de alta un vehículo

> *Como personal de AutoRent, quiero registrar un nuevo vehículo en el sistema para que pueda formar parte del catálogo disponible.*

- **Priority:** Must
- **Estimate:** 6 h-p
- **Uncertainty:** Media
- **Predecessors:** —
- **Initial plan:** Pendiente de asignación en la planificación de la Semana 3.

#### Acceptance criteria

- **US-018-AC-01:** El personal puede acceder desde la vista administrativa a la función de alta de vehículos.
- **US-018-AC-02:** El personal puede introducir la marca, modelo, categoría, número de plazas, capacidad de maletero o carga, tipo de transmisión y estado operativo del vehículo.
- **US-018-AC-03:** El sistema valida que los campos mínimos del vehículo estén informados.
- **US-018-AC-04:** Si falta algún campo obligatorio, el sistema informa del problema y no registra el vehículo.
- **US-018-AC-05:** Si los datos son válidos, el sistema genera automáticamente un identificador único para el nuevo vehículo y lo registra.
- **US-018-AC-06:** El vehículo registrado puede utilizarse posteriormente en búsquedas y reservas.

#### Verification and constraints

- Los datos del vehículo siguen el modelo mínimo de datos sintéticos definido en `specs/product/goals.md`.
- El identificador del vehículo es generado automáticamente por CityDrive y no es introducido manualmente por el personal.
- Cada vehículo registrado debe disponer de un identificador único.
- Una vez asignado, el identificador no se modifica mediante las funciones de mantenimiento del catálogo.
- La función forma parte de la vista administrativa destinada al personal de AutoRent.
- En el MVP no se implementará un sistema complejo o externo de autenticación y gestión de identidades.
- Los vehículos utilizados serán ficticios.
- Se verificarán mediante pruebas funcionales deterministas los casos de alta válida y campo obligatorio ausente.
- Los mensajes de validación deberán identificar el motivo por el que el vehículo no puede registrarse.
- No se almacenará información de localización GPS.
- No se incluirán datos de mantenimiento mecánico.
- La información registrada debe estar disponible en consultas posteriores.

---

### US-019 — Modificar la información de un vehículo

> *Como personal de AutoRent, quiero modificar los datos de un vehículo para mantener actualizada su información.*

- **Priority:** Should
- **Estimate:** 5 h-p
- **Uncertainty:** Baja
- **Predecessors:** US-018
- **Initial plan:** Pendiente de asignación en la planificación de la Semana 3.

#### Acceptance criteria

- **US-019-AC-01:** El personal puede seleccionar un vehículo existente desde la vista administrativa.
- **US-019-AC-02:** Puede modificar la marca, modelo, categoría, número de plazas, capacidad de maletero o carga y tipo de transmisión del vehículo.
- **US-019-AC-03:** Si los datos modificados son válidos, los cambios quedan almacenados.
- **US-019-AC-04:** Si los datos modificados no son válidos, el sistema informa del problema y mantiene los valores anteriores.
- **US-019-AC-05:** Las consultas posteriores muestran la información actualizada.

#### Verification and constraints

- Los campos modificables siguen el modelo mínimo de datos sintéticos definido en `specs/product/goals.md`.
- La función forma parte de la vista administrativa destinada al personal de AutoRent.
- El identificador del vehículo no se modifica mediante esta historia.
- El cambio del estado operativo se realiza mediante US-020.
- Solo se podrán modificar vehículos existentes.
- Las modificaciones deben respetar las validaciones definidas para el catálogo.
- Se verificarán mediante pruebas funcionales deterministas una modificación válida y una modificación con datos no válidos.
- No se incluye información mecánica ni GPS.

---

### US-020 — Modificar el estado de disponibilidad

> *Como personal de AutoRent, quiero marcar un vehículo como disponible o no disponible para evitar que se ofrezcan vehículos que temporalmente no pueden alquilarse.*

- **Priority:** Should
- **Estimate:** 4 h-p
- **Uncertainty:** Media
- **Predecessors:** US-018
- **Initial plan:** Pendiente de asignación en la planificación de la Semana 3.

#### Acceptance criteria

- **US-020-AC-01:** El personal puede acceder desde la vista administrativa al estado de un vehículo.
- **US-020-AC-02:** El personal puede cambiar el estado manual del vehículo entre disponible y no disponible.
- **US-020-AC-03:** Un vehículo marcado como no disponible no aparece como reservable.
- **US-020-AC-04:** Un vehículo puede volver a marcarse como disponible.
- **US-020-AC-05:** El nuevo estado queda almacenado y se refleja en las consultas posteriores.

#### Verification and constraints

- La función forma parte de la vista administrativa destinada al personal de AutoRent.
- El estado manual debe tenerse en cuenta junto con las reservas existentes.
- Se verificará mediante pruebas funcionales deterministas el cambio de disponible a no disponible y el cambio inverso.
- Después del cambio se comprobará que las búsquedas y consultas utilizan el nuevo estado.
- No implica modificar físicamente el vehículo.
- No existe integración con sistemas externos de flota.

---

### US-021 — Consultar el catálogo completo

> *Como personal de AutoRent, quiero consultar el catálogo completo de vehículos para revisar la información y el estado actual de la flota.*

- **Priority:** Should
- **Estimate:** 5 h-p
- **Uncertainty:** Baja
- **Predecessors:** US-018
- **Initial plan:** Pendiente de asignación en la planificación de la Semana 3.

#### Acceptance criteria

- **US-021-AC-01:** El personal puede acceder desde la vista administrativa al catálogo completo.
- **US-021-AC-02:** El personal puede visualizar los vehículos registrados.
- **US-021-AC-03:** Cada vehículo muestra su identificador, marca, modelo, categoría, número de plazas, capacidad de maletero o carga y tipo de transmisión.
- **US-021-AC-04:** Se muestra el estado operativo actual de cada vehículo.
- **US-021-AC-05:** La información mostrada coincide con los datos almacenados.
- **US-021-AC-06:** La consulta ofrece una respuesta observable en la interfaz en menos de 2 segundos en el entorno local de pruebas.

#### Verification and constraints

- La información mostrada sigue el modelo mínimo de datos sintéticos definido en `specs/product/goals.md`.
- La consulta está orientada exclusivamente a las funciones simuladas del personal de AutoRent.
- La separación entre cliente y personal se representa mediante una vista administrativa diferenciada dentro del prototipo.
- En el MVP no se implementará un sistema complejo o externo de autenticación y gestión de identidades.
- Solo se utilizarán datos ficticios.
- El tiempo de respuesta inferior a 2 segundos se comprobará en el entorno local de pruebas.
- La verificación se realizará mediante pruebas funcionales deterministas utilizando datos sintéticos.
- No se requieren pruebas de carga o estrés propias de un entorno de producción.
- No se incluye información GPS, mecánica ni procedente de sistemas externos.