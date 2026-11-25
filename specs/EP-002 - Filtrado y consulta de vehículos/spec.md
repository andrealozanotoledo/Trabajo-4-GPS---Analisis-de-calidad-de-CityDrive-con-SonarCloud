# EP-002 — Filtrado y consulta de vehículos

**Goals:** G-01, G-02  
**Baseline:** Catálogo V0 - Semana 2

## Boundary

Esta épica incluye el filtrado de los resultados disponibles según el tipo de vehículo, la consulta de las características principales de cada vehículo y la visualización de su disponibilidad.

Quedan fuera de esta épica la introducción inicial de las fechas, la confirmación de reservas y la gestión del catálogo por parte del personal de AutoRent.

## Epic outcome

Facilitar que el cliente pueda reducir las opciones disponibles y consultar la información necesaria de cada vehículo antes de decidir cuál desea reservar.

## Stories

### US-004 — Filtrar los vehículos por tipo

> *Como cliente, quiero filtrar los vehículos disponibles por tipo para poder encontrar más fácilmente un coche o una furgoneta según mis necesidades.*

- **Priority:** Must
- **Estimate:** 4 h-p
- **Uncertainty:** Baja
- **Predecessors:** US-002
- **Initial plan:** Pendiente de asignación en la planificación de la Semana 3.

#### Acceptance criteria

- **US-004-AC-01:** El usuario puede seleccionar el tipo coche.
- **US-004-AC-02:** El usuario puede seleccionar el tipo furgoneta.
- **US-004-AC-03:** Los resultados muestran únicamente vehículos del tipo seleccionado.
- **US-004-AC-04:** El usuario puede eliminar el filtro y volver a ver todos los vehículos disponibles.
- **US-004-AC-05:** Si no existen vehículos del tipo seleccionado, se muestra un mensaje indicando que no hay resultados para ese filtro.

#### Verification and constraints

- El filtro se aplica únicamente sobre los resultados de vehículos disponibles.
- En esta versión solo se contemplan coches y furgonetas.
- El control de filtrado debe estar disponible en la vista de resultados y permitir aplicar o eliminar el filtro sin volver a introducir las fechas.
- La verificación se realizará mediante pruebas funcionales deterministas utilizando datos sintéticos.

---

### US-005 — Consultar las características de un vehículo

> *Como cliente, quiero consultar las características principales de un vehículo para poder valorar si se adapta a mis necesidades.*

- **Priority:** Should
- **Estimate:** 5 h-p
- **Uncertainty:** Baja
- **Predecessors:** US-002
- **Initial plan:** Pendiente de asignación en la planificación de la Semana 3.

#### Acceptance criteria

- **US-005-AC-01:** El usuario puede acceder a la información principal del vehículo seleccionado.
- **US-005-AC-02:** Se muestran la marca, el modelo, la categoría, el número de plazas, la capacidad de maletero o carga, el tipo de transmisión y el estado operativo del vehículo.
- **US-005-AC-03:** La información mostrada corresponde al vehículo seleccionado.
- **US-005-AC-04:** Los campos mostrados aparecen identificados de forma que el usuario puede asociar cada valor con su característica.
- **US-005-AC-05:** La consulta ofrece una respuesta observable en la interfaz en menos de 2 segundos en el entorno local de pruebas.

#### Verification and constraints

- Los campos del vehículo utilizados en esta historia siguen el modelo mínimo de datos sintéticos definido en `specs/product/goals.md`.
- Solo se utilizará información ficticia del catálogo de AutoRent.
- No se incluirán datos mecánicos o técnicos ajenos al alcance definido.
- El tiempo de respuesta inferior a 2 segundos se comprobará en el entorno local de pruebas del proyecto.
- La verificación se realizará mediante pruebas funcionales deterministas utilizando datos sintéticos.
- No se requieren pruebas de carga o estrés propias de un entorno de producción.

---

### US-006 — Visualizar la disponibilidad del vehículo seleccionado

> *Como cliente, quiero comprobar que el vehículo seleccionado está disponible para las fechas indicadas antes de iniciar la reserva.*

- **Priority:** Must
- **Estimate:** 4 h-p
- **Uncertainty:** Media
- **Predecessors:** US-002
- **Initial plan:** Pendiente de asignación en la planificación de la Semana 3.

#### Acceptance criteria

- **US-006-AC-01:** El sistema indica si el vehículo está disponible para el rango seleccionado.
- **US-006-AC-02:** Un vehículo con una reserva incompatible no se muestra como disponible.
- **US-006-AC-03:** Un vehículo marcado manualmente como no disponible tampoco se considera disponible.
- **US-006-AC-04:** La consulta de disponibilidad ofrece una respuesta observable en la interfaz en menos de 2 segundos en el entorno local de pruebas.

#### Verification and constraints

- La disponibilidad debe calcularse usando las reservas almacenadas y el estado del vehículo.
- La información mostrada debe ser coherente con los resultados de búsqueda.
- No se utilizarán servicios externos para determinar la disponibilidad.
- El tiempo de respuesta inferior a 2 segundos se comprobará en el entorno local de pruebas del proyecto.
- La verificación se realizará mediante pruebas funcionales deterministas utilizando datos sintéticos.
- No se requieren pruebas de carga o estrés propias de un entorno de producción.
- Esta historia comprueba y muestra la disponibilidad de un vehículo concreto seleccionado por el usuario.
- La búsqueda general de vehículos disponibles para un rango de fechas corresponde a US-002.
- Esta comprobación no sustituye a la revalidación definitiva realizada durante la confirmación de la reserva.