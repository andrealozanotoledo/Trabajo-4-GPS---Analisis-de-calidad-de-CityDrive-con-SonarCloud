# Requirements review v01

## 1. Metadatos de ejecución

- **Baseline/snapshot:** Las seis especificaciones indican `Catálogo V0 - Semana 2`. No se proporcionó un identificador de snapshot adicional.
- **Commit:** No proporcionado.
- **Fecha/hora:** 2026-10-11 14:41 (zona horaria indicada por la invocación: UTC+02:00).
- **Agente:** `.github/agents/requirements-reviewer.agent.md`; el archivo no declara versión.
- **Modelo/herramienta:** No declarados por la invocación. Se utilizaron las herramientas disponibles de lectura y creación del informe; no se ejecutaron comandos ni pruebas.
- **Modo:** INITIAL.
- **Alcance:** Catálogo completo solicitado: EP-001 a EP-006, historias US-001 a US-021; contexto de misión, objetivos/alcance, constitución, DoR y DoD proporcionados.
- **Idioma:** Español.

## 2. Manifiesto de fuentes y limitaciones

### Fuentes leídas

| Ruta | Papel y secciones revisadas | Baseline/versión declarada |
|---|---|---|
| `.github/agents/requirements-reviewer.agent.md` | Protocolo, criterios y formato de revisión | No indicada |
| `.specify/memory/constitution.md` | Principios, documentación, calidad y gobernanza | No indicada |
| `specs/product/mission.md` | Misión, problema, usuarios, valor y experiencia deseada | No indicada |
| `specs/product/goals.md` | Objetivos, métricas, stakeholders, alcance, exclusiones, supuestos, restricciones y trazabilidad | No indicada |
| `docs/quality/definition-of-ready.md` | Los 14 criterios del DoR compartido | No indicada |
| `docs/quality/definition-of-done.md` | Condiciones compartidas de terminado | No indicada |
| `specs/EP-001 - Búsqueda de vehículos/spec.md` | Límite, resultado y US-001–US-003 | Catálogo V0 - Semana 2 |
| `specs/EP-002 - Filtrado y consulta de vehículos/spec.md` | Límite, resultado y US-004–US-006 | Catálogo V0 - Semana 2 |
| `specs/EP-003 - Creación de reservas/spec.md` | Límite, resultado y US-007–US-010 | Catálogo V0 - Semana 2 |
| `specs/EP-004 - Control de disponibilidad y conflictos/spec.md` | Límite, resultado y US-011–US-013 | Catálogo V0 - Semana 2 |
| `specs/EP-005 - Consulta y gestión de reservas/spec.md` | Límite, resultado y US-014–US-017 | Catálogo V0 - Semana 2 |
| `specs/EP-006 - Gestión del catálogo de vehículos/spec.md` | Límite, resultado y US-018–US-021 | Catálogo V0 - Semana 2 |

También se inspeccionó `docs/reviews/` para versionado; no se observó allí un informe previo con el patrón `requirements-report-vNN.md`.

### Límites

- La evaluación cubre solo las fuentes y los seis archivos expresamente indicados. No se leyeron planes, tareas, código, pruebas, decisiones ni otros artefactos.
- Los campos del catálogo y de la reserva a los que las historias aluden como “definidos” no aparecen especificados en las fuentes revisadas; la conclusión se limita a esas fuentes.
- No se aportaron decisiones humanas, estimaciones alternativas ni historial de cambios.
- El DoD describe condiciones de implementación. Sin evidencia de implementación no se evalúa ni se afirma que se cumpla.
- No se aplica precedencia entre fuentes porque no se identificó contradicción normativa que requiera resolverla. La constitución declara prioridad sobre los demás documentos.

## 3. Evaluación del alcance revisado

**Recomendación: NEEDS_REFINEMENT.**

**Alcance exacto:** EP-001–EP-006 y US-001–US-021, contrastados con misión, objetivos/alcance, constitución, DoR y DoD.

**Historias afectadas por bloqueadores de refinamiento:** US-005, US-008, US-018, US-019 y US-021 por falta de definición verificable de los campos/datos que componen el vehículo o la reserva (F-01); US-009, US-011, US-012 y US-013 por la garantía no especificada ante confirmaciones concurrentes y la distribución repetida de responsabilidades de control (F-02). US-002 y US-006 también comparten el contrato de disponibilidad señalado en F-02.

**Por qué bloquean:** Sin el conjunto de campos al que remiten varias historias no se puede acordar qué datos se capturan, mantienen y muestran, ni verificar el resultado. Asimismo, comprobar disponibilidad antes de registrar no define el resultado cuando dos solicitudes compiten por el mismo vehículo/intervalo; la prevención de solapamientos es un resultado esencial expresado por EP-004 y el alcance de reserva por días. Son brechas de especificación, no un juicio sobre implementación.

La recomendación no es aprobación ni declaración de incompletitud global. Las restantes preguntas, limitaciones y candidatos se detallan abajo.

## 4. Matriz de cobertura

| Dimensión | IDs/artefactos inspeccionados | Resultado | Hallazgos |
|---|---|---|---|
| Claridad y consistencia | EP-001–EP-006; US-001–US-021; misión, objetivos y calidad | Requiere precisión en datos de vehículo/reserva y en el contrato de control de disponibilidad; criterios de aceptación generalmente presentes, con algunos términos no medibles | F-01, F-02, F-03 |
| Cobertura y alineación de alcance | G-01–G-03, M-01–M-04, S-01–S-03, EX-01–EX-03; EP-001–EP-006 | El recorrido esencial de búsqueda/reserva y las funciones de catálogo/consulta están representados. La meta M-03 sobre instalación/ejecución revisable no tiene requisito detallado localizado en este catálogo | Candidato §7; sin hallazgo confirmado |
| Elementos ausentes de especificación | US-001–US-021; DoR/DoD y constitución | Faltan definiciones referenciadas de campos; hay NFR y límites de verificación que requieren concretarse; preguntar por accesos y estados | F-01, F-02, F-03 |
| Tamaño y granularidad (heurística INVEST) | US-001–US-021 | En general son resultados verticales distinguibles. Repetición del control de disponibilidad y algunos criterios combinados hacen menos clara la frontera entre historias; no se ordena una división | F-02, F-05 |
| Criterios de aceptación y DoR | US-001–US-021; los 14 criterios de `definition-of-ready.md` | Las historias tienen prioridad, estimación, incertidumbre y predecesores declarados. Hay DoR NOT_MET en historias afectadas por F-01/F-02; ver matriz §6 | F-01, F-02, F-03 |
| Dependencias y supuestos | Predecesores de US-001–US-021; supuestos/restricciones de `goals.md` | Predecesores explicitados y sin ciclo visible. Hace falta distinguir prerrequisito de contrato compartido de disponibilidad; las dependencias externas no se presuponen | F-02, F-03 |

## 5. Hallazgos

### Índice

| ID | Severidad | Categoría | Referencias | Estado de bloqueo |
|---|---|---|---|---|
| F-01 | MAJOR | Datos/reglas, verificabilidad y DoR | EP-002 US-005; EP-003 US-008; EP-006 US-018, US-019, US-021 | Bloqueador de refinamiento para las historias afectadas |
| F-02 | MAJOR | Disponibilidad, consistencia y dependencias | EP-001 US-002; EP-002 US-006; EP-003 US-009; EP-004 US-011–US-013 | Bloqueador de refinamiento para el resultado esencial de reserva sin conflictos |
| F-03 | MINOR | NFR y verificabilidad | EP-001 US-002, US-003; EP-002 US-004–US-006; EP-003 US-008–US-009; EP-005 US-014–US-016; EP-006 US-018–US-021 | No bloqueador por sí solo |
| F-04 | QUESTION | Privacidad, stakeholder y reglas de acceso | EP-005 US-014–US-017; EP-006 US-018–US-021 | No confirmado; requiere decisión/clarificación |
| F-05 | MINOR | Redundancia y propiedad de criterios | EP-001 US-002; EP-002 US-006; EP-003 US-009; EP-004 US-012–US-013 | No bloqueador adicional a F-02 |

### F-01 — Campos de vehículo y reserva referenciados pero no definidos

- **Categoría:** Datos/reglas de negocio, verificabilidad y criterios DoR.
- **Fuentes e IDs:** `specs/EP-002 - Filtrado y consulta de vehículos/spec.md`, US-005 AC-02: “la información básica definida en el catálogo”; `specs/EP-003 - Creación de reservas/spec.md`, US-008 AC-01: “campos definidos como obligatorios para la reserva”; `specs/EP-006 - Gestión del catálogo de vehículos/spec.md`, US-018 AC-01 “datos básicos definidos para un vehículo”, US-019 AC-02 “campos permitidos” y US-021 AC-02 “información básica definida para el catálogo”. Contraste: `specs/product/goals.md`, S-02, menciona catálogo y reservas ficticios, sin enumerar campos.
- **Observación:** En las fuentes revisadas no se encontró el esquema/diccionario que concrete esos campos, cuáles son obligatorios/editables, sus validaciones ni qué información básica se muestra. Los criterios dependen de una definición externa al texto inspeccionado.
- **Impacto:** Cliente y personal no pueden compartir una interpretación comprobable de los datos que introducen, editan o consultan; también impide comprobar adecuadamente los criterios afectados del DoR (capacidad, límites y dudas pendientes).
- **Acción sugerida:** Acordar y enlazar el conjunto mínimo de datos sintéticos de vehículo y reserva, campos obligatorios/editables/visibles y validaciones y errores correspondientes. No se propone ningún campo concreto.
- **Confianza:** HIGH; las historias remiten expresamente a definiciones no contenidas en las seis especificaciones leídas.
- **Bloqueador:** Sí, para US-005, US-008, US-018, US-019 y US-021, no para el catálogo completo fuera de esas historias.

### F-02 — Contrato insuficiente para impedir conflictos de disponibilidad

- **Categoría:** Regla de negocio, comportamiento concurrente y dependencias.
- **Fuentes e IDs:** `specs/EP-004 - Control de disponibilidad y conflictos/spec.md`, US-012 AC-01: “comprueba las reservas existentes antes de registrar una nueva”; US-012 Verification and constraints: “la validación debe mantener la integridad”; US-009 AC-04–AC-06 en `specs/EP-003 - Creación de reservas/spec.md`; US-013 AC-01–AC-03 en EP-004. En sentido de lectura, EP-001 US-002 y EP-002 US-006 definen qué disponibilidad se presenta.
- **Observación:** Se exige comprobar antes de confirmar y rechazar solapamientos, pero no se especifica el resultado observable si dos confirmaciones concurrentes leen el mismo estado disponible. “Integridad” y “inmediatamente antes” no fijan por sí solos cómo debe quedar la reserva. Las historias reparten entre sí consulta, revalidación, registro y bloqueo, sin un contrato único explícito. US-012 sí resuelve la frontera de fechas: ambas incluidas y una reserva que termina el 12 permite iniciar la siguiente el 13; no se cuestiona esa regla.
- **Impacto:** Una interpretación puede aceptar dos reservas incompatibles en una carrera, en tensión con el resultado de EP-004 y el supuesto de una reserva por vehículo y rango. También dificulta pruebas de aceptación compartidas.
- **Acción sugerida:** Definir el resultado de negocio observable para confirmaciones simultáneas y dejar claro qué historia/criterio cubre revalidación, rechazo, registro y disponibilidad posterior. Definirlo sin prescribir tecnología.
- **Confianza:** HIGH en la brecha de especificación (no hay escenario concurrente explícito); MEDIUM en su probabilidad dentro de la demostración, que no se detalla.
- **Bloqueador:** Sí, para US-009, US-011, US-012 y US-013 y el contrato consultado por US-002/US-006; no se atribuye defecto de implementación.

### F-03 — NFR y condiciones de verificación expresadas de forma genérica

- **Categoría:** NFR, accesibilidad y verificabilidad.
- **Fuentes e IDs:** Constitución, principios 3 y 5; `docs/quality/definition-of-done.md`, revisión de NFR aplicables y verificación de criterios; `specs/EP-001 - Búsqueda de vehículos/spec.md`, US-002: “tiempo de respuesta adecuado”; `specs/EP-002 - Filtrado y consulta de vehículos/spec.md`, US-004 y US-005: “fácil”, “clara y legible”; y varias historias de cliente/personal describen mensajes claros, sencillez y presentación comprensible sin asociar condiciones observables comunes.
- **Observación:** Son intenciones válidas, pero en el catálogo revisado no se encuentran condiciones de aceptación que permitan juzgar qué constituye “adecuado”, ni referencias consistentes a las expectativas transversales de accesibilidad, protección de información y validación de entradas establecidas por la constitución. No se inventa un umbral numérico ni un estándar.
- **Impacto:** Evaluadores podrían aplicar interpretaciones distintas a rendimiento/usabilidad/accesibilidad; queda débil la trazabilidad de los principios de calidad a las historias.
- **Acción sugerida:** Identificar qué NFR aplican al flujo de reserva y al de personal y acordar criterios comprobables, con evidencia de aceptación apropiada y sin añadir umbrales no decididos.
- **Confianza:** MEDIUM; la constitución expresa los principios, pero la aplicabilidad y las medidas se deben decidir con el equipo.
- **Bloqueador:** No como hallazgo independiente. Se debe refinar para una verificación coherente; no convierte cada mención genérica en bloqueo de historia.

### F-04 — Acceso a consulta/cancelación y protección de datos no aclarados

- **Categoría:** QUESTION — privacidad, acceso y stakeholders.
- **Fuentes e IDs:** `specs/EP-005 - Consulta y gestión de reservas/spec.md`, US-014 consulta por referencia y US-016 cancelación de reserva localizada; US-017 consulta de reservas activas por “personal de AutoRent”. `specs/EP-006 - Gestión del catálogo de vehículos/spec.md`, historias US-018–US-021 dirigidas al personal. Contraste: constitución, principio 4, exige proteger información; `specs/product/goals.md`, restricción de datos ficticios.
- **Observación:** No se especifica si conocer la referencia basta para consultar/cancelar ni cómo se distingue al personal de AutoRent. El uso de datos ficticios reduce el riesgo de exposición de datos reales, pero no determina la regla de acceso esperada. No se presume que un mecanismo concreto esté dentro del alcance.
- **Impacto:** La información de reservas o las operaciones de personal podrían interpretarse con niveles de acceso distintos; la política de privacidad/acceso no es evaluable con la evidencia disponible.
- **Acción sugerida:** Aclarar quién puede consultar, cancelar y mantener información y qué comprobación funcional se espera en el MVP; confirmar explícitamente si controles de acceso se incluyen o se excluyen y cómo se mantiene el límite de datos sintéticos.
- **Confianza:** MEDIUM; existe una obligación general de proteger la información, pero no hay evidencia suficiente para afirmar una infracción concreta.
- **Bloqueador:** No confirmado; clasificado como pregunta, no como defecto probado.

### F-05 — Repetición de la revalidación de disponibilidad sin frontera explícita

- **Categoría:** Consistencia, granularidad y propiedad de criterios.
- **Fuentes e IDs:** EP-003 US-009 AC-04/05: revalidar disponibilidad y no permitir solapamiento; EP-004 US-012 AC-01/02: comprobar reservas y no registrar si hay solapamiento; EP-004 US-013 AC-01/02: volver a comprobar antes de confirmar y no confirmar si dejó de estar disponible; EP-001 US-002 y EP-002 US-006 duplican parte del resultado visible de disponibilidad.
- **Observación:** Hay solapamiento textual entre criterios, pero no una contradicción directa: la consulta de disponibilidad y la comprobación final pueden ser momentos distintos del mismo flujo. La especificación no declara cuál historia es propietaria del criterio de aceptación transversal.
- **Impacto:** Riesgo de pruebas duplicadas o de que cada historia se considere satisfecha con un nivel diferente de revalidación; aumenta la ambigüedad expuesta en F-02.
- **Acción sugerida:** Aclarar la relación como prerrequisito, contrato compartido o criterio de la confirmación; mantener la trazabilidad entre historias en vez de dividirlas automáticamente. Revisar el acoplamiento con el contrato concurrente de F-02.
- **Confianza:** HIGH; los textos citados repiten el mismo comportamiento con formulaciones próximas.
- **Bloqueador:** No adicional a F-02.

## 6. Matriz DoR

Se evaluaron los **14 criterios reales** de `docs/quality/definition-of-ready.md`, en este orden:

1. Identificador único; 2. épica; 3. trazabilidad a objetivo; 4. usuario/stakeholder; 5. capacidad; 6. valor; 7. alcance/límites; 8. criterios observables/verificables; 9. prioridad; 10. estimación; 11. incertidumbre; 12. dependencias/predecesores; 13. restricciones relevantes; 14. ausencia de dudas que impidan comprender/planificar.

**Leyenda de cada vector:** `M` = MET; `N` = NOT_MET; `E` = NOT_ASSESSABLE; `A` = NOT_APPLICABLE. Las 14 posiciones siguen el orden anterior. Para cada fila, los criterios no marcados `N` se respaldan con el propio encabezado y texto de la historia: los archivos EP declaran su épica y objetivo(s), cada historia contiene actor/capacidad/valor, prioridad, estimación, incertidumbre, predecesores explícitos (incluido `—` en US-001), criterios y restricciones/verification; los IDs son estables en el catálogo leído. La trazabilidad a objetivo se establece por la épica indicada en los archivos. `M` no significa aprobación general ni cumplimiento del DoD.

| Historia | Evaluación 1–14 | Evidencia específica de NOT_MET / explicación |
|---|---|---|
| US-001 | `MMMMMMMMMMMMMM` | — |
| US-002 | `MMMMMMMMMMMMMM` | — |
| US-003 | `MMMMMMMMMMMMMM` | — |
| US-004 | `MMMMMMMMMMMMMM` | — |
| US-005 | `MMMMNMNNMMMMMN` | F-01: “información básica definida en el catálogo” no identifica los datos a consultar; impide cerrar alcance y criterios verificables. |
| US-006 | `MMMMMMMMMMMMMM` | — |
| US-007 | `MMMMMMMMMMMMMM` | — |
| US-008 | `MMMMNMNNMMMMMN` | F-01: “campos definidos como obligatorios” no determina los campos. Sin ellos no se concretan los límites ni la validación observable. |
| US-009 | `MMMMMMMMMMMMMN` | F-02: la confirmación no define el resultado observable cuando compite con otra confirmación sobre el mismo vehículo/intervalo. |
| US-010 | `MMMMMMMMMMMMMM` | — |
| US-011 | `MMMMMMMMMMMMMN` | F-02: el resultado de bloqueo depende del contrato de confirmaciones concurrentes, aún no descrito. |
| US-012 | `MMMMMMMMMMMMMN` | F-02: no define el resultado para dos confirmaciones concurrentes; la duda afecta a la interpretación/planning del resultado de integridad. |
| US-013 | `MMMMMMMMMMMMMN` | F-02: revalidación y rechazo no definen resultado para solicitudes concurrentes; F-05 recoge la frontera solapada. |
| US-014 | `MMMMMMMMMMMMMN` | F-04: no está resuelta la regla de acceso a una reserva consultada por referencia; aclaración sobre acceso necesaria para cerrar límites. |
| US-015 | `MMMMMMMMMMMMMN` | F-04: la historia depende de la regla de acceso de US-014; no se aclara quién puede ver esos datos. |
| US-016 | `MMMMMMMMMMMMMN` | F-04: no se define si la referencia por sí sola autoriza una cancelación ni quién puede solicitarla. |
| US-017 | `MMMMMMMMMMMMMN` | F-04: “personal de AutoRent” se identifica como stakeholder, pero no se especifica la condición observable que diferencia su acceso. |
| US-018 | `MMMMNMNNMMMMMN` | F-01: “datos básicos definidos” no enumera campos ni validaciones; F-04 pregunta por el límite de acceso del personal. |
| US-019 | `MMMMMMNNMMMMMN` | F-01: “campos permitidos” no se enumeran; no puede comprobarse el límite de edición. F-04 pregunta por acceso del personal. |
| US-020 | `MMMMMMMMMMMMMN` | F-04: función dirigida al personal sin regla verificable de quién puede cambiar el estado; aclarar si hay control de acceso. |
| US-021 | `MMMMMMNNMMMMMN` | F-01: “información básica definida para el catálogo” no identifica los atributos visibles. F-04 pregunta por acceso del personal. |

**Justificación del patrón:** Los estados `N` en posiciones 7–8 reflejan F-01: campos no enumerados impiden cerrar límites y criterios, sin negar que el actor, objetivo o valor general se expresen en la historia. Los `N` en posición 14 corresponden a datos no definidos (F-01), acceso aún no aclarado (F-04) o comportamiento concurrente (F-02). Los demás criterios quedan `M` sobre la evidencia textual descrita; no hay `NOT_ASSESSABLE` ni `NOT_APPLICABLE` en esta matriz. La severidad de las preguntas F-04 sigue siendo QUESTION y no se convierte en defecto confirmado por la matriz.

**Elementos diferidos, separados del estado DoR:** El `Initial plan` de las 21 historias dice “Pendiente de asignación en la planificación de la Semana 3”. Se registra como planificación diferida, no como una de las 14 condiciones evaluadas, ni se interpreta como decisión de calendario. No se revisaron estimaciones fuera de las declaradas en las historias.

## 7. Omisiones candidatas y preguntas de alcance

### Candidatos

| Etiqueta | Candidato/pregunta | Racional y fuente | Pregunta humana |
|---|---|---|---|
| IN_SCOPE_CANDIDATE | Requisito detallado para que un tercero instale, ejecute y evalúe el incremento | `specs/product/goals.md`, G-03 y M-03; las seis épicas consultadas no detallan ese resultado. La meta forma parte del producto, aunque podría residir en otros artefactos no aportados. | ¿El criterio de instalación/ejecución estable se cubrirá en una especificación de este catálogo o en otro artefacto? ¿Cuál será su referencia verificable? |

### Pregunta sobre stakeholder declarado

Los stakeholders declarados (clientes, personal, dirección de AutoRent y MoveTech Solutions) aparecen en los objetivos. Las historias detalladas se dirigen principalmente a cliente, sistema y personal. **No se encontró en las seis especificaciones revisadas** un resultado/criterio dirigido específicamente a Dirección; no se concluye que no exista en otros artefactos. ¿Dirección necesita una consulta o resultado de demostración distinto del ya cubierto por el catálogo/reservas, o no forma parte del alcance funcional de estas épicas?

### OUT_OF_SCOPE

No se recomienda añadir funciones de pagos/facturación reales, aseguradoras, IoT/GPS o mantenimiento físico: `specs/product/goals.md` EX-01–EX-03 y los límites de EP-003/EP-004/EP-006 las excluyen. Se registran como límites a preservar, no como omisiones.

## 8. Dependencias, supuestos y brechas de trazabilidad

- **Prerequisitos declarados:** US-001 → US-002 → US-003; US-002 precede a filtrado/selección; US-007 → US-008; US-009 depende de US-007, US-008 y US-012; US-010 sigue a US-009; US-011 depende de US-009/US-012; US-014 depende de US-010, US-015/US-016 de US-014 y US-017 de US-009; US-018 precede a US-019/US-020/US-021. Se conservaron los IDs tal como aparecen.
- **Ciclo:** No se encontró ciclo en los predecesores expresos de US-001–US-021.
- **Contrato compartido:** Disponibilidad consultada, estado manual del vehículo y reservas activas interactúan (US-002, US-006, US-011, US-012, US-016, US-020). La regla de US-012 especifica solapamiento inclusivo en días; falta un resultado de aceptación para confirmaciones simultáneas (F-02). Aclarar el contrato compartido sin confundirlo con un nuevo requisito de integración.
- **Secuenciación:** “Initial plan” de Semana 3 está pendiente para todas las historias. Se considera preferencia/planificación aún no asignada, no dependencia funcional.
- **Dependencias de datos:** US-005/US-008/US-018/US-019/US-021 dependen de definiciones de campos no contenidas en las fuentes leídas (F-01).
- **Dependencias externas:** `goals.md` asume que no hacen falta sistemas externos para disponibilidad; EP-004/EP-006 excluyen sistemas externos/IoT. No se añadió ninguna dependencia externa supuesta.
- **Supuestos explícitos relevantes:** datos ficticios; AutoRent; un cliente por vehículo en el mismo rango; acceso a Internet/navegador actualizado; disponibilidad interna. No se encontró contradicción directa con las seis épicas. El significado operativo de “rango” se precisa en US-012 con intervalos por días inclusivos; la regla para la fecha inicial pasada o límites del calendario no se especifica en las fuentes revisadas.
- **Trazabilidad:** las épicas declaran Goals y los elementos del catálogo tienen IDs estables; no se revisaron planes, tareas, código o pruebas para verificar el resto de la cadena declarada en `goals.md`.

## 9. Preguntas para el equipo humano

1. **Prioridad alta — F-01:** ¿Dónde se define la lista de campos para vehículos y reservas, incluyendo obligatoriedad, edición, presentación y validación? ¿Se debe enlazar ese artefacto en las historias?
2. **Prioridad alta — F-02:** ¿Qué resultado debe observarse si dos clientes intentan confirmar al mismo tiempo el mismo vehículo para periodos incompatibles? ¿Qué historias son responsables de revalidar, rechazar y comunicar el resultado?
3. **Prioridad alta — F-04:** ¿Basta la referencia para consultar/cancelar una reserva? ¿Cómo se delimita el acceso del personal a la consulta y mantenimiento? ¿Qué controles se incluyen o excluyen expresamente del MVP?
4. **Prioridad media — F-03:** ¿Qué criterios de rendimiento, accesibilidad, protección de información y validación se consideran aplicables y comprobables, sin introducir umbrales por inferencia?
5. **Prioridad media — cobertura:** ¿Dónde se especifica la meta G-03/M-03 (instalación, ejecución y evaluación por un tercero)?
6. **Prioridad media — reglas de fechas:** ¿Se permiten fechas de inicio anteriores al día actual y qué límites de calendario se esperan? ¿La igualdad inicio/fin representa una reserva válida de un día, como sugiere el intervalo inclusivo?
7. **Prioridad baja — stakeholders:** ¿Dirección de AutoRent requiere algún resultado funcional adicional en este alcance, o basta su interés recogido en los objetivos?

## 10. Revisión posterior

**INITIAL.** No se proporcionó informe anterior, registro de decisiones ni revisión previa; no aplica tabla de cruce RECHECK.

## 11. Cierre explícito

Este es un informe consultivo. No se modificó ningún requisito fuente, prioridad, estimación, plan ni decisión humana. No se aprobó ningún baseline ni gate.
