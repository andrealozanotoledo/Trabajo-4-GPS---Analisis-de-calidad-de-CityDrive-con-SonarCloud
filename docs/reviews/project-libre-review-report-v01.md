# Revisión de ProjectLibre — Hito 4 de CityDrive

## Metadatos

- **Proyecto:** CityDrive — MoveTech Solutions / AutoRent
- **Modo:** `FINAL`
- **Fecha:** 2026-10-15
- **Agente auditor:** `project-libre`
- **Fuentes auditadas:** las dos planificaciones `.pod`, la baseline Excel, el README, la revisión humana de Semana 3 y la revisión anterior disponible.
- **Limitaciones:** los `.pod` son serializaciones binarias de ProjectLibre. El lector disponible permite observar cadenas y metadatos, pero no reconstruir de forma fiable las tablas completas de tareas, asignaciones, costes, dependencias, unidades, holguras o camino crítico. El `.xlsx` tampoco es legible directamente con el lector disponible; sus métricas se contrastan mediante la revisión humana y el informe anterior. No se ha localizado un registro específico de riesgos o decisiones de Semana 4.

## Veredicto

**APROBADO_CON_CONDICIONES**

La evidencia permite confirmar que existen dos artefactos nativos de ProjectLibre, que corresponden a las vistas por sprints y por épicas, y que contienen tareas de gestión y asignaciones a integrantes. La baseline humana mantiene 21 historias y 102 h-p.

No obstante, la auditoría final no puede aprobar sin condiciones la planificación porque se observa una diferencia de calendario entre las dos vistas (`GMT` frente a `Europe/Madrid`) y no existe evidencia exportada suficiente para demostrar la equivalencia completa de tareas, asignaciones, costes, dependencias, ciclos, sobreasignaciones, camino crítico y holguras. Tampoco se ha encontrado un registro de riesgos propio de Semana 4.

Este veredicto se limita al Hito 4 de ProjectLibre y no constituye una nueva revisión de requisitos ni de la planificación inicial de Semana 3.

## Manifiesto de fuentes

| Fuente | Versión o fecha | Función | Estado |
|---|---|---|---|
| [`CityDrive_Por_Sprints.pod`](../planning/CityDrive_Por_Sprints.pod) | Artefacto disponible; fecha interna no observable | Vista final ordenada por sprints | `PARTIAL` — serialización binaria; se observan nombre, calendario, recursos, tareas MGT y enlaces, pero no se puede reconstruir todo el modelo |
| [`CityDrive_Por_Epicas.pod`](../planning/CityDrive_Por_Epicas.pod) | Artefacto disponible; fecha interna no observable | Vista final ordenada por épicas | `PARTIAL` — serialización binaria; se observan nombre, calendario, recursos, tareas MGT y enlaces, pero no se puede reconstruir todo el modelo |
| [`CityDrive_Semana3_FINAL.xlsx`](../planning/CityDrive_Semana3_FINAL.xlsx) | Baseline indicada por la invocación | Comparación de historias, esfuerzo, capacidad y coste de referencia | `PARTIAL` — formato binario no legible directamente |
| [`README.md`](../planning/README.md) | Sin versión indicada | Contexto de la carpeta de planificación | `ASSESSED` |
| [`human-planning-review-v01.md`](human-planning-review-v01.md) | 2026-10-12 | Decisiones humanas y baseline de Semana 3 | `ASSESSED` |
| [`audit-review-report-v01.md`](audit-review-report-v01.md) | 2026-10-14 | Auditoría previa | `ASSESSED_WITH_LIMITATION` — afirma que no había `.pod`; esa observación queda superada por los dos artefactos actualmente presentes |
| [`project-libre.agent.md`](../../.github/agents/project-libre.agent.md) | Versión disponible en la auditoría | Criterios y límites de la auditoría | `ASSESSED` |

No se localizaron PDF/enunciado de Semana 4 ni registro específico de riesgos y decisiones de Semana 4 en las rutas revisadas.

## Traslado a ProjectLibre

### Evidencia observable

- Los artefactos se identifican como:
  - `CityDrive - Planificación por Sprints (ajustada)`.
  - `CityDrive - Planificación por Épicas (ajustada)`.
- Ambos contienen objetos de proyecto, tareas normales, asignaciones, dependencias y calendarios de trabajo.
- Se observan los cinco recursos con sus nombres serializados: Julia, Andrea, Óscar, Borja y Álvaro.
- Se observan tareas de gestión asignadas, entre ellas `MGT IT-001 - Sprint grooming` y `MGT IT-001 - Sprint planning`, con asignaciones a integrantes.
- En la vista por sprints se observa al menos `US-001 - Introducir un rango de fechas`.

### Comprobaciones

| Elemento | Resultado | Evidencia o limitación |
|---|---|---|
| Seis iteraciones `IT-001` a `IT-006` | `NOT_ASSESSABLE` | La serialización muestra `IT-001`, pero no permite verificar de forma fiable el conjunto completo |
| Tres releases o hitos equivalentes | `NOT_ASSESSABLE` | No hay exportación legible de la jerarquía ni de los hitos |
| 21 historias de usuario | `PARTIAL` | La baseline humana confirma 21; no puede comprobarse el traslado completo dentro de cada `.pod` |
| Épicas `EP-001` a `EP-006` en la vista por épicas | `NOT_ASSESSABLE` | La vista está identificada como ordenada por épicas, pero no se puede reconstruir el listado completo |
| Identificadores `US-XXX`, `IT-XXX`, `EP-XXX`, `MGT-XXX` | `PARTIAL` | Se observan ejemplos `US-001`, `IT-001` y `MGT IT-001`; el conjunto completo no es verificable |
| Tareas de gestión | `PARTIAL` | Hay evidencia de grooming y planning de IT-001; no se puede confirmar el catálogo completo ni sus 30 h-p |
| Estimaciones de historias | `NOT_ASSESSABLE` | La baseline confirma 102 h-p, pero no se puede leer la suma de trabajo de los `.pod` |
| Hitos de release y entrega final | `NOT_ASSESSABLE` | No existe exportación legible de fechas e hitos |

La evidencia no permite declarar que ProjectLibre haya sido abierto o recalculado durante esta auditoría; solo se inspeccionaron los artefactos almacenados.

## Comparación de las dos vistas

La agrupación distinta por sprints y por épicas es esperada. Sin embargo, la equivalencia sustantiva no puede demostrarse con los artefactos binarios y se observa una diferencia que no es de agrupación:

- Vista por sprints: `Calendario CityDrive` y zona `GMT`.
- Vista por épicas: `Calendario CityDrive[Imported]` y zona `Europe/Madrid`.

La diferencia de calendario puede cambiar fechas, duración efectiva, límites de sprint, hitos, costes temporales y holguras. Debe tratarse como una inconsistencia abierta hasta que el equipo confirme cuál es el calendario aprobado y vuelva a exportar o documentar ambas vistas con la misma configuración.

| Dimensión de equivalencia | Resultado |
|---|---|
| Historias y estimaciones | `NOT_ASSESSABLE` |
| Recursos y horas asignadas | `NOT_ASSESSABLE` |
| Costes | `NOT_ASSESSABLE` |
| Dependencias relevantes | `NOT_ASSESSABLE` |
| Esfuerzo total | `NOT_ASSESSABLE` en ProjectLibre; `102 h-p` confirmado para la baseline humana |
| Hitos, releases y entrega final | `NOT_ASSESSABLE` |
| Calendario | **Diferencia observable** |

## Capacidad y asignaciones

### Referencia humana

La revisión humana de la baseline informa de 22 h-p por semana y de las siguientes capacidades efectivas:

| Integrante | Capacidad semanal | Capacidad en 6 iteraciones |
|---|---:|---:|
| Julia | 5 h-p | 30 h-p |
| Andrea | 4 h-p | 24 h-p |
| Óscar | 5 h-p | 30 h-p |
| Borja | 4 h-p | 24 h-p |
| Álvaro | 4 h-p | 24 h-p |
| **Equipo** | **22 h-p** | **132 h-p** |

### Carga por iteración

La carga de la baseline Excel comunicada en la revisión previa es la siguiente. No se afirma que sea la carga recalculada por los `.pod`:

| Iteración | Historias baseline | Capacidad de referencia | Carga ProjectLibre | Estado |
|---|---:|---:|---:|---|
| IT-001 | 21 h-p | 22 h-p | `NOT_ASSESSABLE` | La serialización sí muestra tareas MGT de IT-001 |
| IT-002 | 17 h-p | 22 h-p | `NOT_ASSESSABLE` | — |
| IT-003 | 17 h-p | 22 h-p | `NOT_ASSESSABLE` | — |
| IT-004 | 20 h-p | 22 h-p | `NOT_ASSESSABLE` | — |
| IT-005 | 17 h-p | 22 h-p | `NOT_ASSESSABLE` | — |
| IT-006 | 10 h-p | 22 h-p | `NOT_ASSESSABLE` | — |
| **Total** | **102 h-p** | **132 h-p** | **NOT_ASSESSABLE** | — |

La presencia de nombres de recursos y asignaciones en la serialización no permite comprobar `MaxUnits`, tarifas, duplicidades, recursos desconocidos, carga individual, ni sobreasignaciones. Por tanto, la viabilidad de capacidad en ProjectLibre queda `NOT_ASSESSABLE`, aunque la baseline Excel fue considerada viable por la revisión humana.

## Costes

La referencia aprobada para la comparación es:

| Concepto | Horas | Tarifa | Coste de referencia | Estado en ProjectLibre |
|---|---:|---:|---:|---|
| Historias de usuario | 102 h-p | 25 €/h | 2.550 € | `NOT_ASSESSABLE` |
| Gestión | 30 h-p | 25 €/h | 750 € | `NOT_ASSESSABLE` |
| **Total planificado** | **132 h-p** | **25 €/h** | **3.300 €** | `NOT_ASSESSABLE` |
| Reserva libre adicional | 0 h si las 132 h están asignadas | 25 €/h | 0 € | `NOT_ASSESSABLE` |

La fórmula de referencia es `Σ(horas asignadas × tarifa)`. Los 30 h-p de gestión no deben presentarse como reserva libre. La tarifa de 25 €/h es académica y provisional, no contractual.

No puede verificarse desde la serialización disponible si las asignaciones de ProjectLibre suman exactamente 102 h-p de historias, 30 h-p de gestión y 132 h-p totales, ni si la tarifa está configurada a 25 €/h en cada recurso.

## Dependencias, camino crítico y holguras

- Se observan objetos de enlace y dependencias en ambos artefactos.
- No puede reconstruirse la lista completa de precedencias entre historias, tareas de gestión, iteraciones y releases.
- No puede comprobarse la ausencia de ciclos.
- No puede comprobarse que el orden de las historias dentro de cada sprint sea coherente en las dos vistas.
- No existe evidencia exportada del camino crítico ni de holguras.
- No se infiere camino crítico, holgura ni reserva a partir de la carga agregada de la baseline.

Resultado: dependencias completas, ausencia de ciclos, camino crítico y holguras `NOT_ASSESSABLE`.

## Riesgos de la planificación

No se encontró un registro específico de riesgos de Semana 4. La tabla siguiente recoge los riesgos que deben quedar trazados para cerrar la auditoría; no se inventa su aceptación ni su tratamiento por parte del equipo.

| ID | Situación | Evento | Consecuencia | Tratamiento | Contingencia |
|---|---|---|---|---|---|
| R-H4-01 | No demostrada la misma configuración de calendario | Las vistas usan calendarios/zona horaria diferentes | Fechas, duración, hitos y holguras no equivalentes | Confirmar calendario aprobado y homogeneizar ambas vistas | Recalcular ambas vistas y revisar releases |
| R-H4-02 | Carga ProjectLibre no observable | Una asignación supera la capacidad individual o de sprint | Sobreasignación y retraso | Exportar carga por sprint e integrante y validar 22 h-p | Reordenar ejecución bajo decisión humana |
| R-H4-03 | Dependencias binarias no reconstruibles | Una precedencia dentro del sprint no se conserva | Historias ejecutadas fuera de orden | Exportar predecesoras/sucesoras y comprobar ciclos | Detener el trabajo sucesor hasta validar la predecesora |
| R-H4-04 | Diferencia potencial entre Excel y ProjectLibre | El traslado altera esfuerzo, horas o coste | Baseline y plan final no coinciden | Comparar una exportación tabular de ambas vistas | Mantener la baseline humana hasta corregir la diferencia |
| R-H4-05 | Tarifa académica provisional | Se interpreta 25 €/h como tarifa contractual | Coste económico mal comunicado | Etiquetar el coste como académico/provisional | Recalcular cuando exista tarifa oficial |
| R-H4-06 | No demostrada reserva libre tras incluir gestión | Las 30 h de gestión se cuentan como contingencia | Margen real sobreestimado | Separar historias, gestión y reserva adicional | Elevar una decisión de capacidad al equipo |
| R-H4-07 | Cambios de disponibilidad o concurrencia | Cambia la capacidad efectiva o aparece trabajo concurrente | Secuencia y fechas dejan de ser viables | Revisar capacidad antes de cambiar asignaciones | Replanificar solo con aprobación humana |

## Hallazgos

| ID | Dimensión | Severidad | Estado | Evidencia | Impacto | Recomendación |
|---|---|---|---|---|---|---|
| AUD-001 | Calendario y equivalencia de vistas | `MAJOR` | `OPEN` | El `.pod` por sprints expone `Calendario CityDrive`/`GMT`; el `.pod` por épicas expone `Calendario CityDrive[Imported]`/`Europe/Madrid` | Las dos vistas pueden producir fechas, límites de sprint, hitos y holguras diferentes | Homogeneizar el calendario aprobado en ambas vistas y aportar una exportación verificable |
| AUD-002 | Traslado, asignaciones, costes y capacidad | `MAJOR` | `NOT_ASSESSABLE` | Los artefactos son binarios serializados y no existe exportación tabular legible | No se puede demostrar que el Hito 4 conserve 21 historias, 102 h-p, 30 h-p de gestión, recursos, tarifas, cargas y 3.300 € | Entregar PDF/CSV/XML o capturas completas de ProjectLibre con tareas, trabajo, recursos, tarifas, costes y carga |
| AUD-003 | Dependencias, ciclos, camino crítico y holguras | `MAJOR` | `NOT_ASSESSABLE` | Se observan objetos de enlace, pero no el grafo completo ni campos de camino crítico/holgura | No se puede confirmar secuencialidad, ausencia de ciclos ni margen temporal | Exportar predecesoras/sucesoras y campos de holgura/camino crítico, o documentar una comprobación observable |
| AUD-004 | Riesgos de Semana 4 | `MAJOR` | `OPEN` | No se localizó registro de riesgos con situación, evento, consecuencia, tratamiento y contingencia | El plan no demuestra tratamiento de sobreasignaciones, diferencias Excel/ProjectLibre, tarifa o ausencia de reserva | Incorporar el registro y obtener decisión humana sobre cada riesgo |
| AUD-005 | Evidencia documental de la baseline | `MINOR` | `OPEN` | La baseline Excel es binaria y la revisión anterior usa métricas agregadas, no una exportación de ProjectLibre | La trazabilidad de la comparación final queda limitada | Adjuntar una exportación legible conservando los archivos originales sin modificarlos |

No se marca ningún hallazgo como `RESOLVED` porque no existe evidencia posterior a una corrección.

## Próximos pasos

1. **AUD-001 — MAJOR:** decidir y documentar el calendario laboral y la zona horaria de referencia; homogeneizar ambas vistas.
2. **AUD-002 — MAJOR:** aportar una exportación o evidencia visual legible de tareas, historias, gestión, recursos, unidades, tarifas, asignaciones, carga y costes.
3. **AUD-003 — MAJOR:** aportar dependencias completas, comprobación de ciclos y evidencia de camino crítico/holguras.
4. **AUD-004 — MAJOR:** registrar los riesgos de planificación y su tratamiento, contingencia y responsable o seguimiento.
5. **AUD-005 — MINOR:** conservar junto a la entrega el manifiesto y una representación legible de la baseline usada para la comparación.

