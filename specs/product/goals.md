# Objetivos y Alcance: CityDrive

## Objetivos

| ID | Objetivo | Resultado esperado |
|---|---|---|
| G-01 | Autonomía del cliente | El usuario puede completar el recorrido esencial de una reserva sin ayuda externa. |
| G-02 | Claridad y confianza | El usuario comprende el vehículo elegido, las fechas y el estado de su reserva. |
| G-03 | Incremento revisable | Un tercero puede instalar, ejecutar y evaluar de manera estable el incremento desarrollado. |

## Indicadores de éxito

| ID | Objetivo | Meta |
|---|---|---|
| M-01 | G-01 | Al menos cuatro de cinco participantes completan el escenario de reserva en menos de diez minutos y sin ayuda. |
| M-02 | G-02 | Al menos cuatro de cinco participantes comprenden correctamente qué vehículo han reservado y para qué fechas. |
| M-03 | G-03 | Una persona que no haya implementado el producto puede seguir el guion de instalación sin intervenciones no documentadas. |
| M-04 | Todos | No existe ningún defecto bloqueante abierto durante la revisión final. |

## Stakeholders

Los principales stakeholders del proyecto CityDrive son:

- **Clientes de AutoRent:** Usuarios finales que consultarán la disponibilidad de vehículos y realizarán reservas.
- **Personal de AutoRent:** Encargado de mantener la información de los vehículos y consultar las reservas activas.
- **Dirección de AutoRent:** Interesada en mejorar la gestión de las reservas y modernizar el servicio ofrecido a los clientes.
- **Equipo de desarrollo MoveTech Solutions:** Responsable de la planificación, desarrollo, pruebas y evolución del producto.

## Alcance incluido

El proyecto incluye:

- **S-01:** Un recorrido esencial y coherente para la búsqueda, filtrado y reserva individual de un vehículo por días.
- **S-02:** Un catálogo controlado de vehículos y reservas completamente ficticios.
- **S-03:** Funciones básicas para que el personal de AutoRent pueda mantener el catálogo de vehículos y consultar las reservas necesarias para la demostración.

## Modelo mínimo de datos sintéticos

Para mantener una definición común y verificable en todo CityDrive, se establece el siguiente modelo mínimo de datos para los vehículos y las reservas utilizadas en el proyecto.

### Vehículo

Cada vehículo estará definido mediante los siguientes campos:

- **id:** Identificador único del vehículo.
- **marca:** Marca del vehículo.
- **modelo:** Modelo del vehículo.
- **categoría:** Coche o furgoneta.
- **plazas:** Número de plazas disponibles.
- **maletero/carga:** Capacidad de maletero o carga.
- **transmisión:** Manual o automática.
- **estado operativo:** Disponible o no disponible.

### Reserva

Cada reserva estará definida mediante los siguientes campos:

- **referencia:** Identificador único alfanumérico de la reserva.
- **vehiculoId:** Identificador del vehículo asociado a la reserva.
- **fecha inicio:** Primer día de la reserva.
- **fecha fin:** Último día de la reserva.
- **nombre y apellidos:** Datos ficticios del cliente.
- **correo electrónico:** Dirección de correo ficticia.
- **estado:** Confirmada o cancelada.

Todos los datos utilizados durante el desarrollo, demostración y pruebas serán ficticios, de acuerdo con las restricciones definidas para CityDrive.

## Exclusiones

Quedan expresamente fuera del proyecto:

- **EX-01:** Procesamiento de pagos reales, pasarelas de pago o facturación.
- **EX-02:** Integraciones con aseguradoras de vehículos.
- **EX-03:** Apertura de puertas mediante hardware o integración IoT con la flota física.

## Supuestos

Para el desarrollo de CityDrive se parte de los siguientes supuestos:

- La información del catálogo de vehículos será ficticia y estará disponible para el desarrollo y las pruebas.
- Cada vehículo solo podrá estar reservado por un cliente para un mismo rango de fechas.
- El sistema trabajará únicamente con la agencia AutoRent.
- No será necesario conectarse con sistemas externos para consultar la disponibilidad de los vehículos.
- Los usuarios dispondrán de acceso a Internet y de un navegador web actualizado.

## Restricciones

El proyecto debe respetar las siguientes condiciones:

- Prohibición de utilizar datos personales, bancarios o de conducción reales.
- Uso exclusivo de las tecnologías y convenciones aprobadas en el curso.
- El desarrollo deberá ajustarse al tiempo y capacidad disponible del equipo.

## Criterios transversales de verificación

### Verificación técnica

Para las historias relacionadas con la consulta de información y la confirmación de reservas se aplicarán los siguientes criterios durante la validación del MVP:

- Las operaciones de consulta y confirmación deberán ofrecer una respuesta observable en la interfaz en menos de 2 segundos en el entorno local de pruebas del proyecto.
- La verificación funcional se realizará mediante pruebas deterministas utilizando datos sintéticos.
- No se requieren pruebas de carga, estrés o rendimiento propias de un entorno de producción industrial.
- Los mensajes mostrados al usuario deberán permitir identificar el resultado de la operación o el motivo por el que no puede completarse.

### Evidencia de las métricas M-01 y M-02

Las pruebas funcionales y las mediciones de tiempo de respuesta anteriores verifican el comportamiento técnico del sistema, pero no constituyen por sí solas evidencia suficiente para las métricas M-01 y M-02.

- **M-01** se verificará mediante la realización del escenario completo de reserva con cinco participantes. La métrica se considerará cumplida si al menos cuatro de los cinco completan el escenario en menos de diez minutos y sin ayuda.
- **M-02** se verificará con esos participantes comprobando, una vez realizado el escenario, que pueden identificar correctamente el vehículo reservado y las fechas de la reserva. La métrica se considerará cumplida si al menos cuatro de los cinco responden correctamente.
- Los resultados de estas evaluaciones se conservarán como evidencia separada de las pruebas funcionales deterministas y de las mediciones de rendimiento.

## Trazabilidad

La cadena de trazabilidad será:

**Misión -> objetivos -> épicas -> historias -> tareas -> código y pruebas -> evidencias.**

Una épica que no contribuya a ningún objetivo se considera fuera del alcance hasta que se apruebe un cambio en los objetivos o en el alcance del proyecto.

## Gestión de cambios

Cualquier modificación de los objetivos, métricas, alcance, exclusiones, supuestos o restricciones requerirá:

1. Revisión por parte del equipo.
2. Decisión explícita del Product Owner.
3. Registro de la decisión tomada.
4. Revisión de la planificación y de la capacidad del equipo si fuera necesario.
5. Actualización de los documentos y referencias afectadas.