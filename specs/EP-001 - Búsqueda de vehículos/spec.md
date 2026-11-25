# EP-001 — Búsqueda de vehículos

**Goals:** G-01, G-02  
**Baseline:** Catálogo V0 - Semana 2

## Boundary

Esta épica incluye la introducción de un rango de fechas por parte del cliente y la consulta de los vehículos disponibles durante dicho periodo. También contempla informar al usuario cuando no existan vehículos disponibles.

Quedan fuera de esta épica el filtrado por tipo de vehículo, la selección definitiva del vehículo y la creación de la reserva.

## Epic outcome

Permitir que el cliente indique las fechas en las que necesita un vehículo y obtenga de forma clara qué vehículos de AutoRent se encuentran disponibles durante ese periodo.

## Stories

### US-001 — Introducir un rango de fechas para la búsqueda

> *Como cliente, quiero indicar una fecha de inicio y una fecha de fin para poder buscar vehículos disponibles durante ese periodo.*

- **Priority:** Must
- **Estimate:** 5 h-p
- **Uncertainty:** Baja
- **Predecessors:** —
- **Initial plan:** Pendiente de asignación en la planificación de la Semana 3.

#### Acceptance criteria

- **US-001-AC-01:** El usuario puede introducir una fecha de inicio.
- **US-001-AC-02:** El usuario puede introducir una fecha de fin.
- **US-001-AC-03:** La fecha de fin no puede ser anterior a la fecha de inicio.
- **US-001-AC-04:** Si las fechas introducidas no son válidas, el sistema indica qué condición no se cumple.
- **US-001-AC-05:** Si ambas fechas son válidas, el usuario puede continuar con la búsqueda.
- **US-001-AC-06:** Los campos de fecha de inicio y fecha de fin aparecen identificados mediante etiquetas diferenciadas.

#### Verification and constraints

- Ambas fechas son obligatorias.
- La fecha final debe ser igual o posterior a la fecha inicial.
- Las fechas deben utilizar un formato válido y coherente.
- No se utilizarán datos reales de clientes.
- Los mensajes de validación deben permitir identificar el error que impide continuar.
- La verificación se realizará mediante pruebas funcionales deterministas con fechas válidas e inválidas.

---

### US-002 — Consultar los vehículos disponibles

> *Como cliente, quiero consultar los vehículos disponibles para las fechas seleccionadas para poder elegir una opción que pueda reservar.*

- **Priority:** Must
- **Estimate:** 7 h-p
- **Uncertainty:** Media
- **Predecessors:** US-001
- **Initial plan:** Pendiente de asignación en la planificación de la Semana 3.

#### Acceptance criteria

- **US-002-AC-01:** Solo se muestran vehículos disponibles durante todo el rango seleccionado.
- **US-002-AC-02:** Los vehículos con reservas incompatibles no se muestran como disponibles.
- **US-002-AC-03:** Los vehículos marcados manualmente como no disponibles tampoco aparecen.
- **US-002-AC-04:** Si no existen resultados, se muestra un mensaje indicando que no existen vehículos disponibles para el rango seleccionado.
- **US-002-AC-05:** La consulta ofrece una respuesta observable en la interfaz en menos de 2 segundos en el entorno local de pruebas.

#### Verification and constraints

- Un vehículo solo se considera disponible si lo está durante todo el periodo solicitado.
- Las reservas existentes deben comprobarse antes de mostrar los resultados.
- La información procederá únicamente del catálogo ficticio de AutoRent.
- El tiempo de respuesta inferior a 2 segundos se comprobará en el entorno local de pruebas del proyecto.
- La verificación se realizará mediante pruebas funcionales deterministas utilizando datos sintéticos.
- No se requieren pruebas de carga o estrés propias de un entorno de producción.
- Esta historia realiza la consulta general del catálogo para el rango de fechas seleccionado.
- La comprobación detallada de disponibilidad de un vehículo concreto corresponde a US-006.
- Los cambios de disponibilidad producidos durante el proceso de reserva se gestionan mediante US-013.

---

### US-003 — Informar cuando no existan vehículos disponibles

> *Como cliente, quiero recibir un mensaje claro cuando no existan vehículos disponibles para las fechas indicadas para saber que debo modificar mi búsqueda.*

- **Priority:** Should
- **Estimate:** 3 h-p
- **Uncertainty:** Baja
- **Predecessors:** US-002
- **Initial plan:** Pendiente de asignación en la planificación de la Semana 3.

#### Acceptance criteria

- **US-003-AC-01:** Si la búsqueda no devuelve vehículos, el sistema muestra un mensaje informativo.
- **US-003-AC-02:** El mensaje indica que no existen vehículos disponibles para el rango seleccionado.
- **US-003-AC-03:** El usuario puede modificar las fechas y volver a realizar la búsqueda.

#### Verification and constraints

- El mensaje debe ser visible e indicar explícitamente que no existen vehículos disponibles para las fechas seleccionadas.
- No debe mostrarse información de vehículos no disponibles como alternativa válida.
- Desde el mensaje de falta de disponibilidad, el usuario debe poder volver al formulario de búsqueda y modificar las fechas.
- La verificación se realizará mediante una prueba funcional determinista con datos sintéticos que produzca una búsqueda sin resultados.