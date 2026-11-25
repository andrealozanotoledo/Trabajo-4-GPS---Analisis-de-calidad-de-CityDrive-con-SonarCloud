
# Informe de Revisión Inicial de Planificación (v01)

- **Proyecto:** CityDrive (MoveTech Solutions / AutoRent)
- **Agente evaluador:** `initial-planning-reviewer`
- **Modo:** READINESS (Preparación y viabilidad)
- **Fuente analizada:** `docs/planning/CityDrive_Semana2.xlsx`
- **Fecha:** Semana 3

---

## 1. Resumen Ejecutivo y Dictamen de Preparación

- **Veredicto general:** READY_WITH_CONDITIONS (Preparado con condiciones para la línea base).
- **Justificación:** El alcance preliminar (21 US, 102 h-p) se encuentra acotado, estimado de forma consensuada y resulta viable frente a la capacidad efectiva declarada (132 h efectivas, 6 iteraciones). Se identifican condiciones de secuencia y asignación que deben ser controladas en la ejecución.

---

## 2. Dimensiones Evaluadas

### 2.1. Alcance y Priorización (MoSCoW)

- **Total de historias:** 21 historias de usuario estructuradas en 6 épicas.
- **Distribución:** 13 historias clasificadas como `Must` (62%) y 8 historias como `Should` (38%). Cumple con el criterio de no saturar el MVP con elementos accesorios (`Could` y `Won't` se mantienen en 0).
- **Trazabilidad:** Coherente con los objetivos estratégicos G-01, G-02 y G-03 fijados para el cliente AutoRent.

### 2.2. Capacidad y Carga de Trabajo

- **Capacidad nominal:** 27 h/semana.
- **Capacidad efectiva declarada:** 22 h/semana (factor de dedicación neta que descuenta coordinación y gestión).
- **Capacidad total horizonte (6 semanas):** 132 h.
- **Esfuerzo total estimado:** 102 h-p.
- **Margen de contingencia global:** 30 h (22,7% de holgura disponible frente a incertidumbres).

### 2.3. Secuencia Temporal y Viabilidad de Iteraciones

| Iteración       | Release   | Esfuerzo (h-p) | Capacidad (h) | Margen (h) | Estado de Carga               |
| :--------------- | :-------- | :------------: | :-----------: | :--------: | :---------------------------- |
| **IT-001** | Release 1 |       21       |      22      |     +1     | Carga alta (95,5%)            |
| **IT-002** | Release 1 |       17       |      22      |     +5     | Carga adecuada (77,3%)        |
| **IT-003** | Release 2 |       17       |      22      |     +5     | Carga adecuada (77,3%)        |
| **IT-004** | Release 2 |       20       |      22      |     +2     | Carga media-alta (90,9%)      |
| **IT-005** | Release 3 |       17       |      22      |     +5     | Carga adecuada (77,3%)        |
| **IT-006** | Release 3 |       10       |      22      |    +12    | Carga reducida (buffer final) |

---

## 3. Condiciones y Recomendaciones para la Línea Base

1. **Atención a IT-001 e IT-004:** Presentan márgenes reducidos (+1 h y +2 h). Cualquier desviación en el alta de catálogo (US-018) o en la concurrencia de bloqueo (US-011, US-012) requerirá absorber holgura en las iteraciones subsiguientes.
2. **Buffer de estabilización en IT-006:** La iteración final dispone de 12 h de margen, lo que asegura capacidad suficiente para pruebas de integración globales, corrección de defectos y entrega final del prototipo sin comprometer el calendario.
3. **Respeto a precedencias:** Se valida la ordenación lógica del flujo: catálogo base -> búsqueda y consulta -> bloqueo y concurrencia -> gestión de reserva -> administración y cancelación.
