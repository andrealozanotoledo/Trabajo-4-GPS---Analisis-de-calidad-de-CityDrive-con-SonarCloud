# Revisión de ProjectLibre — Hito 4 de CityDrive

## Metadatos

- **Proyecto:** CityDrive — MoveTech Solutions / AutoRent
- **Modo:** `RECHECK`
- **Fecha:** 2026-10-15
- **Agente auditor:** `project-libre`
- **Informe anterior:** [`project-libre-review-report-v01.md`](project-libre-review-report-v01.md)
- **Fuentes auditadas:** los dos XML indicados, los dos POD, la baseline Excel, el README, la revisión humana de Semana 3 y el informe v01.
- **Limitaciones:** la comprobación se ha realizado sobre el contenido XML almacenado; no se ha abierto ProjectLibre durante esta auditoría. Los POD y el XLSX se han utilizado como referencia documental y no como sustituto de los XML. No se localizó un registro específico de riesgos de Semana 4.

## Veredicto

**APROBADO_CON_CONDICIONES**

La RECHECK confirma que las dos exportaciones XML contienen el mismo plan en agrupaciones distintas: 21 historias, 6 iteraciones, 6 épicas en la vista por épicas, 3 hitos, 5 recursos de equipo, asignaciones con trabajo y coste, y 75 enlaces de precedencia. El calendario XML también es coherente entre las dos vistas y ya no reproduce la diferencia de calendario observada en el informe v01 sobre los POD.

La planificación coincide con la referencia solicitada: 102 h-p de historias, 30 h-p de gestión, 132 h-p totales y 3.300 € a 25 €/h. Las cargas de sprint verificadas son 22, 21, 21, 19, 21 y 22 h; el grooming inicial de 6 h es una tarea global separada del desglose de sprint.

Quedan condiciones antes de cerrar la entrega: `MaxUnits=0.5` en los cinco recursos no expresa las capacidades efectivas aprobadas de 5/4/5/4/4 h-p por semana, y no hay campos XML observables de camino crítico ni holguras. Además, no se ha aportado el registro de riesgos de Semana 4. Estas condiciones no cambian los archivos de planificación.

## Manifiesto de fuentes

| Fuente | Versión o fecha | Función | Estado |
|---|---|---|---|
| [`CityDrive_Por_Sprints.xml`](../planning/CityDrive_Por_Sprints.xml) | `CreationDate`/`LastSaved`: 2026-10-21 | Vista final ordenada por sprints y fuente primaria de la RECHECK | `ASSESSED` |
| [`CityDrive_Por_Epicas.xml`](../planning/CityDrive_Por_Epicas.xml) | `CreationDate`/`LastSaved`: 2026-10-21 | Vista final ordenada por épicas y fuente primaria de comparación | `ASSESSED` |
| [`CityDrive_Por_Sprints.pod`](../planning/CityDrive_Por_Sprints.pod) | Fecha interna no usada como autoridad | Artefacto ProjectLibre por sprints | `PARTIAL` |
| [`CityDrive_Por_Epicas.pod`](../planning/CityDrive_Por_Epicas.pod) | Fecha interna no usada como autoridad | Artefacto ProjectLibre por épicas | `PARTIAL` |
| [`CityDrive_Semana3_FINAL.xlsx`](../planning/CityDrive_Semana3_FINAL.xlsx) | Baseline indicada por la invocación | Comparación de estimaciones y capacidad | `PARTIAL` — formato binario |
| [`README.md`](../planning/README.md) | Sin versión indicada | Contexto de planificación | `ASSESSED` |
| [`human-planning-review-v01.md`](human-planning-review-v01.md) | 2026-10-12 | Decisiones humanas y baseline aprobada | `ASSESSED` |
| [`project-libre-review-report-v01.md`](project-libre-review-report-v01.md) | 2026-10-15 | Resultados de la auditoría anterior | `ASSESSED` |

No se localizó un PDF/enunciado adicional de Semana 4 ni un registro específico de riesgos y decisiones de Semana 4.

## Traslado a ProjectLibre

La comprobación directa de los XML confirma:

- **21 historias:** identificadores `US-001` a `US-021` presentes una vez por vista, aunque el orden de la vista por sprints sigue la ejecución y el de la vista por épicas sigue `EP-001` a `EP-006`.
- **6 sprints:** `IT-001` a `IT-006`.
- **6 épicas:** `EP-001` a `EP-006` en la vista por épicas.
- **3 hitos:** `Hito R1 - Fin de Release 1`, `Hito R2 - Fin de Release 2` y `Hito R3 - Entrega Final CityDrive`.
- **Gestión:** `MGT-000 - Project grooming` y las actividades de grooming, planning, review y retrospective de cada iteración.
- **Recursos:** Julia, Andrea, Óscar, Borja y Álvaro; `Unassigned` aparece como recurso técnico reservado por ProjectLibre, sin asignaciones de trabajo observadas.
- **Estimaciones:** las tareas hoja de historias conservan el trabajo de la baseline; las tareas resumen de sprint/épica muestran `Work=0`, como es esperable al no duplicar el trabajo de sus hojas.

| Elemento | Resultado | Evidencia XML |
|---|---|---|
| Historias trasladadas | `PASS` | 21 tareas `US-*` en cada XML |
| Épicas en vista por épicas | `PASS` | 6 tareas resumen `EP-*` |
| Sprints | `PASS` | 6 tareas resumen `IT-*` |
| Hitos | `PASS` | 3 tareas con `Milestone=1` |
| Tareas de gestión | `PASS` | `MGT-000` y cuatro eventos por sprint |
| Estimaciones de historias | `PASS` | Trabajo de tareas hoja; total contrastado: 102 h-p |
| Apertura o recálculo en ProjectLibre durante esta RECHECK | `NO_ASSESSABLE` | El XML prueba el artefacto guardado, no una acción realizada durante la auditoría |

## Comparación de las dos vistas

La equivalencia se verificó normalizando el identificador de tarea y comparando nombre, tipo, indicador de resumen, inicio, fin, duración, trabajo, hitos, recursos, asignaciones, costes y enlaces. Los UID y la jerarquía cambian por la reordenación, pero el trabajo representado no cambia.

| Dimensión | Resultado |
|---|---|
| Historias | `PASS` — 21 en cada vista |
| Épicas | `PASS` — la agrupación por épicas contiene EP-001..EP-006 |
| Sprints | `PASS` — la vista por sprints contiene IT-001..IT-006 |
| Recursos, trabajo y costes | `PASS` — mismos cinco recursos, tarifas y asignaciones normalizadas |
| Dependencias | `PASS` — 75 enlaces por vista, con equivalencia tras mapear UID a identificadores |
| Hitos y entrega final | `PASS` — R1, R2 y R3 coinciden |
| Calendario | `PASS` — ambos XML declaran `Calendario CityDrive`, lunes-viernes laborables, 08:00-12:00 y 13:00-17:00 |
| Camino crítico y holguras | `NO_ASSESSABLE` — no se exportan campos `Critical`, `TotalSlack` o equivalente |

La diferencia `GMT` frente a `Europe/Madrid` señalada en v01 pertenece a la evidencia POD anterior y no se observa en los XML nuevos. No se mantiene como hallazgo abierto de esta RECHECK.

## Capacidad y asignaciones

### Carga por sprint

El trabajo de historias por sprint es 18, 17, 17, 15, 17 y 18 h-p. Al añadir los cuatro eventos de gestión de 1 h de cada sprint se obtienen las cargas esperadas:

| Sprint | Historias | Gestión del sprint | Carga comprobada | Capacidad de referencia | Margen |
|---|---:|---:|---:|---:|---:|
| IT-001 | 18 | 4 | **22** | 22 | 0 |
| IT-002 | 17 | 4 | **21** | 22 | 1 |
| IT-003 | 17 | 4 | **21** | 22 | 1 |
| IT-004 | 15 | 4 | **19** | 22 | 3 |
| IT-005 | 17 | 4 | **21** | 22 | 1 |
| IT-006 | 18 | 4 | **22** | 22 | 0 |
| **Subtotal sprints** | **102** | **24** | **126** | **132** | **6** |
| Project grooming global | — | **6** | **6** | — | — |
| **Total** | **102** | **30** | **132** | **132** | **0** |

### Recursos

Los XML contienen asignaciones explícitas con `TaskUID`, `ResourceUID`, `Work`, `Units` y `Cost`. Cada historia y cada actividad de gestión tiene al menos una asignación; no se observan recursos desconocidos ni asignaciones a `Unassigned`.

| Recurso | Capacidad aprobada | `MaxUnits` XML | Tarifa XML | Resultado |
|---|---:|---:|---:|---|
| Julia | 5 h-p/semana | 0,5 | 25 €/h | `MAJOR` — configuración no expresada como capacidad efectiva |
| Andrea | 4 h-p/semana | 0,5 | 25 €/h | `MAJOR` — configuración no expresada como capacidad efectiva |
| Óscar | 5 h-p/semana | 0,5 | 25 €/h | `MAJOR` — configuración no expresada como capacidad efectiva |
| Borja | 4 h-p/semana | 0,5 | 25 €/h | `MAJOR` — configuración no expresada como capacidad efectiva |
| Álvaro | 4 h-p/semana | 0,5 | 25 €/h | `MAJOR` — configuración no expresada como capacidad efectiva |

La ausencia de un campo agregado de carga individual o de `Overallocated` en los XML impide certificar desde esta exportación la carga máxima por persona y la ausencia de sobreasignaciones. La revisión humana de la baseline sí informó de ausencia de sobreasignaciones, pero no sustituye la configuración técnica de ProjectLibre.

## Costes

La tarifa observada en cada recurso es `StandardRate=25.0` €/h y no hay coste por uso ni tarifa de horas extra. La suma de trabajo y costes de las asignaciones es coherente con:

| Concepto | Trabajo | Tarifa | Coste |
|---|---:|---:|---:|
| Historias de usuario | 102 h-p | 25 €/h | **2.550 €** |
| Gestión | 30 h-p | 25 €/h | **750 €** |
| **Total ProjectLibre** | **132 h-p** | **25 €/h** | **3.300 €** |
| Reserva libre adicional | **0 h-p** | 25 €/h | **0 €** |

La tarifa es un supuesto académico provisional, tal como indica la revisión humana; no es una tarifa contractual. Las 30 h-p de gestión están asignadas y no se consideran reserva de contingencia.

## Dependencias, camino crítico y holguras

- Cada XML contiene **75 `PredecessorLink`**, y el recuento coincide entre vistas.
- Los enlaces cubren la secuencia interna de historias, las actividades de gestión, los cambios de sprint y los hitos de release/entrega.
- La comparación por identificadores conserva los mismos enlaces relevantes entre ambas vistas.
- No se observa un ciclo al revisar la dirección temporal de los enlaces exportados.
- Las tareas hoja y los hitos permanecen dentro del calendario laboral declarado.
- No se exportan campos de camino crítico, holgura total o holgura libre; por tanto, esas comprobaciones son `NO_ASSESSABLE` y no se infieren a partir de la carga.

## Riesgos de la planificación

No se encontró el registro formal de riesgos de Semana 4. La tabla identifica el seguimiento que debe cerrar el equipo; no atribuye una aceptación o tratamiento no documentado.

| ID | Situación | Evento | Consecuencia | Tratamiento | Contingencia |
|---|---|---|---|---|---|
| R-H4-01 | `MaxUnits=0.5` no representa 5/4/5/4/4 h-p por semana | Capacidad técnica distinta de la capacidad aprobada | Sobreasignación o lectura incorrecta de viabilidad | Documentar la conversión o ajustar la configuración con decisión humana | Revisar asignaciones y secuencia antes de ejecutar |
| R-H4-02 | IT-001 e IT-006 consumen 22 h-p | Cualquier retrabajo o cambio de disponibilidad | No existe margen en esos sprints | Controlar cambios y revisar capacidad | Reordenar solo con aprobación del equipo |
| R-H4-03 | Hay 75 precedencias, incluidas dependencias dentro de sprint | Una sucesora se ejecuta antes de su predecesora | Retraso o incumplimiento de la secuencia | Revisar enlaces al cambiar asignaciones | Bloquear la sucesora hasta validar la predecesora |
| R-H4-04 | La tarifa es académica | Se comunica como coste contractual | Coste económico mal interpretado | Mantener la etiqueta provisional | Sustituir tarifa y recalcular |
| R-H4-05 | Las 132 h-p están asignadas | Se cuentan las 30 h-p de gestión como reserva | Margen real sobreestimado | Mantener reserva libre en 0 h-p | Elevar decisión de capacidad al equipo |
| R-H4-06 | No hay campos exportados de holgura/camino crítico | Se toma la carga agregada como evidencia temporal | Riesgo de retraso no cuantificado | Aportar exportación o captura verificable | Revisar el plan en ProjectLibre |

## Hallazgos

| ID | Dimensión | Severidad | Estado | Evidencia | Impacto | Recomendación |
|---|---|---|---|---|---|---|
| AUD-001 | Capacidad técnica de recursos | `MAJOR` | `OPEN` | Los dos XML declaran `MaxUnits=0.5` para Julia, Andrea, Óscar, Borja y Álvaro; la referencia aprobada es 5/4/5/4/4 h-p por semana | ProjectLibre no representa directamente la disponibilidad efectiva y la comprobación de sobreasignación individual no queda cerrada | Documentar la equivalencia de unidades con la capacidad aprobada o corregirla mediante decisión humana; después exportar la carga |
| AUD-002 | Camino crítico y holguras | `MAJOR` | `NOT_ASSESSABLE` | No aparecen campos XML de camino crítico, holgura total o holgura libre | No se puede cuantificar el margen temporal ni confirmar el camino crítico | Aportar exportación/captura de esos campos o registrar formalmente que quedan fuera de la evidencia |
| AUD-003 | Riesgos de Semana 4 | `MAJOR` | `OPEN` | No se localizó registro con situación, evento, consecuencia, tratamiento, contingencia y seguimiento | El cierre del Hito 4 no demuestra la aceptación y seguimiento de los riesgos de planificación | Incorporar el registro y la decisión humana sobre cada riesgo |
| AUD-004 | Trazabilidad de carga individual | `MINOR` | `NOT_ASSESSABLE` | Los XML contienen asignaciones detalladas, pero no un resumen por persona ni indicador `Overallocated` | La carga por sprint se confirma, pero la lectura independiente por persona requiere sumar asignaciones o una vista adicional | Conservar una exportación de uso de recursos por sprint y persona |

Los hallazgos v01 sobre la ausencia de XML y la diferencia de calendarios quedan superados por la evidencia nueva y no se marcan como resueltos sin más: se consideran cerrados por cambio de evidencia, no por una corrección auditada del informe anterior.

## Próximos pasos

1. **AUD-001 — MAJOR:** documentar y validar la correspondencia entre `MaxUnits` y la capacidad efectiva individual.
2. **AUD-002 — MAJOR:** aportar evidencia de camino crítico y holguras, o dejar constancia de su `NO_ASSESSABLE` aceptación.
3. **AUD-003 — MAJOR:** incorporar el registro formal de riesgos de Semana 4 con responsable y seguimiento.
4. **AUD-004 — MINOR:** adjuntar una vista/exportación de carga por persona y sprint.
5. Mantener la referencia económica como académica/provisional y la reserva libre adicional en **0 h-p**.
