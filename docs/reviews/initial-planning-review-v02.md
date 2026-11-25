# Revisión de planificación inicial CityDrive — Semana 3 (v02)

## 1. Metadatos y alcance

- **Proyecto:** CityDrive (MoveTech Solutions / AutoRent).
- **Modo:** READINESS; revisión documental sin aprobación ni modificación de la planificación.
- **Fecha de revisión:** 12-10-2026.
- **Fuente de planificación solicitada:** `docs/planning/CityDrive_Semana3_FINAL.xlsx`.
- **Informe anterior:** `docs/reviews/initial-planning-review-v01.md` (basado en el libro de Semana 2).
- **Fuentes de requisitos y calidad:** catálogo EP-001–EP-006 / US-001–US-021, `specs/product/goals.md`, `docs/quality/definition-of-ready.md` y `docs/quality/definition-of-done.md`.
- **Resultado:** **Coherencia aritmética verificada, con condiciones de trazabilidad y recálculo.** Las cifras actuales caben en las capacidades efectivas y cuadran con las 102 h-p del catálogo. La secuencia de algunas historias dentro de la misma semana y la validez dinámica del control de dependencias requieren cautela; esto no constituye aprobación de la planificación.

Esta revisión usa valores y fórmulas observados en las hojas del libro, y distingue cálculos de controles estáticos. No se reutilizan como evidencia de Semana 3 las cargas, asignaciones, márgenes ni costes consignados en v01 para Semana 2.

## 2. Método y limitaciones de acceso

1. Se inspeccionó el XLSX como contenedor ZIP/XML y se interpretaron nombres de hoja, celdas, fórmulas y valores almacenados (caché de cálculo) de `Resumen`, `Requisitos`, `Capacidad`, `Planificación`, `Carga semanal`, `Costes`, `Viabilidad` e `IT-001 detalle`.
2. Se cotejaron las 21 filas de `Requisitos` y `Planificación`, sus estimaciones, predecesores, semanas y asignaciones; se comprobaron las sumas de carga y margen contra capacidades efectivas por integrante y semana.
3. Se revisaron fórmulas y valores guardados en el XLSX. No se abrió ni guardó el libro con Excel/LibreOffice para forzar un recálculo independiente. Por ello se verifica la estructura y coherencia de las fórmulas, además de la consistencia de los valores almacenados, pero no la ejecución de un motor de hoja de cálculo en esta revisión.
4. Se contrastaron las fuentes legibles de requisitos, objetivos, calidad y la revisión anterior. No se trasladaron a Semana 3 datos de Semana 2.

**Límite:** los valores de fórmula que se citan son los resultados almacenados en el XLSX; no se ejecutó un recálculo con una aplicación de hoja de cálculo. Se identifican por separado los controles estáticos y las dependencias cuya ordenación temporal no queda demostrada solo por compartir semana.

## 3. Evidencia comprobada en las fuentes legibles

### 3.1 Catálogo y esfuerzo de referencia

Se inspeccionaron las seis especificaciones vigentes EP-001–EP-006. Declaran el baseline `Catálogo V0 - Semana 2` y contienen, en conjunto, las historias US-001–US-021. La suma de las estimaciones explícitas en esas historias es **102 h-p**:

| Épica | Historias | Suma de estimaciones expresas |
|---|---|---:|
| EP-001 — Búsqueda de vehículos | US-001–US-003 | 15 h-p |
| EP-002 — Filtrado y consulta de vehículos | US-004–US-006 | 13 h-p |
| EP-003 — Creación de reservas | US-007–US-010 | 20 h-p |
| EP-004 — Control de disponibilidad y conflictos | US-011–US-013 | 16 h-p |
| EP-005 — Consulta y gestión de reservas | US-014–US-017 | 18 h-p |
| EP-006 — Gestión del catálogo de vehículos | US-018–US-021 | 20 h-p |
| **Total del catálogo** | **US-001–US-021 (21 HU)** | **102 h-p** |

La distribución de prioridades que resulta de esas especificaciones es 13 `Must` y 8 `Should`; no se observaron categorías `Could` o `Won't` en las historias revisadas. Las épicas declaran trazabilidad a G-01, G-02 y/o G-03. Esta es la referencia contra la que se cotejaron la cobertura, valores y prioridades del Excel en la tabla siguiente.

### 3.2 Horizonte, capacidad y supuestos de referencia

El libro declara seis iteraciones de una semana y tres releases de dos semanas. En su hoja `Capacidad`, las capacidades nominales por integrante son 6, 5, 6, 5 y 5 h/semana (27 en total); descuenta 1 h/semana a cada integrante y obtiene capacidades efectivas 5, 4, 5, 4 y 4 (22 en total), 132 h efectivas en seis semanas. Frente a las 102 h-p del catálogo, el margen aritmético global es 30 h-p. La carga semanal individual y de equipo se comprueba más abajo contra esos límites.

No se ha leído en las fuentes consultadas una base autorizada para establecer velocidades, factores de conversión o estimaciones adicionales. No se introduce ninguna.

### 3.3 Requisitos de preparación y terminado

- El DoR pide, entre otros, identificador estable, épica, trazabilidad a objetivo, alcance y criterios verificables, prioridad, estimación, incertidumbre y dependencias/predecesores conocidos, y que no queden dudas que impidan planificar. El catálogo aporta esas referencias; el plan conserva IDs, prioridad, estimación, incertidumbre y predecesores, y el detalle de IT-001 enlaza tareas con criterios. La trazabilidad del plan a objetivos se conserva indirectamente mediante la épica/especificación, no como campo explícito de cada fila planificada. Sigue existiendo una discrepancia documental sobre la evidencia de M-01/M-02 en US-009 (R-PL-05).
- El DoD define condiciones de terminado del trabajo (implementación, revisión, pruebas, integración, ausencia de bloqueos, trazabilidad y documentación, entre otras). Un plan de esfuerzo por sí solo no demuestra que una HU o una iteración cumpla el DoD.
- En `goals.md`, G-01 cubre la autonomía del recorrido de reserva, G-02 la comprensión y confianza y G-03 un incremento revisable. Estos objetivos son el marco documental para revisar la trazabilidad; no permiten inferir la asignación o prioridad anotada en Excel.

## 4. Comprobaciones solicitadas y estado de evidencia

| Comprobación | Evidencia observable y resultado |
|---|---|
| Cobertura de las 21 HU | **Cumple:** `Planificación` contiene una fila para cada US-001–US-021, sin duplicados; las 21 IDs corresponden a `Requisitos`. La columna de esfuerzo de las historias suma 102 h-p. |
| Predecesores | Los predecesores consignados en `Planificación` coinciden con los del catálogo revisado. Las dependencias entre semanas quedan en orden. Hay dependencias dentro de la misma semana (US-001→US-002→US-003 en IT-001; US-009→US-010/US-011/US-017 y US-014→US-015 en semanas posteriores). En IT-001, la hoja de detalle presenta tareas ordenadas por esa secuencia. Para las dependencias intra-semana restantes, el plan las coloca en la misma iteración y en orden de filas, pero no representa una relación/tarea explícita; la garantía depende de respetar esa secuencia durante la ejecución. |
| Responsable | **Cumple en cobertura:** las 21 historias tienen uno o más responsables no vacíos, y la distribución numérica de horas coincide con la lista de responsables de cada fila. |
| Cargas por persona y semana | **Cumple:** no hay cargas superiores a capacidad efectiva. Capacidades semanales (Julia/Andrea/Óscar/Borja/Álvaro): 5/4/5/4/4 h. Cargas, por semana: S1 5/4/5/3/4; S2 3/3/4/3/4; S3 3/3/5/3/3; S4 4/3/5/4/4; S5 3/3/4/3/4; S6 2/2/2/2/2. |
| Trabajo no asignado | **No se observa trabajo sin asignar:** en las 21 filas de `Planificación`, la suma por personas iguala la estimación de la historia (diferencia cero) y hay responsables; no existe fila adicional de esfuerzo de proyecto sin imputar. |
| Margen | **Cumple aritméticamente:** margen semanal de equipo S1–S6 = 1, 5, 5, 2, 5 y 12 h (total 30). Margen acumulado por persona (Julia/Andrea/Óscar/Borja/Álvaro) = 10/6/5/6/3 h. El margen individual mínimo semanal es 0 h. Los márgenes usan capacidad efectiva, no nominal, y no incluyen esfuerzo sin asignar. |
| Coherencia con 102 h-p | **Cumple:** los valores consensuados de las 21 historias suman 102 h-p; la distribución por semanas (21+17+17+20+17+10) y por personas (20+18+25+18+21) también suma 102 h-p. No se añade esfuerzo total fuera de esas historias. |
| Costes por persona, iteración y proyecto | Con la tarifa editable de **25 €/h**, expresamente un **supuesto académico provisional** y no una tarifa oficial del cliente ni del profesor, los costes por persona (Julia/Andrea/Óscar/Borja/Álvaro) son 500/450/625/450/525 € (total 2.550 €). Por iteración S1–S6: 525/425/425/500/425/250 €; suman 2.550 €. Los importes son coherentes con horas × tarifa y no constituyen una valoración oficial. |
| Fórmulas recalculables | **Parcialmente cumple:** sumas de esfuerzo, reparto por persona/semana, márgenes, costes y resúmenes están formulados con fórmulas Excel estándar y sus valores almacenados son aritméticamente coherentes. No se ejecutó recálculo externo. El contador de historias del resumen (`Resumen!A5`) y el control de dependencias (`Viabilidad!B9:C9`) son valores estáticos; el estado global no recalcula ese control ante cambios del plan. Por ello el libro no actualiza automáticamente todas las verificaciones relevantes al editarlo. |
| Detalle de Iteración 1 | **Detalle suficiente para trazabilidad básica:** 14 tareas (T-001–T-014) describen trabajo ligado a US-018, US-001, US-002 y US-003, indican responsable, horas y referencias a criterios/verificación. Los totales por historia y persona reproducen exactamente el reparto de IT-001: 21 h-p y 5/4/5/3/4 h. La secuencia de tareas muestra US-001 antes de US-002 y US-002 antes de US-003. |
| Horizonte de seis semanas / releases | **Cumple en el libro:** seis semanas/iteraciones (IT-001 a IT-006) y tres releases de dos semanas (R1–R3); el agrupamiento semanal coincide con las seis iteraciones. |
| No incorporar nuevos factores/estimaciones/velocidades | No se introduce una velocidad ni factor de conversión. El total de estimación de las HU sigue siendo el catálogo vigente de 102 h-p. Sin embargo, la hoja de IT-001 asigna horas numéricas a tareas (1–2 h cada una): suman exactamente las horas ya estimadas por historia, pero el libro no identifica esas horas de tarea como estimaciones independientes aprobadas. Deben entenderse solo como desglose interno del esfuerzo existente, no como nuevas estimaciones de alcance. |
| DoR y evidencia de objetivos | Las HU tienen los campos principales de planificación y las épicas enlazan con objetivos. Persiste en US-009 una discrepancia entre su verificación determinista y la evidencia de participantes exigida por `goals.md` para M-01/M-02; el libro no desglosa cómo se cubrirá esa evidencia. Esto no cambia las 7 h-p de US-009 ni autoriza a añadir esfuerzo en esta revisión. |

## 5. Incidencias y límites

### R-PL-01 — Control de dependencias no dinámico

- **Severidad:** Condición para mantener la validez ante cambios; no es una infracción observada en los datos actuales.
- **Evidencia:** en `Viabilidad!B9` figura `OK` como valor literal y `C9` contiene un texto literal que afirma que la secuencia está revisada. El estado global `B13` se calcula a partir de `B4:B9`, pero no comprueba los predecesores. `Resumen!A5` también contiene el valor constante 21 en vez de contar las historias.
- **Impacto:** las celdas no reflejan cambios de iteración o dependencias ni detectan automáticamente omisiones/duplicados si se edita el plan. Los datos actuales sí coinciden con el catálogo y la secuencia, con las reservas de dependencias dentro de una misma semana ya indicadas.
- **Estado:** Limitación funcional de las comprobaciones del libro; no invalida por sí sola los resultados actuales.

### R-PL-02 — Alcance de la revisión anterior

- **Evidencia:** `initial-planning-review-v01.md` documenta `CityDrive_Semana2.xlsx`, con cargas y márgenes por iteración, y formula un veredicto para aquella planificación.
- **Impacto:** esa evaluación no demuestra la corrección del nuevo libro Semana 3. Las cifras de IT-001–IT-006 y los márgenes de v01 no se trasladan como resultados de este recheck.
- **Estado:** Limitación de comparabilidad; no es una no conformidad del plan Semana 3.

### R-PL-03 — Desglose horario de tareas de IT-001

- **Evidencia:** `IT-001 detalle` asigna 21 h a 14 tareas y liga las tareas a historias/criterios. La suma por historia y por persona coincide con el plan y las estimaciones consensuadas; el libro no señala una fuente ni aprobación separada para la granularidad de 1–2 h por tarea.
- **Impacto:** no aumenta el total de 102 h-p, pero si esas horas se interpretaran como estimaciones nuevas de tarea en vez de reparto del esfuerzo ya acordado, sería una estimación adicional no sustentada por el catálogo.
- **Estado:** Válido únicamente como desglose interno de las 21 h-p de las cuatro historias; no se valida como baseline de estimaciones independientes a nivel de tarea.

### R-PL-04 — Dependencias compartiendo iteración

- **Evidencia:** US-009 precede a US-010, US-011 y US-017, asignadas también a la semana 4; US-014 precede a US-015, ambas en semana 5. Las filas aparecen en orden de predecesor y luego sucesoras. En IT-001, el detalle sí concreta el orden entre US-001, US-002 y US-003.
- **Impacto:** la semana asignada no contradice por sí misma una precedencia si se respeta la secuencia dentro de la iteración. Para las semanas 4 y 5 no hay desglose equivalente que materialice ese orden en tareas; el control automático del libro tampoco lo valida.
- **Estado:** Condición de ejecución/seguimiento; no se detecta inversión de precedencias en la planificación por semanas.

### R-PL-05 — Evidencia de M-01/M-02 en US-009

- **Evidencia:** la especificación de US-009 dice que la verificación funcional determinista servirá como evidencia para M-01/M-02; `goals.md` aclara que las pruebas funcionales no bastan y exige evaluar el escenario con cinco participantes. `Planificación` asigna US-009 7 h-p a la semana 4, pero no desglosa tareas o evidencia de participantes.
- **Impacto:** el libro sí planifica US-009, pero no puede comprobarse si la medición de objetivos está dentro de las tareas/horas asignadas. Esto deja una duda respecto al DoR y la trazabilidad de resultados, no una ausencia demostrada de capacidad ni una base para inventar esfuerzo adicional.
- **Estado:** Incompatibilidad documental que condiciona la confianza en la cobertura de objetivos; no se modifican requisitos ni estimaciones.

## 6. Conclusión

**Resultado de la revisión de Semana 3: aritméticamente coherente con condiciones.** El libro contiene las 21 HU del catálogo y sus 102 h-p; cada HU tiene responsables, las cargas individuales y de equipo no superan capacidad efectiva, no se observa trabajo sin asignar, los márgenes cuadran y los costes son coherentes bajo el supuesto académico provisional de 25 €/h. IT-001 tiene un desglose de tareas trazable cuya suma conserva las estimaciones originales.

Se identifican condiciones: la secuencia entre dependencias que comparten semana debe respetarse durante la iteración; el estado automático de viabilidad no recalcula dependencias y algunos indicadores (como el recuento de historias) son constantes; las horas del detalle IT-001 deben tratarse como desglose de las estimaciones de HU, no como nuevas estimaciones independientes; y queda por aclarar cómo se medirá M-01/M-02 para US-009 sin añadir esfuerzo no aprobado. Los valores/fórmulas se inspeccionaron, pero no se forzó el recálculo con Excel/LibreOffice.

Este resultado **no es una aprobación ni un rechazo automático**, y no modifica ni propone cambios a la planificación. Determina que sus cifras principales cuadran con las fuentes y capacidades indicadas, dejando explícitas las reservas de control y evidencia descritas.

## 7. Manifiesto de fuentes consultadas

| Ruta | Uso en esta revisión | Límite |
|---|---|---|
| `docs/planning/CityDrive_Semana3_FINAL.xlsx` | Hojas, valores, fórmulas y resultados almacenados de `Resumen`, `Requisitos`, `Capacidad`, `Planificación`, `Carga semanal`, `Costes`, `Viabilidad` e `IT-001 detalle`. | No se ejecutó un recálculo independiente en Excel/LibreOffice; se señalan controles estáticos y secuencias intra-semana sin desglosar. |
| `docs/planning/README.md` | Confirmación de que la carpeta contiene documentos de planificación de CityDrive. | No define capacidad individual, tarifas ni datos de la planificación. |
| `specs/EP-001 - Búsqueda de vehículos/spec.md` a `specs/EP-006 - Gestión del catálogo de vehículos/spec.md` | IDs, épicas, prioridades, estimaciones y predecesores especificados; comparación con el libro. | No sustituyen la evidencia de ejecución ni aprobación de tareas. |
| `specs/product/goals.md` | G-01–G-03, métricas y alcance. | No prueba que la planificación incluya trabajo asociado. |
| `docs/quality/definition-of-ready.md` | Criterios de preparación de HU. | Se revisó como marco documental; no se atribuye al plan evidencia de terminado o ejecución. |
| `docs/quality/definition-of-done.md` | Criterios compartidos de terminado. | No se inspeccionó implementación ni evidencia de pruebas; el plan de esfuerzo no demuestra DoD. |
| `specs/EP-003 - Creación de reservas/spec.md` (US-009) | Predecesores, estimación y requisito de verificación de US-009. | La indicación de evidencia M-01/M-02 diverge de la regla de `goals.md`; se señala, no se resuelve en esta revisión. |
| `docs/reviews/initial-planning-review-v01.md` | Contraste de alcance y referencia Semana 2. | No se extrapolan sus resultados al nuevo libro. |
| `docs/organization/` | Inspección del directorio para localizar artefactos organizativos adicionales. | Solo contiene `.gitkeep`; no se encontró allí una declaración legible de límites individuales. |

No se modificaron el Excel, los requisitos, las estimaciones ni la planificación.
