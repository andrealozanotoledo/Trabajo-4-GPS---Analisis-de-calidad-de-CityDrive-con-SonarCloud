# Informe formal de auditoría de planificación y viabilidad — CityDrive (Semana 4)

- **Proyecto:** CityDrive (MoveTech Solutions / AutoRent)
- **Agente auditor:** `audit-reviewer`
- **Fecha:** 2026-10-14
- **Fuentes auditadas:** `docs/planning/CityDrive_Semana3_FINAL.xlsx`, `docs/planning/README.md`, `specs/product/goals.md`, y ausencia de artefactos nativos de ProjectLibre en `docs/planning/`.
- **Alcance:** revisión de la planificación semestral de Semana 3, alineación con objetivos del producto y viabilidad de capacidad, costes y cronograma.

----

## 1. Resumen ejecutivo

**Veredicto:** APROBADO_CON_CONDICIONES

La planificación de CityDrive revisada en `CityDrive_Semana3_FINAL.xlsx` resulta coherente con el alcance definido en `specs/product/goals.md` y presenta una estructura de trabajo viable en términos de capacidad y margen. El conjunto mantiene 21 historias de usuario, 102 horas-persona de esfuerzo previsto, una capacidad efectiva de 132 horas y un margen global de 30 horas, lo que supone un colchón del 22,7% respecto a la capacidad disponible. La distribución semanal no supera los 22 h efectivas por semana y no se detectan sobreasignaciones individuales.

No obstante, la auditoría no puede validar plenamente la versión “ProjectLibre” del plan porque no existen archivos nativos de ProjectLibre (`.pod`, `.pclx` o equivalentes) en `docs/planning/`. Además, los costes están basados en una tarifa académica provisional de 25 €/h que el propio documento indica como supuesto, no como precio contractual aprobado. En consecuencia, la aprobación es condicionada a la incorporación de la evidencia de ProjectLibre y a la ratificación explícita del supuesto de coste antes de una aprobación formal gestionada por cliente o dirección.

---

## 2. Alcance, fuentes y limitaciones

### 2.1. Fuentes revisadas

- `docs/planning/CityDrive_Semana3_FINAL.xlsx`
- `docs/planning/README.md`
- `specs/product/goals.md`
- `docs/reviews/human-planning-review-v01.md`
- `docs/reviews/initial-planning-review-v02.md` (para contraste histórico de la planificación)

### 2.2. Limitaciones de auditoría

- En `docs/planning/` solo se observan el archivo Excel y el README; no se ha localizado ninguna representación nativa de ProjectLibre.
- La revisión se limita al modelo de planificación contenido en el libro Excel y a los objetivos del producto; no se auditan implementaciones ni pruebas ejecutadas.
- El supuesto de tarifa de 25 €/h se declara como provisional y académico en la revisión humana, por lo que no debe interpretarse como coste contractual real.

---

## 3. Alineación con objetivos del producto

`specs/product/goals.md` establece tres objetivos principales:

- G-01: autonomía del cliente para completar la reserva sin ayuda externa.
- G-02: claridad y confianza en la información del vehículo y la reserva.
- G-03: capacidad de instalación y evaluación del incremento por un tercero.

La planificación revisada cubre, con las historias US-001 a US-021, los ciclos esenciales de búsqueda, selección, reserva, consulta, gestión del catálogo y control de disponibilidad. El modelo de alcance también define exclusiones y restricciones explícitas (pago real, seguros, IoT y uso de datos reales), consistentemente con un MVP académico y controlado.

La trazabilidad funcional resulta coherente con el alcance del producto: la secuencia del flujo principal se articula desde alta de catálogo y consulta de disponibilidad hasta reserva, confirmación, consulta y cancelación. La asignación por épicas y por iteraciones acompaña dicha secuencia sin romper la lógica del recorrido de usuario.

---

## 4. Auditoría del modelo de planificación Excel

### 4.1. Capacidad, carga y equilibrio de trabajo

La hoja `Planificación` del libro confirma los siguientes valores:

- **Historias planificadas:** 21
- **Esfuerzo total:** 102 h
- **Capacidad efectiva total:** 132 h
- **Margen global:** 30 h
- **Capacidad semanal efectiva:** 22 h/semana

La carga por semana es la siguiente:

| Semana | Carga (h) | Capacidad (h) | Margen (h) |
|---|---:|---:|---:|
| 1 | 21 | 22 | 1 |
| 2 | 17 | 22 | 5 |
| 3 | 17 | 22 | 5 |
| 4 | 20 | 22 | 2 |
| 5 | 17 | 22 | 5 |
| 6 | 10 | 22 | 12 |

La tabla evidencia que la planificación no supera el umbral semanal de capacidad efectiva por iteración ni genera sobreasignaciones. Las cargas individuales también permanecen dentro de los límites esperados para cada participante:

- Julia: 20 h planificadas frente a 30 h disponibles
- Andrea: 18 h frente a 24 h
- Óscar: 25 h frente a 30 h
- Borja: 18 h frente a 24 h
- Álvaro: 21 h frente a 24 h

**Conclusión:** la asignación resulta viable y equilibrada. El margen acumulado de 30 h, así como la holgura semestral en Iteración 6, permiten absorber pequeñas desviaciones sin romper la ejecución prevista.

### 4.2. Secuencialidad y flujo crítico

La secuencia funcional del plan es congruente con la lógica de negocio del sistema:

- `US-001` / `US-002` / `US-018`: definición del catálogo y disponibilidad inicial.
- `US-007` / `US-008` / `US-012`: selección y registro de la reserva.
- `US-009` / `US-010` / `US-011`: confirmación, referencia y bloqueo de disponibilidad.
- `US-014` / `US-016` / `US-017`: consulta y gestión de reservas activas.

La secuencia es razonable para un MVP con control de conflictos y reserva por fechas. Aunque el libro Excel no expone un camino crítico formal con holguras calculadas a nivel de tareas, las dependencias funcionales y la distribución por iteración muestran una lógica de precedencia aceptable y no circular.

---

## 5. Auditoría de ProjectLibre y archivos de gestión

### 5.1. Hallazgo principal de la auditoría

**AUD-01 — ProjectLibre no disponible en repositorio**

- **Severidad:** MAJOR
- **Descripción:** No existen artefactos de ProjectLibre dentro de `docs/planning/` ni en el repositorio del proyecto. La auditoría solo puede revisarse el libro Excel, no el modelo nativo de Gantt y recursos de ProjectLibre.
- **Impacto:** no es posible verificar la configuración de calendario, asignaciones de recursos, precedencias internas o ruta crítica a nivel del software de planificación de gestión de proyectos.
- **Recomendación:** incorporar los archivos `.pod`, `.pclx` o el equivalente exportado, y conservar la versión final en `docs/planning/` para que la auditoría pueda validar la planificación sobre la misma baseline técnica.

### 5.2. Evaluación de la evidencia disponible en ProjectLibre

Dado que no se dispone del archivo Base de ProjectLibre, la auditoría no puede confirmar automáticamente:

- calendario laboral exacto,
- días no laborables y festivos,
- costes horarios por integrante,
- dependencias internas de cada tarea,
- camino crítico con holguras,
- asignación de recursos por tareas y sobrecostes.

La evidencia disponible en Excel sugiere que la intención del plan es correcta, pero la comprobación formal de la planificación de gestión del proyecto queda incompleta.

---

## 6. Riesgos, costes y viabilidad económica

### 6.1. Riesgos del proyecto

La revisión del artefacto no incluye un registro explícito de riesgos con tratamiento formal. Este factor no invalida la planificación, pero introduce un riesgo de auditoría y de control de cambios: no se documenta de forma sistemática el tratamiento de incertidumbres operativas, de capacidad o de dependencias con cliente.

**Recomendación:** adjuntar una matriz de riesgos con campos de situación, evento, consecuencia y tratamiento (mitigar, evitar, transferir o aceptar) y una respuesta de contingencia asociada.

### 6.2. Coste estimado

El libro calcula:

- **Coste base del backlog:** 102 h × 25 €/h = 2.550 €
- **Capacidad efectiva disponible:** 132 h
- **Margen de capacidad:** 30 h
- **Presupuesto con contingencia:** 132 h × 25 €/h = 3.300 €
- **Reserva financiera:** 750 € (equivalente a 30 h)

El dato es consistente en términos aritméticos, pero se basa en una tarifa académica provisional. La revisión humana lo reconoce explícitamente como supuesto. Por tanto, el coste debe entenderse como presupuesto de referencia y no como coste real de ejecución ni como tarifa contratada.

---

## 7. Tabla de hallazgos

| ID | Dimensión | Severidad | Descripción | Recomendación |
|---|---|---|---|---|
| AUD-01 | ProjectLibre / trazabilidad de planificación | MAJOR | No se encuentran artefactos nativos de ProjectLibre en `docs/planning/`; por tanto, la validación de dependencias, tareas y camino crítico en ese entorno queda incompleta. | Incluir la versión final del archivo de ProjectLibre y mantenerlo bajo control de versión en `docs/planning/`. |
| AUD-02 | Costes y presupuestos | MINOR | El presupuesto se apoya en una tarifa provisional de 25 €/h, declarada como supuesto académico y no como valor contractual. | Validar la tarifa con cliente o dirección antes de cerrar presupuesto definitivo. |
| AUD-03 | Riesgos y gestión de contingencia | MAJOR | La planificación no muestra una matriz de riesgos formal ni tratamiento concretado para incertidumbres críticas. | Añadir una matriz de riesgos con tratamiento y contingencias para riesgos de disponibilidad, coordinación y desviación de esfuerzo. |

---

## 8. Métricas de viabilidad

| Métrica | Valor | Observación |
|---|---:|---|
| Historias de usuario | 21 | Cobertura adecuada del MVP |
| Esfuerzo total | 102 h | Coherente con el alcance del proyecto |
| Capacidad efectiva total | 132 h | Suficiente para ejecutar el backlog |
| Margen global | 30 h | 22,7% de reserva sobre capacidad |
| Máxima carga semanal | 21 h | Bajo el límite de 22 h |
| Coste base | 2.550 € | Basado en supuesto académico de 25 €/h |
| Coste con contingencia | 3.300 € | Incluye reserva de 750 € |

---

## 9. Dictamen final

**VEREDICTO FINAL: APROBADO_CON_CONDICIONES**

La planificación es técnicamente viable y coherente con los objetivos del producto en los términos revisados. La capacidad, la carga, el margen y la secuencia funcional del plan son compatibles con la ejecución del MVP propuesto. Sin embargo, la aprobación formal queda condicionada a dos requisitos básicos:

1. **Conservación de la evidencia de ProjectLibre** o cualquier equivalente nativo del plan de gestión del proyecto.
2. **Validación explícita del supuesto de tarifa** y documentación del tratamiento de riesgo del proyecto.

Con estas condiciones, el plan puede considerarse viable para avanzar a la siguiente fase de desarrollo y validación del producto.
