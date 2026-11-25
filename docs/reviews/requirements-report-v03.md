# Requirements review v03

## 1. Metadatos de ejecución

- **Baseline/snapshot:** Las seis especificaciones EP-001–EP-006 declaran `Catálogo V0 - Semana 2`. `specs/product/goals.md` no declara una versión. No se proporcionó otro snapshot.
- **Commit:** No proporcionado.
- **Fecha/hora:** 2026-10-12 14:01 (UTC+02:00; indicada en la invocación).
- **Agente:** `.github/agents/requirements-reviewer.agent.md`; el archivo no declara versión.
- **Modelo/herramienta:** Modelo no indicado. Lectura y creación/verificación del informe con las herramientas disponibles; no se ejecutaron comandos ni pruebas.
- **Modo:** RECHECK.
- **Alcance:** Catálogo completo indicado en la invocación: EP-001–EP-006, US-001–US-021; misión, objetivos, constitución, DoR y DoD. Revisión de F-01–F-07 del informe v02 frente a las fuentes actuales y al registro humano v01; inspección de modificaciones relevantes para identificar hallazgos nuevos.
- **Idioma:** Español.

## 2. Manifiesto de fuentes y limitaciones

### Fuentes leídas

| Ruta | Papel y secciones revisadas | Baseline/versión |
|---|---|---|
| `.github/agents/requirements-reviewer.agent.md` | Protocolo, estados RECHECK, severidad, DoR, formato y versionado | Sin versión declarada |
| `docs/reviews/requirements-report-v01.md` | Hallazgos F-01–F-05 originales, alcance, matriz DoR y preguntas | Informe v01 |
| `docs/reviews/requirements-report-v02.md` | Recheck anterior, F-01–F-07, matrices, evidencias y preguntas | Informe v02 |
| `docs/reviews/human-review-report-v01.md` | Decisiones humanas registradas para F-01–F-05 | Semana 3; sin versión formal |
| `specs/product/goals.md` | Objetivos/métricas, stakeholders, alcance, modelo mínimo, exclusiones, supuestos, restricciones, verificación y trazabilidad | Sin versión declarada |
| `specs/product/mission.md` | Misión, problema, usuarios y experiencia deseada | Sin versión declarada |
| `.specify/memory/constitution.md` | Principios, estándares y gobernanza | Sin versión declarada |
| `docs/quality/definition-of-ready.md` | Los 14 criterios reales del DoR | Sin versión declarada |
| `docs/quality/definition-of-done.md` | Condiciones de terminado | Sin versión declarada |
| `specs/EP-001 - Búsqueda de vehículos/spec.md` | Boundary, outcome, US-001–US-003 y verificaciones | Catálogo V0 - Semana 2 |
| `specs/EP-002 - Filtrado y consulta de vehículos/spec.md` | Boundary, outcome, US-004–US-006 y verificaciones | Catálogo V0 - Semana 2 |
| `specs/EP-003 - Creación de reservas/spec.md` | Boundary, outcome, US-007–US-010 y verificaciones | Catálogo V0 - Semana 2 |
| `specs/EP-004 - Control de disponibilidad y conflictos/spec.md` | Boundary, outcome, US-011–US-013 y verificaciones | Catálogo V0 - Semana 2 |
| `specs/EP-005 - Consulta y gestión de reservas/spec.md` | Boundary, outcome, US-014–US-017 y verificaciones | Catálogo V0 - Semana 2 |
| `specs/EP-006 - Gestión del catálogo de vehículos/spec.md` | Boundary, outcome, US-018–US-021 y verificaciones | Catálogo V0 - Semana 2 |

Se inspeccionó `docs/reviews/` para el siguiente nombre libre. Existían `requirements-report-v01.md` y `requirements-report-v02.md`, además de otros informes con distinto patrón.

### Limitaciones y precedencia

- Se revisaron únicamente los archivos enumerados; no se inspeccionaron código, pruebas ejecutadas, planes, tareas, otros artefactos ni historial de cambios.
- No se proporcionó commit ni una lista autoritativa de modificaciones desde v02. Las diferencias se determinan mediante la comparación textual de los informes y fuentes leídos, no por historial.
- El DoD se revisó como requisito compartido; no se evaluó cumplimiento de implementación porque no se proporcionó evidencia de implementación.
- El registro humano v01 documenta decisiones para F-01–F-05, pero no decisiones para F-06/F-07. No se presupone una decisión posterior.
- La constitución declara precedencia sobre los demás documentos. No se encontró una regla de precedencia entre objetivos y especificaciones de historias. Por tanto, la ambigüedad del vínculo entre `goals.md` y US-009 se registra, no se resuelve por inferencia.

## 3. Evaluación del alcance revisado

**Recomendación: NO_BLOCKING_FINDINGS_IN_REVIEWED_SCOPE.**

**Alcance exacto:** EP-001–EP-006 y US-001–US-021, contrastados con misión, objetivos/alcance, constitución, DoR y DoD; recheck de F-01–F-07 del informe v02 y de las decisiones humanas F-01–F-05.

**Bloqueadores confirmados:** No se identificaron. F-06 permanece parcialmente resuelto como QUESTION, no como defecto confirmado: `goals.md` ahora distingue expresamente la evaluación con cinco participantes para M-01/M-02 de las pruebas funcionales y mediciones de rendimiento. US-009 todavía declara que “La verificación del flujo de confirmación servirá como evidencia para las métricas M-01 y M-02”. La frase podría referirse a evidencia técnica complementaria, compatible con la advertencia de goals de que esas pruebas no son suficientes por sí solas, pero no lo aclara. US-002 y US-003 ya no hacen esa atribución en sus textos actuales. La evidencia disponible no basta para afirmar que US-009 contradiga los objetivos ni que la prueba funcional se considere evidencia suficiente.

F-01, F-02, F-04, F-05 y F-07 quedan resueltos con evidencia en las fuentes actuales. F-03 permanece parcialmente resuelto: los resultados de usabilidad asociados a M-01/M-02 y la comprobación de rendimiento están mejor definidos, pero las expectativas de accesibilidad derivadas de la constitución no cuentan con condiciones observables específicas en el catálogo revisado. No se considera un bloqueo independiente.

La recomendación no aprueba el baseline, una puerta de calidad ni la completitud general del producto. Las fuentes esenciales indicadas fueron accesibles; la pregunta residual F-06 y la limitación no bloqueante F-03 no impiden una evaluación global fiable del alcance.

## 4. Matriz de cobertura

| Dimensión | IDs/artefactos inspeccionados | Resultado | Hallazgos |
|---|---|---|---|
| Claridad y consistencia | EP-001–EP-006; US-001–US-021; goals, misión, registro humano y F-01–F-07 | Los campos comunes, el límite de acceso simulado y el flujo concurrente están precisados. La función probatoria de US-009 para M-01/M-02 queda ambigua, aunque puede ser evidencia complementaria según goals. | F-03, F-06 |
| Cobertura y alineación de alcance | G-01–G-03, M-01–M-04, S-01–S-03, EX-01–EX-03; seis épicas | Búsqueda, reserva, gestión básica y stakeholders principales están representados. No se localizó en las seis épicas el requisito detallado que permite evaluar M-03. | Pregunta de alcance §7 |
| Elementos ausentes de especificación | US-001–US-021; modelo y verificación transversal de goals; constitución; DoR/DoD | El modelo mínimo, la regla de conflicto y el origen automático del ID están descritos. Subsiste precisión pendiente sobre accesibilidad; la evidencia de usabilidad está desarrollada en goals pero contradicha por US-009. | F-03, F-06 |
| Tamaño y granularidad (heurística INVEST) | US-001–US-021; boundaries EP-001–EP-006 | Se mantienen resultados por historia inspectables; la separación búsqueda masiva/detalle/conflicto está explicitada. No se recomienda dividir ni fusionar historias. | F-05 RESOLVED |
| Criterios de aceptación y DoR | US-001–US-021; 14 criterios de `definition-of-ready.md` | Los criterios funcionales son observables; queda una pregunta no bloqueante sobre si US-009 cita evidencia técnica complementaria o la evaluación completa de M-01/M-02. | F-06; matriz §6 |
| Dependencias y supuestos | Predecesores US-001–US-021; supuestos/restricciones de goals y contratos entre épicas | La revalidación, el rechazo, el retorno a fechas y la conservación de filtros están expresos. No se encontró ciclo entre predecesores declarados. | F-02 RESOLVED; brecha de evidencia F-06 |

## 5. Hallazgos

### Índice de hallazgos del recheck

| ID previo | Estado RECHECK | Severidad actual | Categoría | Referencias |
|---|---|---|---|---|
| F-01 | RESOLVED | — | Modelo de datos/verificabilidad | goals; US-005, US-008, US-018, US-019, US-021 |
| F-02 | RESOLVED | — | Disponibilidad/recuperación | US-009, US-012, US-013 |
| F-03 | PARTIALLY_RESOLVED | MINOR, residual | NFR/usabilidad y accesibilidad | Constitución principio 5; misión; goals M-01/M-02 |
| F-04 | RESOLVED | — | Límites de acceso | EP-005 US-014–US-017; EP-006 US-018–US-021 |
| F-05 | RESOLVED | — | Fronteras/granularidad | US-002, US-006, US-013 |
| F-06 | PARTIALLY_RESOLVED | QUESTION, residual no bloqueante | Evidencia de métricas y trazabilidad | goals M-01/M-02; US-009 |
| F-07 | RESOLVED | — | Origen del ID de vehículo | US-018 |

`—` indica que no queda un defecto confirmado de ese hallazgo anterior en el texto actual; no supone aprobación de las historias.

### F-01 — Modelo de campos de vehículo y reserva

- **Referencia anterior:** F-01, `requirements-report-v01.md` §5; decisión humana en `human-review-report-v01.md`, F-01.
- **Estado:** **RESOLVED**.
- **Categoría:** Modelo de datos, reglas y verificabilidad.
- **Decisión humana:** ACCEPTED; se acordó un modelo sintético común.
- **Fuentes e IDs:** `specs/product/goals.md`, “Modelo mínimo de datos sintéticos”; `specs/EP-002 - Filtrado y consulta de vehículos/spec.md`, US-005 AC-02; `specs/EP-003 - Creación de reservas/spec.md`, US-008 AC-01–04; `specs/EP-006 - Gestión del catálogo de vehículos/spec.md`, US-018 AC-02–05, US-019 y US-021.
- **Extracto:** goals enumera “id, marca, modelo, categoría, plazas, maletero/carga, transmisión y estado operativo” para vehículo, y los campos de reserva; US-005 AC-02 lista las características mostradas.
- **Evidencia actual:** El modelo de goals enumera campos de vehículo y reserva. Las historias pertinentes lo invocan o concretan para consulta, captura, alta, modificación y visualización.
- **Observación/impacto:** La ausencia de un esquema común que motivó F-01 ya no está en las fuentes actuales. No se vuelve a abrir el hallazgo por detalles que no formaban parte de la brecha original.
- **Acción:** Ninguna necesaria para cerrar F-01.
- **Confianza:** HIGH; el modelo está enumerado y las historias pertinentes lo invocan o concretan.
- **Bloqueador:** No.

### F-02 — Conflicto de disponibilidad y camino de recuperación

- **Referencia anterior:** F-02, `requirements-report-v01.md` §5 y `requirements-report-v02.md` §5; decisión humana F-02.
- **Estado:** **RESOLVED**.
- **Categoría:** Regla de negocio, disponibilidad y dependencias.
- **Decisión humana:** ACCEPTED; revalidación definitiva, una operación funcional que evita doble confirmación, rechazo/notificación y vuelta a fechas conservando filtros.
- **Fuentes e IDs:** `specs/EP-003 - Creación de reservas/spec.md`, US-009 AC-04–07 y Verification; `specs/EP-004 - Control de disponibilidad y conflictos/spec.md`, US-012 AC-03–05 y US-013 AC-01–05 y Verification.
- **Extracto:** US-013 AC-03: “volver a la selección de fechas”; AC-04: “estos se conservan”.
- **Evidencia actual:** EP-003 US-009 AC-04–07 y Verification definen la revalidación en confirmación, rechazo y exclusión de dos confirmaciones incompatibles. EP-004 US-012 AC-03–05 define el resultado concurrente y el intervalo inclusivo. US-013 AC-03 dice que el usuario vuelve a la selección de fechas; AC-04 establece que se conservan los filtros, y Verification repite ambas condiciones.
- **Observación/impacto:** La omisión residual identificada en v02 coincide con la intención registrada por el equipo y se encuentra atendida en el texto actual. No se prescribe tecnología ni se infiere implementación.
- **Acción:** Ninguna necesaria para cerrar el hallazgo.
- **Confianza:** HIGH; criterios de aceptación y restricciones de recuperación son explícitos.
- **Bloqueador:** No.

### F-03 — NFR, usabilidad y accesibilidad

- **Referencia anterior:** F-03, `requirements-report-v01.md` §5 y `requirements-report-v02.md` §5; decisión humana F-03.
- **Estado:** **PARTIALLY_RESOLVED**.
- **Categoría:** Requisito no funcional y verificabilidad.
- **Decisión humana:** ACCEPTED_WITH_CHANGES; respuesta observable <2 s en entorno local, pruebas deterministas con datos sintéticos y exclusión de pruebas industriales de carga/estrés.
- **Fuentes e IDs:** `specs/product/goals.md`, “Criterios transversales de verificación” y “Evidencia de las métricas M-01 y M-02”; `.specify/memory/constitution.md`, principio 5; `specs/product/mission.md`, “Experiencia deseada”; EP-001–EP-006, criterios y verificaciones de historias.
- **Extracto:** La constitución exige que los flujos y errores consideren “la diversidad de usuarios”; la misión califica la experiencia como “accesible”.
- **Evidencia actual:** goals fija <2 s, pruebas deterministas y evaluación de comprensión/completitud con participantes. En las seis épicas revisadas no se encontraron criterios concretos para evaluar accesibilidad.
- **Observación:** Rendimiento y aspectos de usabilidad de las métricas tienen mayor precisión que en las revisiones anteriores. Sigue sin quedar observable qué aspectos de accesibilidad exige el MVP ni qué evidencia los comprobará. No se infiere un estándar, umbral ni obligación externa.
- **Impacto:** La evaluación de accesibilidad podría diferir entre revisores. Este residual no impide compartir la interpretación de los criterios funcionales expresos, pero deja incompleta la trazabilidad del principio transversal.
- **Acción sugerida:** Acordar, si aplica al alcance actual, los aspectos de accesibilidad a verificar y su evidencia, sin inferir un estándar externo.
- **Confianza:** MEDIUM; la obligación general está en la constitución, pero el alcance de su operacionalización no se determina en las fuentes.
- **Bloqueador:** No.

### F-04 — Límites de acceso de clientes y personal

- **Referencia anterior:** F-04, `requirements-report-v01.md` §5 y `requirements-report-v02.md` §5; decisión humana F-04.
- **Estado:** **RESOLVED**.
- **Categoría:** Límites de acceso y privacidad.
- **Decisión humana:** ACCEPTED; cliente consulta/cancela mediante referencia y el personal usa vistas administrativas diferenciadas, sin autenticación compleja/externa en el prototipo.
- **Fuentes e IDs:** `specs/EP-005 - Consulta y gestión de reservas/spec.md`, Boundary y US-014/US-016/US-017; `specs/EP-006 - Gestión del catálogo de vehículos/spec.md`, Boundary y US-018–US-021.
- **Extracto:** EP-005 Boundary: “la referencia única de la reserva actúa como mecanismo funcional”; las funciones del personal se presentan mediante “una vista administrativa diferenciada”.
- **Evidencia actual:** US-014/US-016 describen consulta/cancelación por referencia; US-017 y EP-006 US-018–US-021 describen funciones administrativas diferenciadas y excluyen autenticación compleja o externa.
- **Observación/impacto:** Los límites de producto pedidos están reflejados. La especificación no pretende definir una solución de identidad de producción, y esta revisión no la evalúa como tal.
- **Acción:** Ninguna necesaria para cerrar el hallazgo; preservar los límites explícitos de datos ficticios y alcance.
- **Confianza:** HIGH; evidencia directa en boundaries, criterios y restricciones.
- **Bloqueador:** No.

### F-05 — Solapamiento entre búsqueda, ficha y conflicto concurrente

- **Referencia anterior:** F-05, `requirements-report-v01.md` §5 y `requirements-report-v02.md` §5; decisión humana F-05.
- **Estado:** **RESOLVED**.
- **Categoría:** Consistencia, granularidad y propiedad de criterios.
- **Decisión humana:** ACCEPTED_WITH_CHANGES; separar búsqueda masiva, disponibilidad de un vehículo concreto y gestión de error concurrente.
- **Fuentes e IDs:** `specs/EP-001 - Búsqueda de vehículos/spec.md`, US-002 Verification; `specs/EP-002 - Filtrado y consulta de vehículos/spec.md`, US-006 Verification; `specs/EP-004 - Control de disponibilidad y conflictos/spec.md`, US-013 Verification.
- **Extracto:** US-006 dice que “no sustituye a la revalidación definitiva”; US-013 limita su responsabilidad a “informar y permitir recuperar el flujo” ante el conflicto.
- **Evidencia actual:** US-002 atribuye la consulta general; US-006 delimita la disponibilidad de un vehículo concreto; US-013 limita su responsabilidad a informar y recuperar el flujo tras el conflicto.
- **Observación/impacto:** Las fronteras y el momento de la revalidación están expresos. No se identifica duplicación ambigua que justifique fusionar historias.
- **Acción:** Ninguna necesaria para cerrar el hallazgo.
- **Confianza:** HIGH; límites explícitos en las tres historias.
- **Bloqueador:** No.

### F-06 — Evidencia de pruebas funcionales frente a M-01/M-02

- **Referencia anterior:** F-06, `requirements-report-v02.md` §5.
- **Estado:** **PARTIALLY_RESOLVED**.
- **Categoría:** Trazabilidad, medición de objetivos y verificabilidad.
- **Decisión humana:** No consta una decisión humana sobre F-06 en `human-review-report-v01.md`; no se atribuye ninguna.
- **Fuentes e IDs:** `specs/product/goals.md`, “Evidencia de las métricas M-01 y M-02”; `specs/EP-003 - Creación de reservas/spec.md`, US-009 Verification; `specs/EP-001 - Búsqueda de vehículos/spec.md`, US-002/US-003 Verification.
- **Evidencia actual, lado de objetivos:** `specs/product/goals.md`, sección “Evidencia de las métricas M-01 y M-02”, distingue que “Las pruebas funcionales y las mediciones de tiempo de respuesta […] no constituyen por sí solas evidencia suficiente” y especifica cinco participantes, finalización sin ayuda/tiempo para M-01, comprobación de comprensión para M-02 y conservación separada de resultados.
- **Evidencia actual, lado de historia:** EP-003 US-009 Verification dice: “La verificación del flujo de confirmación servirá como evidencia para las métricas M-01 y M-02 definidas en `specs/product/goals.md`”. En la misma historia, la verificación se describe como determinista, con datos sintéticos y una condición de respuesta <2 s. EP-001 US-002/US-003 ya no atribuye a esas pruebas la medición de métricas en el texto actual.
- **Observación:** La nueva sección de goals aborda el defecto de método que motivó F-06, y la retirada de esa atribución de US-002/US-003 es evidencia de avance. US-009 dice que la verificación de confirmación “servirá como evidencia”, pero no precisa si se refiere a evidencia técnica complementaria a la evaluación de participantes o a evidencia suficiente por sí sola. La segunda lectura no concuerda con goals; el texto no indica explícitamente que esa sea la intención.
- **Impacto:** Puede persistir una interpretación distinta sobre el aporte de la verificación de US-009 a M-01/M-02. La metodología principal, incluidos participantes y resultados requeridos, ya está definida en goals; por eso no se confirma que la falta de precisión impida verificar las métricas.
- **Acción sugerida:** Aclarar si la verificación técnica de US-009 es evidencia complementaria, separada de la evaluación de participantes descrita en goals. No cambiar métricas, método ni alcance por inferencia.
- **Confianza:** MEDIUM; las dos afirmaciones son compatibles si la de US-009 se entiende como evidencia complementaria, pero el vínculo no está explícito.
- **Bloqueador:** No; QUESTION por ambigüedad residual, sin bloqueo confirmado.

### F-07 — Origen del identificador al dar de alta un vehículo

- **Referencia anterior:** F-07, `requirements-report-v02.md` §5.
- **Estado:** **RESOLVED**.
- **Categoría:** Claridad y regla de datos.
- **Decisión humana:** No consta decisión para F-07 en `human-review-report-v01.md`; el cierre se basa en la evidencia actual, no en una decisión humana supuesta.
- **Fuente e ID:** `specs/EP-006 - Gestión del catálogo de vehículos/spec.md`, US-018 AC-05 y Verification and constraints.
- **Extracto:** “el sistema genera automáticamente un identificador único”; “no es introducido manualmente por el personal”.
- **Evidencia actual:** US-018 AC-05 especifica que el sistema genera automáticamente el ID al registrar datos válidos; Verification exige unicidad y que no se modifique mediante mantenimiento.
- **Observación/impacto:** La ambigüedad anterior sobre quién proporciona o genera el ID queda resuelta; la unicidad es un resultado explícito de aceptación. El flujo ya no requiere una regla de entrada manual para IDs duplicados.
- **Acción:** Ninguna necesaria para cerrar la pregunta original.
- **Confianza:** HIGH; asignación automática y unicidad aparecen expresamente.
- **Bloqueador:** No.

## 6. Matriz DoR

Se evaluaron los **14 criterios reales** de `docs/quality/definition-of-ready.md`, en este orden:

1. ID único/estable; 2. asociación a épica; 3. trazabilidad a objetivo; 4. usuario o stakeholder identificado; 5. capacidad descrita; 6. valor comprensible; 7. alcance/límites claros; 8. aceptación observable/verificable; 9. prioridad; 10. estimación; 11. incertidumbre; 12. dependencias/predecesores; 13. restricciones relevantes; 14. ausencia de dudas que impidan comprender/planificar.

**Estados:** MET, NOT_MET, NOT_ASSESSABLE, NOT_APPLICABLE. Para cada criterio se muestra el estado; en las filas que no son US-009, los 14 criterios son MET. La evidencia específica de cada fila se da en la última columna. En US-009, el criterio 8 es NOT_MET únicamente respecto de la afirmación inconsistente de que la verificación funcional aporta evidencia de M-01/M-02; los criterios funcionales de confirmación permanecen observables. No se evaluó cumplimiento del DoD.

| Historia | Criterios 1–7 | Criterio 8 | Criterios 9–14 | Evidencia de MET / explicación de NOT_MET |
|---|---|---|---|---|
| US-001 | MET | MET | MET | EP-001 US-001: ID/actor/capacidad/valor, fechas y validaciones AC-01–06; prioridad, estimación, incertidumbre y predecesores declarados; restricciones y prueba de fechas válidas/inválidas. |
| US-002 | MET | MET | MET | EP-001 US-002: disponibilidad por rango, errores sin resultado y <2 s en AC-01–05; predecesor US-001 y pruebas deterministas sintéticas. No mantiene la atribución anterior de prueba técnica como evidencia de M-01/M-02. |
| US-003 | MET | MET | MET | EP-001 US-003 AC-01–03 define mensaje y edición de fechas; Verification especifica prueba determinista de cero resultados y retorno al formulario. |
| US-004 | MET | MET | MET | EP-002 US-004 AC-01–05 define selección, eliminación y filtro sin resultados; Verification fija coches/furgonetas y prueba sintética. |
| US-005 | MET | MET | MET | EP-002 US-005 AC-02 enumera campos; AC-03–05 verifica correspondencia, etiquetas y respuesta; goals fija el modelo común. |
| US-006 | MET | MET | MET | EP-002 US-006 AC-01–04 y Verification delimitan disponibilidad de un vehículo concreto, reservas/estado manual y revalidación final separada. |
| US-007 | MET | MET | MET | EP-003 US-007 AC-01–03 y Verification describen selección de vehículo disponible y retención en el flujo. |
| US-008 | MET | MET | MET | EP-003 US-008 AC-01–04 enumera datos requeridos, validación de presencia, mensajes y asociación; Verification define pruebas de campo omitido y datos ficticios. |
| US-009 | MET | MET | MET | EP-003 US-009 AC-01–08 hace observable confirmación, concurrencia y respuesta técnica; prioridad, estimación, incertidumbre y predecesores constan. La frase de Evidence sobre M-01/M-02 se evalúa como una pregunta de trazabilidad no bloqueante (F-06), no como fallo de observabilidad de los criterios funcionales. |
| US-010 | MET | MET | MET | EP-003 US-010 AC-01–04 define referencia, unicidad, presentación y localización; Verification exige evitar duplicados y da formato ilustrativo. |
| US-011 | MET | MET | MET | EP-004 US-011 AC-01–04 define bloqueo tras confirmación, intervalo afectado y reservas que cuentan; restricciones de coherencia explícitas. |
| US-012 | MET | MET | MET | EP-004 US-012 AC-01–05 define comprobación, rechazo, concurrencia y no solapamiento; Verification precisa días inclusivos y ejemplo límite. |
| US-013 | MET | MET | MET | EP-004 US-013 AC-01–05 define rechazo, mensaje, retorno a fechas, retención de filtros y protección de la reserva existente; Verification reafirma el contexto conservado. |
| US-014 | MET | MET | MET | EP-005 Boundary y US-014 AC-01–05 establecen consulta por referencia, existente/inexistente, no modificación y respuesta <2 s; Verification incluye pruebas de ambos casos. |
| US-015 | MET | MET | MET | EP-005 US-015 AC-01–06 identifica vehículo, fechas, estado, pertenencia, etiquetas y respuesta; Verification limita datos a la reserva localizada. |
| US-016 | MET | MET | MET | EP-005 US-016 AC-01–05 define cancelación, estado activo, disponibilidad resultante y error; Verification incluye casos cancelable/no cancelable. |
| US-017 | MET | MET | MET | EP-005 US-017 AC-01–05 identifica personal, vista administrativa, datos activos y exclusión de canceladas; Verification aclara la simulación de acceso. |
| US-018 | MET | MET | MET | EP-006 US-018 AC-01–06 define alta, campos, errores, ID automático único y uso posterior; Verification fija el origen automático, datos ficticios y casos de alta/campo ausente. |
| US-019 | MET | MET | MET | EP-006 US-019 AC-01–05 enumera campos editables y valida cambio/no válido conservando valores; Verification excluye ID/estado y define prueba de ambos casos. |
| US-020 | MET | MET | MET | EP-006 US-020 AC-01–05 define cambio de estado en ambas direcciones y persistencia; Verification enlaza el efecto a búsquedas y consultas. |
| US-021 | MET | MET | MET | EP-006 US-021 AC-01–06 enumera campos visibles, correspondencia y respuesta; Verification establece modelo de datos, vista simulada y pruebas sintéticas. |

**Evidencia común de los estados MET:** Las 21 historias tienen ID estable, secciones dentro de una épica que declara Goals, y texto de usuario/capacidad/valor. Cada una contiene prioridad, estimación, incertidumbre y campo de predecesores explícito (incluido `—` en US-001 y US-018), además de criterios de aceptación y restricciones/verificación en las referencias indicadas. Los límites generales de datos sintéticos y alcance se contrastaron con goals y la constitución. Esta evaluación es del texto del DoR, no de planificación, implementación ni calidad final.

**Elementos diferidos separados del DoR:** Las 21 historias indican `Initial plan: Pendiente de asignación en la planificación de la Semana 3`. Se conserva como dato de planificación declarado; no se transforma en una decisión ni en un fallo adicional del DoR. Prioridades, estimaciones y planes no se modificaron.

## 7. Candidatos de omisiones y preguntas de alcance

Estos puntos no son hallazgos confirmados ni bloqueadores y no repiten F-03/F-06.

| Etiqueta | Candidato/pregunta | Racional y fuente | Pregunta humana |
|---|---|---|---|
| IN_SCOPE_CANDIDATE | Requisito detallado verificable para que un tercero instale, ejecute y evalúe el incremento | `goals.md` G-03/M-03; no localizado en las seis épicas leídas. Puede residir en otro artefacto no proporcionado. | ¿En qué fuente se especifican la instalación, ejecución y evaluación de M-03 y cuál es su referencia verificable? |
| SCOPE_UNCLEAR | Resultado específico para Dirección de AutoRent | Stakeholder declarado en `goals.md`; no se encontró en EP-001–EP-006 una historia dirigida específicamente a Dirección. | ¿El resultado de catálogo y reservas satisface las necesidades de Dirección para este alcance o se espera otro resultado? |
| OUT_OF_SCOPE | Pagos/facturación reales, aseguradoras, hardware/IoT, GPS y mantenimiento físico | `goals.md` EX-01–EX-03 y boundaries de EP-003/EP-004/EP-006 los excluyen. | ¿Se mantienen estas exclusiones para el alcance actual? No se recomienda añadirlas sin una decisión explícita de cambio de alcance. |

## 8. Dependencias, supuestos y brechas de trazabilidad

- **Prerrequisitos declarados:** US-001 → US-002 → US-003; US-002 precede a US-004/US-005/US-006 y US-007; US-007 → US-008; US-009 depende de US-007, US-008 y US-012; US-010 sigue a US-009; US-011 depende de US-009 y US-012; US-013 depende de US-012; US-014 depende de US-010; US-015/US-016 dependen de US-014; US-017 depende de US-009; US-018 precede a US-019/US-020/US-021. Se mantienen los IDs y relaciones textuales.
- **Ciclos:** No se encontró ciclo en los predecesores expresos de US-001–US-021.
- **Contrato compartido:** La disponibilidad combina reservas activas, intervalo por días (incluyente), estado manual del vehículo y cancelación (US-002, US-006, US-011, US-012, US-016, US-020). F-02 se resuelve a nivel de criterios: revalidación, rechazo, notificación y recuperación con filtros. No se atribuye comportamiento técnico de implementación.
- **Métrica/evidencia:** `goals.md` asigna evidencia de participante a M-01/M-02 y la separa de las pruebas técnicas. La declaración de US-009 no especifica si el vínculo a esas métricas es evidencia adicional o suficiente (F-06). La cadena de trazabilidad no se verificó más allá de las fuentes proporcionadas.
- **Secuenciación:** “Initial plan” indica pendiente de planificación para todas las historias. Es estado declarado de planificación, no dependencia funcional ni decisión de calendario.
- **Dependencias de datos:** El modelo sintético común de vehículo/reserva está en goals; el ID de alta se genera automáticamente (F-01/F-07 RESOLVED).
- **Dependencias externas:** goals asume que no se necesitan sistemas externos para disponibilidad; EP-004/EP-006 excluyen sistemas externos e IoT. No se presume otra integración.
- **Supuestos:** Datos ficticios, agencia AutoRent, reserva exclusiva por vehículo durante intervalos incompatibles, navegador actualizado e Internet. No se encontró contradicción textual nueva respecto a esos supuestos.
- **Suposición no confirmada:** No se infiere ningún proveedor externo, autenticación, tecnología, sistema de identidad ni dependencia no mencionada.
- **DoD:** Se leyó el DoD compartido; sin evidencia de implementación no se afirma cumplimiento.

## 9. Preguntas para el equipo humano

1. **Prioridad media — F-06 / US-009:** ¿La verificación funcional de US-009 pretende ser evidencia técnica complementaria, aparte de la evaluación con participantes definida en goals? Si es así, ¿conviene explicitarlo para evitar que se interprete como evidencia suficiente por sí sola?
2. **Prioridad media — F-03:** ¿Qué aspectos de accesibilidad son exigibles en el MVP y qué evidencia observable se aceptará, sin inferir un estándar o umbral?
3. **Prioridad media — M-03:** ¿En qué fuente se especifica el resultado de instalación/ejecución por un tercero?
4. **Prioridad media — Stakeholder:** ¿Dirección de AutoRent requiere una salida funcional explícita dentro de estas épicas o queda atendida por los resultados ya descritos?
5. **Prioridad baja — Cierre:** ¿Se mantienen las exclusiones EX-01–EX-03 y los límites sobre IoT/GPS y mantenimiento físico para el alcance revisado?

F-01, F-02, F-04, F-05 y F-07 no requieren preguntas adicionales para cerrar sus hallazgos anteriores según la evidencia disponible.

## 10. RECHECK crosswalk

| Hallazgo previo | Decisión humana en la fuente leída | Evidencia actual | Estado |
|---|---|---|---|
| F-01 | ACCEPTED en human-review-report-v01: modelo sintético común | goals enumera campos; US-005/008/018/019/021 los usan o concretan | **RESOLVED** |
| F-02 | ACCEPTED en human-review-report-v01: revalidación, rechazo, aviso, retorno a fechas con filtros | US-009/012 describen exclusión mutua; US-013 AC-03/04 y Verification especifican retorno y filtros | **RESOLVED** |
| F-03 | ACCEPTED_WITH_CHANGES en human-review-report-v01: <2 s y pruebas deterministas, sin carga/estrés industriales | goals especifica comprobaciones técnicas y evaluación de M-01/M-02; no se hallan criterios observables específicos de accesibilidad | **PARTIALLY_RESOLVED** |
| F-04 | ACCEPTED en human-review-report-v01: referencia individual y vista administrativa simulada | Boundaries y criterios de EP-005/EP-006 reflejan esos límites | **RESOLVED** |
| F-05 | ACCEPTED_WITH_CHANGES en human-review-report-v01: separación de las tres responsabilidades | US-002, US-006 y US-013 definen límites separados | **RESOLVED** |
| F-06 | No consta decisión humana para este hallazgo en human-review-report-v01 | goals ahora distingue evaluación de participantes y pruebas funcionales; US-002/003 ya no atribuyen evidencia de métricas a sus pruebas. US-009 conserva una atribución que puede ser complementaria, pero no precisa esa relación | **PARTIALLY_RESOLVED** |
| F-07 | No consta decisión humana para este hallazgo en human-review-report-v01 | US-018 expresa generación automática por CityDrive y unicidad | **RESOLVED** |

No se asigna JUSTIFIABLY_REJECTED ni DEFERRED: no hay una decisión humana en el registro revisado que justifique esos estados. Las decisiones ACCEPTED/ACCEPTED_WITH_CHANGES de F-01–F-05 se contrastan con la fuente actual; la aceptación de una sugerencia no se toma como evidencia de corrección. No se identificó una resolución humana incompatible con la constitución.

## 11. Cierre explícito

Este es un informe consultivo. No se modificó ningún requisito fuente, prioridad, estimación, plan ni decisión humana. No se aprobó ningún baseline ni gate.
