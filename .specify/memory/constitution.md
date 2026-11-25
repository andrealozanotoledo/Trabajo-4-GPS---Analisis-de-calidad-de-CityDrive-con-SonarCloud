# Constitución del Proyecto CityDrive

## Core Principles (Principios Fundamentales)
1. **Especificación y trazabilidad:** Toda funcionalidad debe estar especificada antes de implementarse. Debe poder seguirse la relación: Necesidad -> requisito -> plan -> tareas -> código -> pruebas. No se implementarán funcionalidades que no estén justificadas por una especificación aprobada.
2. **Disciplina de alcance del MVP:** El equipo debe centrarse en las funcionalidades necesarias para obtener un producto mínimo viable. Las ampliaciones de alcance deberán estar justificadas, priorizadas y evaluar su impacto en plazo, coste y capacidad.
3. **Calidad y comportamiento verificable:** Los requisitos deben ser claros, medibles y comprobables. Cada funcionalidad debe incluir criterios de aceptación, tratamiento de errores y pruebas adecuadas cumpliendo la definición de terminado (Definition of Done).
4. **Seguridad, privacidad y datos sintéticos:** El proyecto utilizará exclusivamente datos ficticios o sintéticos. La solución deberá evitar el uso de datos personales reales, validar las entradas y proteger la información.
5. **Usabilidad y accesibilidad:** Las funcionalidades deben ser comprensibles, consistentes y fáciles de utilizar. Los flujos principales y los mensajes de error deberán diseñarse teniendo en cuenta la diversidad de usuarios.

## Development and Documentation Standards
Cada artefacto tiene una responsabilidad diferente:
* `spec.md`: explica qué se necesita y por qué.
* `plan.md`: explica cómo se abordará técnicamente.
* `tasks.md`: descompone el plan en trabajo concreto y ejecutable.
Las decisiones importantes deberán quedar documentadas y los artefactos deberán mantener la trazabilidad entre ellos.

## Quality Gates and Delivery Workflow
Antes de aprobar una especificación, un plan o una implementación, debe comprobarse que:
* Cumple los principios de esta constitución.
* Respeta el alcance acordado.
* Mantiene la trazabilidad y define criterios verificables.
* Considera calidad, pruebas, seguridad y accesibilidad.
* No contiene decisiones importantes sin justificar.

## Governance
La constitución tiene prioridad sobre el resto de los documentos del proyecto.
Cualquier modificación deberá:
* Estar justificada y ser aprobada explícitamente.
* Registrar la fecha y la nueva versión.
* Indicar qué documentos o decisiones resultan afectados.
Las excepciones deberán ser explícitas, justificadas, aprobadas y, cuando sea posible, temporales.