# Registro de Decisiones Humanas - Revisión de Requisitos v01

**Proyecto:** CityDrive (MoveTech Solutions)  
**Documento base analizado:** docs/reviews/requirements-report-v01.md  
**Fecha:** Semana 3  
**Equipo revisor:** Julia, Andrea, Óscar, Borja, Álvaro  

---

## Hallazgo F-01 (Severidad: MAJOR)
- **Descripción:** Ambigüedad en los campos mínimos que componen un vehículo y una reserva.
- **Decisión del equipo:** ACCEPTED (Aceptada)
- **Justificación y acuerdo:**
  Se establece un modelo de datos sintéticos uniforme para todo el proyecto:
  - **Vehículo:** id, marca, modelo, categoría (Coche / Furgoneta), plazas, maletero/carga, transmisión (Manual / Automático) y estado operativo (Disponible / No disponible).
  - **Reserva:** referencia, vehiculoId, fecha inicio, fecha fin, nombre/apellidos ficticios, correo ficticio y estado (Confirmada / Cancelada).
  ---

## Hallazgo F-02 (Severidad: MAJOR)
- **Descripción:** Falta de especificación sobre concurrencia y conflicto si dos usuarios intentan confirmar simultáneamente el mismo vehículo para fechas solapadas.
- **Decisión del equipo:** ACCEPTED (Aceptada)
- **Justificación y acuerdo:**
  Se define la regla de revalidación atómica en confirmación (US-009 y US-012):
  - El bloqueo del vehículo se consolida en el instante de confirmación definitiva.
  - Si una segunda petición concurrente intenta confirmar sobre las mismas fechas, el sistema detecta la incompatibilidad, deniega la operación, notifica al segundo usuario mediante US-013 que el vehículo ya no está disponible y redirige a la selección de fechas conservando los filtros introducidos, garantizando el supuesto de no solapamiento.
  ---

## Hallazgo F-03 (Severidad: MINOR)
- **Descripción:** NFR y condiciones de verificación con formulaciones genéricas o difícilmente comprobables.
- **Decisión del equipo:** ACCEPTED_WITH_CHANGES (Aceptada con cambios)
- **Justificación y acuerdo:**
  Se vinculan los criterios de aceptación y verificación a las métricas del proyecto ya fijadas en goals.md (M-01 a M-04):
  - Las operaciones de consulta y confirmación se considerarán válidas con tiempos de respuesta en interfaz inferiores a 2 segundos en el entorno de pruebas local.
  - La verificación se basará en pruebas funcionales deterministas con datos sintéticos, sin requerir pruebas de carga o estrés industriales que exceden el marco del MVP.
  ---

## Hallazgo F-04 (Severidad: QUESTION)
- **Descripción:** Ambigüedad en la delimitación de permisos y acceso entre clientes y personal de AutoRent.
- **Decisión del equipo:** ACCEPTED (Aceptada)
- **Justificación y acuerdo:**
  Se delimita el acceso respetando las fronteras del MVP:
  - El cliente consulta y cancela únicamente su reserva individual utilizando la referencia única alfanumérica obtenida en la confirmación.
  - El personal de AutoRent dispone de una vista administrativa diferenciada para consultar todas las reservas activas (US-017) y gestionar el catálogo (US-018 a US-021), simulada dentro del prototipo sin implementar sistemas complejos de autenticación ni gestión de identidades externa.
  ---

## Hallazgo F-05 (Severidad: MINOR)
- **Descripción:** Posible solapamiento funcional entre historias de consulta y validación de disponibilidad (US-002, US-006 y US-013).
- **Decisión del equipo:** ACCEPTED_WITH_CHANGES (Aceptada con cambios)
- **Justificación y acuerdo:**
  Se preserva la separación de las tres historias para no alterar la granularidad ni el catálogo ya estimado, delimitando con precisión su alcance:
  - US-002 opera como filtro masivo del catálogo según rango de fechas.
  - US-006 comprueba y muestra el estado específico en la ficha de detalle del vehículo.
  - US-013 actúa exclusivamente como manejador de error/excepción cuando sobreviene un cambio de estado concurrente durante el flujo de reserva.

  ## Decisiones posteriores al RECHECK

### F-06 — Evidencia de pruebas funcionales frente a M-01/M-02

**Decisión:** ACCEPTED_WITH_CHANGES

**Justificación:**  
El equipo acepta la observación. Las pruebas funcionales deterministas y las
mediciones de tiempo de respuesta se consideran evidencia técnica complementaria,
pero no sustituyen la evaluación con participantes definida para M-01 y M-02.

El procedimiento de evaluación con participantes queda definido en
`specs/product/goals.md`.

### F-07 — Origen del identificador del vehículo

**Decisión:** ACCEPTED

**Justificación:**  
El equipo decide que el identificador único de cada vehículo será generado
automáticamente por CityDrive durante el alta.

El personal de AutoRent no introducirá manualmente dicho identificador.
Esta decisión ya se encuentra reflejada en US-018.