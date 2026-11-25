# GC03-14 — ST-0161: Revisión de condiciones de cancelación

## Objetivo
Comprobar que las condiciones funcionales de cancelación de reservas coinciden con los criterios de aceptación de US-016.

## Archivos revisados
- src/citydrive/reservas/cancelacion.py
- src/models/cancelacion_disponibilidad.py
- src/services/cancelacion_disponibilidad_service.py
- test_cancelacion.py

## Resultados por criterio de aceptación

AC-01 — Cancelar una reserva localizada por referencia.
Estado: No verificado.
La función cancelar_reserva recibe directamente un objeto Reserva. No se ha identificado en los archivos revisados una búsqueda previa por referencia.

AC-02 — Solo se pueden cancelar reservas activas.
Estado: Verificado.
La función comprueba que el estado sea "activa" y rechaza los demás estados mediante ValueError.

AC-03 — La reserva pasa al estado cancelada.
Estado: Verificado.
La función modifica el estado de la reserva a "cancelada".

AC-04 — El vehículo recupera disponibilidad para el periodo correspondiente.
Estado: Parcial.
El servicio de disponibilidad permite establecer el estado general del vehículo como DISPONIBLE, pero no comprueba el periodo de reserva ni posibles reservas coincidentes. Tampoco verifica por sí mismo que la cancelación esté confirmada.

AC-05 — Informar de errores sin modificar los datos.
Estado: Parcial.
Se rechazan reservas no activas sin modificar su estado. No se ha verificado el tratamiento de reservas inexistentes ni la integración con el almacenamiento de datos.

## Pruebas ejecutadas
Comando: python -m test_cancelacion

- RES-001: reserva activa, cancelación correcta.
- RES-002: reserva cancelada, operación rechazada.
- RES-003: reserva pendiente, operación rechazada.

Resultado: Todas las pruebas superadas.

## Conclusión
La implementación revisada cumple las condiciones básicas de cancelación de reservas activas y actualización de su estado. Quedan pendientes de verificación la búsqueda por referencia, la liberación de disponibilidad por fechas y el tratamiento completo de reservas inexistentes.

Esta revisión no modifica la implementación existente.
