# Revisión humana de la planificación — Semana 3

## Metadatos

- **Proyecto:** CityDrive
- **Empresa:** MoveTech Solutions
- **Cliente:** AutoRent
- **Informe de IA revisado:** `docs/reviews/initial-planning-review-v02.md`
- **Herramienta:** GitHub Copilot Chat
- **Modelo utilizado:** GPT-6 Luna
- **Fecha:** 12-10-2026
- **Artefacto revisado:** `docs/planning/CityDrive_Semana3_FINAL.xlsx`

## Resultado de la revisión humana

El equipo ha revisado las observaciones realizadas por el Planning Agent sobre la primera planificación de CityDrive.

La planificación mantiene las 21 Historias de Usuario y las 102 h-p estimadas en el catálogo. No se han detectado sobreasignaciones, trabajo sin responsable ni incompatibilidades con la capacidad efectiva disponible.

Las recomendaciones del agente se clasifican a continuación.

---

## R-PL-01 — Control de dependencias no dinámico

**Decisión:** ACCEPTED_WITH_CHANGES

**Justificación:**

El equipo acepta que algunos controles del libro, como el recuento de historias y la comprobación general de dependencias, no se recalculan automáticamente.

No se modifica la planificación porque las dependencias actuales han sido revisadas y su secuencia es correcta.

Los cálculos principales exigidos para la planificación —carga, capacidad, margen y costes— sí se encuentran basados en fórmulas.

Si posteriormente se modifica la asignación temporal de las historias, las dependencias deberán volver a revisarse.

---

## R-PL-02 — Alcance de la revisión anterior

**Decisión:** ACCEPTED

**Justificación:**

El equipo acepta que `initial-planning-review-v01.md` corresponde a una versión anterior de la planificación y no se utiliza como evidencia de la planificación definitiva de Semana 3.

La revisión vigente es `initial-planning-review-v02.md`, realizada sobre `CityDrive_Semana3_FINAL.xlsx`.

---

## R-PL-03 — Desglose horario de tareas de IT-001

**Decisión:** ACCEPTED

**Justificación:**

Las horas asignadas a las tareas de IT-001 se consideran exclusivamente un desglose interno de las estimaciones ya aprobadas a nivel de Historia de Usuario.

No constituyen nuevas estimaciones independientes ni incrementan el esfuerzo total del proyecto.

El total de IT-001 continúa siendo de 21 h-p.

---

## R-PL-04 — Dependencias que comparten iteración

**Decisión:** ACCEPTED_WITH_CHANGES

**Justificación:**

El equipo acepta que varias historias con relación de precedencia se encuentran dentro de una misma iteración.

Esto no supone una contradicción siempre que durante la ejecución se respete el orden entre la historia predecesora y sus sucesoras.

En IT-001 este orden ya aparece detallado a nivel de tareas.

Para las iteraciones posteriores, la secuencia concreta se detallará cuando se realice la planificación de tareas de cada iteración.

No se modifica la distribución actual por semanas.

---

## R-PL-05 — Evidencia de M-01 y M-02 en US-009

**Decisión:** ACCEPTED_WITH_CHANGES

**Justificación:**

El equipo interpreta la verificación funcional de US-009 como evidencia técnica complementaria, no como evidencia suficiente por sí sola para las métricas M-01 y M-02.

La evaluación principal de M-01 y M-02 será la definida en `specs/product/goals.md`, mediante la evaluación con cinco participantes.

Como esta primera planificación se realiza a nivel de Historia de Usuario, el detalle de las actividades de evaluación correspondientes a US-009 se concretará cuando se planifique la iteración en la que se ejecutará dicha historia.

No se modifica en esta fase la estimación de 7 h-p de US-009 ni se inventa esfuerzo adicional.

---

## Supuesto de costes

La tarifa de **25 €/h por integrante** utilizada en el Excel se mantiene exclusivamente como un supuesto académico provisional para permitir realizar los cálculos requeridos de coste.

No representa una tarifa oficial proporcionada por AutoRent, MoveTech Solutions o el profesorado.

Si posteriormente se proporciona una tarifa oficial, se sustituirá este valor y los costes se recalcularán mediante las fórmulas del libro.

---

## Decisión final

Tras la revisión humana de las observaciones del Planning Agent, el equipo considera que la primera planificación de CityDrive es válida para el Hito 3.

Se mantienen:

- 21 Historias de Usuario planificadas.
- 102 h-p de esfuerzo total.
- 132 h de capacidad efectiva.
- 30 h de margen de capacidad.
- Ausencia de sobreasignaciones individuales.
- Todas las historias con responsables.
- Coste provisional de 2.550 € bajo el supuesto académico de 25 €/h.
- Desglose detallado de IT-001.
- Secuenciación de las dependencias a respetar durante la ejecución.

No se realizan cambios adicionales en requisitos, estimaciones o planificación como resultado de esta revisión.