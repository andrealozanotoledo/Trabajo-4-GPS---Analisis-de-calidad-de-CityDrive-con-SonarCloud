# Requirements review v02

## 1. Metadatos de ejecución

- **Baseline/snapshot:** Las seis especificaciones declaran `Catálogo V0 - Semana 2`; `specs/product/goals.md` no declara versión. No se proporcionó un snapshot adicional.
- **Commit:** No proporcionado.
- **Fecha/hora:** 2026-10-12 13:51 (UTC+02:00; hora proporcionada en la invocación).
- **Agente:** `.github/agents/requirements-reviewer.agent.md`; el archivo no declara versión.
- **Modelo/herramienta:** Modelo no indicado. Lectura de fuentes y creación/verificación del informe mediante las herramientas disponibles; no se ejecutaron comandos ni pruebas.
- **Modo:** RECHECK.
- **Alcance:** Catálogo completo especificado, EP-001–EP-006 y US-001–US-021; reevaluación de F-01–F-05 del informe v01 frente al registro humano v01 y las fuentes actuales explícitamente indicadas.
- **Idioma:** Español.

## 2. Manifiesto de fuentes y limitaciones

### Fuentes leídas

| Ruta | Papel/secciones revisadas | Baseline/versión declarada |
|---|---|---|
| `.github/agents/requirements-reviewer.agent.md` | Protocolo, estados RECHECK, severidad, DoR, formato y persistencia | Sin versión declarada |
| `docs/reviews/requirements-report-v01.md` | Informe INITIAL, F-01–F-05, evaluación, matriz DoR, omisiones y dependencias | v01 |
| `docs/reviews/human-review-report-v01.md` | Decisiones humanas y acuerdos para F-01–F-05 | Semana 3; sin versión formal declarada |
| `.specify/memory/constitution.md` | Principios, estándares, calidad y gobernanza | Sin versión declarada |
| `specs/product/mission.md` | Misión, problema, stakeholders y experiencia | Sin versión declarada |
| `specs/product/goals.md` | Objetivos, métricas, stakeholders, alcance, modelo mínimo de datos, exclusiones, supuestos, restricciones, verificación y trazabilidad | Sin versión declarada |
| `docs/quality/definition-of-ready.md` | Los 14 criterios reales del DoR | Sin versión declarada |
| `docs/quality/definition-of-done.md` | Condiciones de terminado | Sin versión declarada |
| `specs/EP-001 - Búsqueda de vehículos/spec.md` | Boundary, outcome y US-001–US-003 | Catálogo V0 - Semana 2 |
| `specs/EP-002 - Filtrado y consulta de vehículos/spec.md` | Boundary, outcome y US-004–US-006 | Catálogo V0 - Semana 2 |
| `specs/EP-003 - Creación de reservas/spec.md` | Boundary, outcome y US-007–US-010 | Catálogo V0 - Semana 2 |
| `specs/EP-004 - Control de disponibilidad y conflictos/spec.md` | Boundary, outcome y US-011–US-013 | Catálogo V0 - Semana 2 |
| `specs/EP-005 - Consulta y gestión de reservas/spec.md` | Boundary, outcome y US-014–US-017 | Catálogo V0 - Semana 2 |
| `specs/EP-006 - Gestión del catálogo de vehículos/spec.md` | Boundary, outcome y US-018–US-021 | Catálogo V0 - Semana 2 |

Se inspeccionó `docs/reviews/` para determinar el siguiente número libre; existían `requirements-report-v01.md`, `human-review-report-v01.md` e `initial-planning-review-v01.md`.

### Limitaciones

- El análisis se limita a las fuentes enumeradas. No se leyeron planes, tareas, código, pruebas, datos de ejecución ni otros artefactos.
- El DoD se revisó como requisito compartido; no se evaluó cumplimiento de implementación porque no se aportó evidencia de implementación.
- El registro humano acredita decisiones/acuerdos, no demuestra por sí solo que la fuente revisada los haya incorporado.
- No se aporta historial de cambios ni commit para identificar qué modificaciones concretas ocurrieron entre revisiones.
- No se estableció una precedencia especial entre fuentes. La constitución dice que prevalece sobre los demás documentos; para contradicciones de requisitos entre objetivos/especificaciones, no se encontró una regla general documentada. Se señalan las discrepancias en lugar de resolverlas por inferencia.

## 3. Evaluación del alcance revisado

**Recomendación: NEEDS_REFINEMENT.**

**Alcance exacto:** EP-001–EP-006 y US-001–US-021 frente a misión, objetivos/alcance, constitución, DoR y DoD; además, estado de F-01–F-05 frente al informe INITIAL v01 y la decisión humana v01.

**Bloqueador confirmado en el alcance:** F-06 (nuevo), respecto a US-002, US-003 y US-009. Las historias declaran que la verificación de consulta/confirmación aportará evidencia para M-01/M-02, pero las métricas del objetivo son resultados de uso con participantes (completar el escenario sin ayuda/tiempo y comprender vehículo/fechas). Las pruebas funcionales deterministas y el tiempo de respuesta <2 s declarados en esas historias no verifican por sí solos esos resultados. Esta referencia puede llevar a aceptar como evidencia de las métricas algo que no las mide. La consulta/confirmación tiene criterios operativos verificables; el bloqueo es la evidencia declarada para la medición de los objetivos, no una afirmación de que la funcionalidad falle.

**F-01–F-05:** F-01 y F-04 resueltos en las fuentes actuales; F-02 y F-03 parcialmente resueltos; F-05 resuelto. El estado parcial de F-02 incluye una diferencia concreta entre el acuerdo humano (conservar filtros al volver a fechas) y el texto vigente. Esta diferencia no se cuenta como un segundo hallazgo separado.

La recomendación es consultiva y se limita a este catálogo; no aprueba su baseline ni declara completitud general.

## 4. Matriz de cobertura

| Dimensión | IDs/artefactos inspeccionados | Resultado | Hallazgos |
|---|---|---|---|
| Claridad y consistencia | EP-001–EP-006; US-001–US-021; objetivos, misión y decisiones F-01–F-05 | Los cambios especifican el esquema sintético y separan búsqueda, detalle y error concurrente. La evidencia para M-01/M-02 no se corresponde con las métricas; queda por aclarar la conservación de filtros pactada | F-02 (parcial), F-06 |
| Cobertura y alineación de alcance | G-01–G-03, M-01–M-04, S-01–S-03, EX-01–EX-03; EP-001–EP-006 | Recorrido esencial y administración representados. M-03 (instalación/ejecución por tercero) sigue sin requisito detallado localizado en las seis épicas revisadas | Candidato §7 |
| Elementos ausentes de especificación | Historias US-001–US-021; modelo y criterios transversales de goals; constitución; DoR/DoD | Campos de vehículo/reserva ya enumerados. Persisten preguntas locales sobre asignación del ID de vehículo, accesibilidad verificable y la evidencia de objetivos de usabilidad | F-03 (parcial), F-06; pregunta nueva |
| Tamaño y granularidad (heurística INVEST) | US-001–US-021; fronteras EP-001–EP-006 | US-002 (búsqueda masiva), US-006 (ficha concreta) y US-013 (conflicto sobrevenido) tienen límites explícitos; no se recomienda fusionarlas. Verificación de métricas se debe separar conceptualmente de pruebas funcionales | F-05 resuelto; F-06 |
| Criterios de aceptación y DoR | US-001–US-021; 14 criterios de `definition-of-ready.md` | Se evaluaron los 14 criterios por cada historia. Evidencia de elegibilidad para M-01/M-02 no queda validada por los ensayos citados; ver matriz §6 | F-06 |
| Dependencias y supuestos | Predecesores US-001–US-021; supuestos/restricciones de goals; flujos EP-003–EP-005 | Revalidación y rechazo concurrente están expresados como contrato funcional; el camino de recuperación no explicita retención de filtros. No se encontró ciclo explícito | F-02 (parcial); pregunta nueva |

## 5. Hallazgos

### Índice de hallazgos vigentes

| ID | Estado RECHECK | Severidad actual | Categoría | Referencias |
|---|---|---|---|---|
| F-01 | RESOLVED | — | Datos y verificabilidad | goals, US-005, US-008, US-018, US-019, US-021 |
| F-02 | PARTIALLY_RESOLVED | MAJOR, residual | Regla de disponibilidad/dependencias | US-009, US-012, US-013 |
| F-03 | PARTIALLY_RESOLVED | MINOR, residual | NFR/verificación | goals; US-001–US-021 y criterios transversales pertinentes |
| F-04 | RESOLVED | — | Acceso y límites del MVP | EP-005 US-014–US-017; EP-006 US-018–US-021 |
| F-05 | RESOLVED | — | Frontera funcional/granularidad | US-002, US-006, US-013 |
| F-06 | NUEVO | MAJOR | Trazabilidad y validez de evidencia para métricas | goals M-01/M-02; US-002, US-003, US-009 |
| F-07 | NUEVO | QUESTION | Alcance de alta de vehículo | US-018 |

`—` significa que no queda un defecto confirmado en las fuentes revisadas para ese hallazgo previo; no es aprobación de las historias.

### F-01 — Modelo de campos de vehículo y reserva

- **Referencia anterior:** F-01, `requirements-report-v01.md` §5.
- **Estado:** **RESOLVED**.
- **Decisión humana:** ACCEPTED; se acordó un modelo sintético común de vehículo y reserva.
- **Evidencia actual:** `specs/product/goals.md`, “Modelo mínimo de datos sintéticos”, enumera para vehículo id, marca, modelo, categoría, plazas, maletero/carga, transmisión y estado operativo; para reserva, referencia, vehiculoId, fechas, nombre/apellidos, correo y estado. US-005 AC-02 lista las características de vehículo; US-008 AC-01–04 concreta datos de cliente obligatorios y su validación de presencia; US-018 AC-02–04 lista los atributos introducidos, exige ID único y trata campos ausentes/duplicado; US-019 AC-02 y Verification delimita campos modificables y excluye ID/estado; US-021 AC-03–04 enumera lo mostrado.
- **Observación:** La causa original —ausencia de una definición compartida de campos— queda atendida y las historias relevantes la enlazan o reproducen. Los detalles aún no fijados de validación se consideran preguntas localizadas, no reabren la ausencia del esquema que motivó F-01.
- **Impacto/acción:** No requiere acción para cerrar F-01. Véase F-07 para una pregunta más acotada sobre el origen del ID al dar de alta.
- **Confianza:** HIGH; evidencia directa en el modelo y los criterios actuales.
- **Bloqueador actual:** No.

### F-02 — Control de conflictos al confirmar concurrentemente

- **Referencia anterior:** F-02, `requirements-report-v01.md` §5.
- **Estado:** **PARTIALLY_RESOLVED**.
- **Decisión humana:** ACCEPTED; revalidación definitiva al confirmar, una operación funcional indivisible, rechazo de la segunda petición concurrente, aviso mediante US-013 y retorno a selección de fechas conservando filtros.
- **Fuentes actuales y extractos:** EP-003 US-009 AC-04–07: revalidar en confirmación definitiva, impedir reservas incompatibles, registrar solo si la revalidación es correcta y delegar el conflicto en US-013; Verification exige que comprobación y registro eviten dos confirmaciones incompatibles. EP-004 US-012 AC-03–05: de dos solicitudes simultáneas solo una queda registrada, la otra se rechaza y solo se permiten periodos no solapados; US-013 AC-01–04 define no confirmar, informar, volver a búsqueda y no alterar la reserva existente.
- **Observación:** La brecha esencial de resultado concurrente se ha concretado suficientemente a nivel funcional. Sin embargo, el acuerdo humano especifica conservar filtros al regresar a selección de fechas, mientras US-013 AC-03 solo dice “volver a la búsqueda para seleccionar otro vehículo”; ni ese criterio ni sus restricciones dicen que se conserven los filtros. También queda sin explicitar en el texto de la fuente la acción concreta “volver a selección de fechas”, aunque el acuerdo la menciona.
- **Impacto:** El rechazo y la ausencia de doble reserva son verificables; una implementación de recuperación puede perder contexto de búsqueda y seguir pareciendo conforme a los criterios actuales pese al acuerdo registrado.
- **Acción sugerida:** Confirmar si conservar filtros y regresar a la selección de fechas siguen siendo resultados obligatorios; si sí, incorporar evidencia verificable en la especificación por decisión humana.
- **Confianza:** HIGH en que el contrato concurrente está ahora escrito; HIGH en la omisión textual de retención de filtros.
- **Bloqueador:** Residual MAJOR para cerrar la interpretación de recuperación comprometida; no queda sin especificar el resultado de exclusión mutua que motivó el hallazgo original.

### F-03 — NFR y condiciones de verificación

- **Referencia anterior:** F-03, `requirements-report-v01.md` §5.
- **Estado:** **PARTIALLY_RESOLVED**.
- **Decisión humana:** ACCEPTED_WITH_CHANGES; vincular criterios con métricas del proyecto, establecer respuesta de interfaz <2 s local y pruebas funcionales deterministas con datos sintéticos, sin pruebas de carga/estrés industriales.
- **Evidencia actual:** `specs/product/goals.md`, “Criterios transversales de verificación”, recoge <2 s, pruebas deterministas, datos sintéticos y exclusión de pruebas industriales. Varias historias de consulta/confirmación reiteran las mismas condiciones; US-002/US-009, por ejemplo, citan métricas del proyecto. La constitución sigue requiriendo calidad verificable, accesibilidad y protección de información.
- **Observación:** La imprecisión inicial de rendimiento y tipo de prueba se redujo sustancialmente. No se encuentran condiciones verificables compartidas para expresiones como “sencillo y accesible” (EP-001 US-001 Verification) ni criterios de accesibilidad aplicables al flujo; no se infiere un estándar o umbral. La vinculación de las pruebas con M-01/M-02 plantea además el hallazgo separado F-06.
- **Impacto:** Quedan aspectos de experiencia/accesibilidad que podrían evaluarse con criterios diferentes. Este residual no invalida los criterios explícitos de tiempo o las exclusiones de pruebas industriales.
- **Acción sugerida:** Decidir qué criterios de accesibilidad/usabilidad son aplicables al MVP y cómo se observarán, sin introducir requisitos externos no acordados; corregir la trazabilidad de evidencia según F-06.
- **Confianza:** MEDIUM; el principio de la constitución es explícito, pero su aplicabilidad concreta necesita decisión.
- **Bloqueador:** No por sí solo. Se mantiene como refinamiento no bloqueante.

### F-04 — Límites de acceso para clientes y personal

- **Referencia anterior:** F-04, `requirements-report-v01.md` §5.
- **Estado:** **RESOLVED**.
- **Decisión humana:** ACCEPTED; cliente consulta/cancela su reserva individual mediante referencia; personal tiene vista administrativa diferenciada para reservas activas y catálogo, sin autenticación compleja/externa en el prototipo.
- **Evidencia actual:** EP-005 Boundary declara que la referencia actúa como mecanismo funcional para consultar/cancelar una reserva individual y distingue la vista administrativa; US-014/US-016 especifican uso de referencia. EP-005 US-017 y EP-006 US-018–US-021 indican funciones desde vista administrativa diferenciada; sus restricciones excluyen autenticación compleja/externa.
- **Observación:** Se precisó el límite de producto pedido. La simulación no equivale a una solución de identidad para producción y no se evalúa como tal. No se declara que exista implementación ni que cumpla el DoD.
- **Impacto/acción:** Sin acción para cerrar el hallazgo previo. Mantener los límites de datos ficticios y de alcance expresos.
- **Confianza:** HIGH; el acuerdo aparece en las fronteras y verificaciones actuales.
- **Bloqueador:** No.

### F-05 — Posible solapamiento entre US-002, US-006 y US-013

- **Referencia anterior:** F-05, `requirements-report-v01.md` §5.
- **Estado:** **RESOLVED**.
- **Decisión humana:** ACCEPTED_WITH_CHANGES; búsqueda masiva, consulta de un vehículo en detalle y gestión de un conflicto durante la reserva son responsabilidades separadas.
- **Evidencia actual:** EP-001 US-003 Verification dice que la consulta general corresponde a esa historia, la disponibilidad específica a US-006 y cambios durante la reserva a US-013. EP-002 US-006 Verification establece que revisa un vehículo concreto y no sustituye la revalidación final. EP-004 US-013 Verification limita su responsabilidad a informar y permitir la recuperación cuando la revalidación final detecta conflicto, y excluye expresamente búsqueda general y consulta ordinaria.
- **Observación:** Los límites funcionales que faltaban ahora aparecen en contexto y en los textos actuales. La relación temporal entre consulta y revalidación también se indica; no se propone fusionar ni dividir historias.
- **Impacto/acción:** No se identifica solapamiento ambiguo remanente de la magnitud del hallazgo. Mantener esas responsabilidades al revisar aceptación.
- **Confianza:** HIGH; límites explícitos en las tres especificaciones.
- **Bloqueador:** No.

### F-06 — Evidencia citada para M-01/M-02 no mide las métricas

- **Tipo:** NUEVO.
- **Categoría:** Trazabilidad, verificabilidad y medición de objetivos.
- **Severidad:** MAJOR.
- **Fuentes, IDs y extractos de ambas partes:**
  - `specs/product/goals.md`, M-01: “Al menos cuatro de cinco participantes completan el escenario de reserva en menos de diez minutos y sin ayuda”; M-02: “Al menos cuatro de cinco participantes comprenden correctamente qué vehículo han reservado y para qué fechas”.
  - EP-001 US-002 Verification: respuesta <2 s y “La verificación de este flujo servirá como evidencia para las métricas M-01 y M-02”.
  - EP-001 US-003 Verification: prueba funcional determinista de búsqueda sin resultados y “servirá como evidencia para M-01”.
  - EP-003 US-009 Verification: prueba funcional determinista de confirmación y <2 s; “servirá como evidencia para las métricas M-01 y M-02”.
- **Observación:** Medir tiempo de respuesta y ejecutar pruebas funcionales deterministas demuestra los resultados técnicos descritos en esos criterios, pero no demuestra por sí mismo la proporción de participantes que completa el escenario sin ayuda ni la comprensión de vehículo/fechas. La fuente no establece que además se vaya a realizar una evaluación con participantes ni cómo se recogerá evidencia para esos resultados. No se recomienda sustituir ni modificar las métricas.
- **Impacto:** Una revisión podría tomar evidencia de funcionamiento/performance como evidencia suficiente de métricas de experiencia que requieren observar participantes, dejando sin método verificable M-01/M-02.
- **Acción sugerida:** Aclarar qué evidencia medirá las métricas tal como están definidas y separar esa evidencia de las pruebas deterministas y del umbral de respuesta. El equipo decide el procedimiento; no se propone tamaño, protocolo ni umbral nuevo.
- **Confianza:** HIGH; la diferencia entre el contenido medido por las métricas y el contenido de las verificaciones aparece literalmente en goals y en las historias.
- **Bloqueador:** Sí, para interpretar qué demuestra la verificación vinculada a M-01/M-02 en US-002, US-003 y US-009; no impide comprender sus resultados funcionales.

### F-07 — Origen del identificador al registrar vehículo

- **Tipo:** NUEVO.
- **Categoría:** Claridad y regla de datos.
- **Severidad:** QUESTION.
- **Fuente:** EP-006 US-018 AC-02 dice que el personal introduce marca/modelo y demás atributos, pero no enumera el ID en esos campos; AC-03 exige que el vehículo “disponga de un identificador único”; AC-04 contempla ID duplicado.
- **Observación:** Se define que debe existir un identificador y que no debe duplicarse, pero no si lo introduce el personal, lo asigna el sistema o se origina de otro modo. No se considera defecto confirmado: cualquiera de esas alternativas podría ser la intención.
- **Impacto:** El flujo de alta y su prueba podrían interpretarse de formas distintas.
- **Acción sugerida:** Preguntar quién/qué asigna el ID y cómo se presenta el caso de duplicado; documentar la respuesta si afecta el flujo observable.
- **Confianza:** MEDIUM; la ausencia se limita al criterio y restricciones de US-018 revisados, pero la intención no está documentada.
- **Bloqueador:** No confirmado; no se eleva a bloqueo sin respuesta humana.

## 6. Matriz DoR

Se evaluaron los **14 criterios reales** del DoR en este orden:

1. ID único y estable; 2. épica; 3. objetivo de producto; 4. usuario/stakeholder; 5. capacidad descrita; 6. valor comprensible; 7. alcance/límites; 8. aceptación observable/verificable; 9. prioridad; 10. estimación; 11. incertidumbre; 12. dependencias/predecesores; 13. restricciones relevantes; 14. ausencia de dudas que impidan comprender/planificar.

**Leyenda:** `M` = MET; `N` = NOT_MET; `E` = NOT_ASSESSABLE; `A` = NOT_APPLICABLE. Cada cadena contiene exactamente 14 estados en el orden anterior. La evidencia general para cada `M` es: IDs y asociación se leen en el encabezado/ubicación de cada historia en su EP; las EP declaran Goals; las historias expresan actor/capacidad/valor y contienen Priority, Estimate, Uncertainty, Predecessors, Acceptance criteria y Verification/constraints. `—` en predecesores de US-001 es declaración explícita de que no hay predecesor, no ausencia del dato. La evidencia particular de toda excepción y el motivo por criterio se anota en la última columna. Los `M` evalúan solo el texto DoR, no implementación ni cumplimiento del DoD.

| Historia | Estados 1–14 | Evidencia para excepciones; evidencia de los demás estados por la regla común anterior |
|---|---|---|
| US-001 | `MMMMMMMMMMMMMM` | EP-001, US-001: actor, fechas, valor, prioridad 5 h-p, incertidumbre baja, predecesores —, criterios y restricciones explícitos. |
| US-002 | `MMMMMMMNMMMMMM` | EP-001, US-002 AC-05 y Verification dan resultado <2 s y prueba determinista; **criterio 8 N** respecto de su pretensión explícita de evidenciar M-01/M-02: esa prueba no mide participantes/comprensión (F-06). |
| US-003 | `MMMMMMMNMMMMMM` | EP-001, US-003 incluye prueba determinista de no resultados; **criterio 8 N** respecto de “evidencia para M-01”: no demuestra completar escenario sin ayuda/tiempo con participantes (F-06). |
| US-004 | `MMMMMMMMMMMMMM` | EP-002, US-004: filtro, retirada y estado sin resultados están descritos en AC-01–05; prioridad y estimación explícitas. |
| US-005 | `MMMMMMMMMMMMMM` | EP-002, US-005 AC-02 enumera campos del modelo de goals; AC-03/04 correspondencia y etiquetas; DoR previo F-01 resuelto. |
| US-006 | `MMMMMMMMMMMMMM` | EP-002, US-006 AC-01–04 distingue consulta de vehículo concreto y enlaza reservas/estado operativo. |
| US-007 | `MMMMMMMMMMMMMM` | EP-003, US-007 AC-01–03 y Verification definen selección de disponible y exclusión del no disponible. |
| US-008 | `MMMMMMMMMMMMMM` | EP-003, US-008 AC-01–04 nombra obligatorios, presencia, error y asociación a vehículo/fechas; goals define el modelo. |
| US-009 | `MMMMMMMNMMMMMM` | EP-003, US-009 AC-04–08 y Verification son verificables para confirmación/concurrencia; **criterio 8 N** respecto a usar la prueba citada como evidencia de M-01/M-02 (F-06). |
| US-010 | `MMMMMMMMMMMMMM` | EP-003, US-010 AC-01–04: referencia por reserva, unicidad, presentación y localización; formato ilustrativo señalado. |
| US-011 | `MMMMMMMMMMMMMM` | EP-004, US-011 AC-01–04 define bloqueo solo tras confirmación y por intervalo reservado. |
| US-012 | `MMMMMMMMMMMMMM` | EP-004, US-012 AC-01–05 y restricciones fijan rechazo, concurrencia y límites inclusivos de fechas. |
| US-013 | `MMMMMMMMMMMMMM` | EP-004, US-013 AC-01–04 define aviso, rechazo, recuperación y no alteración de la reserva en conflicto. La retención de filtros es una discrepancia del acuerdo (F-02), no convierte la historia en ininteligible. |
| US-014 | `MMMMMMMMMMMMMM` | EP-005 Boundary y US-014 AC-01–05 definen búsqueda por referencia y respuesta ante existente/inexistente; límite de acceso aclarado en la propia épica. |
| US-015 | `MMMMMMMMMMMMMM` | EP-005, US-015 AC-01–06 identifica vehículo/fechas/estado, pertenencia a reserva y etiquetas visibles. |
| US-016 | `MMMMMMMMMMMMMM` | EP-005, US-016 AC-01–05 define cancelación por referencia, estado activo/inactivo, efectos y error. |
| US-017 | `MMMMMMMMMMMMMM` | EP-005, US-017 AC-01–05 identifica al personal y la vista administrativa simulada, datos y estados presentados. |
| US-018 | `MMMMMMNMMMMMM` | EP-006, US-018 AC-02–04 enumera datos, ID único y error, pero no dice quién genera/proporciona el ID; **criterio 7 N** por límite del flujo de alta aún ambiguo (F-07, QUESTION). Los demás criterios, incluida aceptación general, están expresos. |
| US-019 | `MMMMMMMMMMMMMM` | EP-006, US-019 AC-02 y Verification enumera campos editables y excluye ID/estado; error preserva valores previos. |
| US-020 | `MMMMMMMMMMMMMM` | EP-006, US-020 AC-01–05 define cambio de estado y efecto; EP-006 explicita vista diferenciada del personal. |
| US-021 | `MMMMMMMMMMMMMM` | EP-006, US-021 AC-01–06 enumera los campos visibles y correspondencia con el almacenamiento; respuesta local <2 s. |

**Elementos diferidos, separados del DoR:** Todas las historias conservan `Initial plan: Pendiente de asignación en la planificación de la Semana 3`. Se registra como estado de planificación indicado en las fuentes, no como criterio DoR ni como decisión humana nueva. Las prioridades, estimaciones e incertidumbres están presentes en las historias y no se modificaron.

## 7. Candidatos de omisión y preguntas de alcance

| Etiqueta | Candidato/pregunta | Racional y fuente | Pregunta humana |
|---|---|---|---|
| IN_SCOPE_CANDIDATE | Resultado/requisito para instalación, ejecución y evaluación estable por un tercero | `specs/product/goals.md`, G-03/M-03; no localizado en los seis archivos de épica revisados | ¿Dónde se especifica y verifica M-03: en otra fuente del producto o en este catálogo? |
| SCOPE_UNCLEAR | Evidencia de usabilidad para M-01/M-02 distinta de pruebas funcionales | `goals.md` M-01/M-02 y EP-001 US-002/US-003, EP-003 US-009 (F-06) | ¿Qué tipo de evidencia del objetivo se espera y dónde se documenta, sin sustituir las métricas acordadas? |
| SCOPE_UNCLEAR | Origen/asignación del ID al dar de alta un vehículo | EP-006 US-018 AC-02–04 (F-07) | ¿Lo proporciona el personal o se asigna en el flujo del sistema? |
| SCOPE_UNCLEAR | Criterios verificables aplicables de accesibilidad/usabilidad | Constitución, principio 5; EP-001 US-001 Verification (“sencillo y accesible”) (F-03) | ¿Qué aspectos son exigibles en este MVP y qué evidencia se aceptará? |
| OUT_OF_SCOPE | Pago/facturación real, integración con aseguradoras, apertura IoT/GPS y mantenimiento físico | `specs/product/goals.md` EX-01–EX-03; límites EP-003/EP-004/EP-006 | No se recomienda incorporarlos sin cambio de alcance aprobado; ¿se mantienen estas exclusiones? |

**Stakeholders:** goals declara clientes, personal de AutoRent, dirección de AutoRent y MoveTech Solutions. Las historias cubren especialmente cliente, sistema y personal; no se encontró en los seis archivos EP un resultado específicamente dirigido a Dirección. La pregunta sigue siendo de cobertura, no un defecto confirmado: ¿el interés de Dirección queda satisfecho por los resultados de reserva/catálogo o necesita un resultado de demostración distinto?

No se repite aquí F-02/F-06 como omisión independiente.

## 8. Dependencias, supuestos y brechas de trazabilidad

- **Contrato funcional de disponibilidad:** US-002 y US-006 consultan disponibilidad; US-009/US-012 revalidan y excluyen confirmaciones incompatibles; US-011 refleja bloqueo y US-013 comunica el conflicto. US-016 (cancelación) y US-020 (estado manual) afectan a la disponibilidad mostrada. El solapamiento inclusivo y el intervalo por días están precisados en US-012. El camino de recuperación no acredita retención de filtros, según F-02.
- **Predecesores explícitos:** Se mantienen los enlaces declarados en las historias (incluidos US-009 con US-012, US-011 con US-009/US-012 y las cadenas US-014–US-016 y US-018–US-021). No se detectó ciclo entre los predecesores expresos. La lectura es textual; no se verificó planificación.
- **Clasificación:** Los enlaces `Predecessors` se tratan como prerrequisitos declarados por el equipo. El contrato de disponibilidad entre consulta, confirmación, reserva activa, cancelación y estado manual es compartido. `Initial plan` pendiente es una cuestión de secuenciación/planificación, no una dependencia funcional.
- **Datos:** El modelo común resuelve la brecha general de F-01. La regla de quién asigna el ID de nuevo vehículo queda sin determinar en US-018 (F-07).
- **Supuestos explícitos:** catálogo ficticio disponible; un solo cliente por vehículo para un rango; agencia AutoRent; disponibilidad sin servicios externos; acceso a Internet/navegador actualizado. No se halló contradicción directa en las fuentes revisadas.
- **Trazabilidad a objetivos:** las seis épicas declaran objetivos; M-01/M-02 están vinculados a pruebas concretas en US-002/US-003/US-009, pero la prueba citada no mide el resultado de esas métricas (F-06). G-03/M-03 permanece como candidato de especificación detallada.
- **Dependencias externas:** `goals.md` asume que no se requiere conexión externa para disponibilidad; EP-004 y EP-006 excluyen sistemas externos. No se presume otra integración.
- **DoD:** Se leyó el DoD compartido; no hay evidencia de implementación, pruebas ejecutadas, integración o revisión técnica, así que no se emite conclusión de cumplimiento.

## 9. Preguntas para el equipo humano

1. **Prioridad alta — F-06:** ¿Qué evidencia verificará M-01 y M-02 conforme a sus definiciones de participantes, ayuda, tiempo y comprensión? ¿Dónde se documentará, separada de pruebas deterministas y de respuesta <2 s?
2. **Prioridad alta — F-02:** ¿Se mantiene el acuerdo de conservar filtros y volver a selección de fechas tras el conflicto? Si sí, ¿qué resultado observable se espera y cómo se refleja en los criterios actuales?
3. **Prioridad media — F-03:** ¿Qué expectativas comprobables de accesibilidad/usabilidad se aplican al MVP, especialmente ante “sencillo y accesible”, sin inferir estándares o umbrales?
4. **Prioridad media — F-07:** ¿Quién asigna/proporciona el ID al dar de alta un vehículo y qué interacción se espera si es duplicado?
5. **Prioridad media — cobertura:** ¿En qué fuente se especifica el resultado M-03 de instalación/ejecución por tercero?
6. **Prioridad media — stakeholders:** ¿Dirección requiere una salida funcional de las épicas revisadas o basta el resultado general de catálogo y reservas?

## 10. RECHECK crosswalk

| Hallazgo previo | Decisión humana registrada | Evidencia actual | Estado exacto |
|---|---|---|---|
| F-01 | ACCEPTED; modelo mínimo de datos uniforme | Modelo en goals y uso explícito en historias de consulta, reserva y catálogo | **RESOLVED** |
| F-02 | ACCEPTED; revalidación final, exclusión mutua, rechazo/aviso y retorno conservando filtros | Concurrencia/rechazo/aviso están escritos; conservación de filtros y retorno a fechas no están expresos | **PARTIALLY_RESOLVED** |
| F-03 | ACCEPTED_WITH_CHANGES; <2 s, pruebas funcionales deterministas y no carga/estrés industrial, vincular con métricas existentes | NFR de respuesta y método reproducible aparecen; accesibilidad/usabilidad sigue genérica y evidencia M-01/M-02 es inadecuada (F-06) | **PARTIALLY_RESOLVED** |
| F-04 | ACCEPTED; consulta/cancelación por referencia y vista administrativa simulada, sin auth compleja/externa | Boundary, criterios y restricciones de EP-005/EP-006 incorporan los límites | **RESOLVED** |
| F-05 | ACCEPTED_WITH_CHANGES; delimitar consulta masiva, ficha y error concurrente | US-003, US-006 y US-013 asignan explícitamente las tres responsabilidades | **RESOLVED** |

No se asigna JUSTIFIABLY_REJECTED ni DEFERRED a ningún hallazgo previo: las fuentes contienen refinamientos para cada decisión, aunque F-02/F-03 solo materializan parte del acuerdo. No hay decisión humana incompatible con una regla de gobernanza identificada.

## 11. Cierre explícito

Este es un informe consultivo. No se modificó ningún requisito fuente, prioridad, estimación, plan ni decisión humana. No se aprobó ningún baseline ni gate.
