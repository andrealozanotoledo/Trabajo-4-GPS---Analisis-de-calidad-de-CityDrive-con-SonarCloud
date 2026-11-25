# GC03-23 - Definición del flujo de consulta por referencia

## Historia de usuario

US-014 - Consultar reserva por referencia.

## Objetivo

Definir el proceso que permite consultar una reserva mediante
su referencia identificativa, sin modificar sus datos.

## Flujo principal

1. El usuario accede a la consulta de reservas.
2. El sistema solicita la referencia de la reserva.
3. El usuario introduce la referencia.
4. El sistema elimina los espacios iniciales y finales.
5. El sistema comprueba que la referencia no esté vacía.
6. El sistema busca la reserva correspondiente.
7. Si existe, recupera sus datos.
8. El sistema muestra la información de la reserva.

## Datos mostrados

- Referencia de la reserva.
- Vehículo reservado.
- Fecha de inicio.
- Fecha de fin.

## Flujos alternativos

### Referencia vacía

Si el usuario no introduce una referencia válida,
el sistema muestra:

"Debes introducir una referencia de reserva."

### Reserva inexistente

Si no existe ninguna reserva asociada a la referencia,
el sistema muestra:

"No se ha encontrado ninguna reserva con esa referencia."

## Restricciones funcionales

- La consulta no debe modificar los datos de la reserva.
- La búsqueda debe realizarse utilizando la referencia introducida.
- Solo se mostrarán los datos de una reserva encontrada.
- El sistema debe informar claramente cuando no haya resultados.

## Implementación existente

La función consultar_por_referencia, situada en
src/views/consulta_referencia.py, implementa la validación
de la referencia y la presentación de resultados.

La búsqueda se proporciona mediante el parámetro buscar_reserva.

Los archivos src/models/reserva.py y
src/services/reserva_service.py están vacíos en la versión revisada.

## Validación existente

Archivo: tests/test_gc03_109.py

Se han identificado cuatro pruebas:

1. Consulta de referencia existente.
2. Consulta de referencia inexistente.
3. Consulta con referencia vacía.
4. Consulta sin modificación de los datos originales.

Estas pruebas todavía deben ejecutarse para confirmar su resultado.
