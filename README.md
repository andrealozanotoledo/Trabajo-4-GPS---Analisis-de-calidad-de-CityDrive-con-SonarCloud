# Proyecto GPS - CityDrive

## Empresa y producto

- Empresa de desarrollo: MoveTech Solutions.
- Cliente: AutoRent.
- Producto: CityDrive, aplicación orientada a la consulta, reserva y gestión de vehículos.

## Gestión del proyecto

El proyecto se ha gestionado mediante Jira y GitHub siguiendo una estrategia de trabajo basada en GitFlow.

Se han utilizado las ramas principales:

- `main`: versión estable e integrada del proyecto.
- `develop`: rama de integración del desarrollo.
- `feature/*`: ramas independientes para el desarrollo de las Historias de Usuario.

Las tareas y subtareas se han gestionado en Jira y los commits asociados al trabajo se han vinculado mediante Smart Commits.

## Alcance funcional

El proyecto está organizado en seis épicas:

- EP-001 - Búsqueda de vehículos.
- EP-002 - Filtrado y consulta de vehículos.
- EP-003 - Creación de reservas.
- EP-004 - Control de disponibilidad y conflictos.
- EP-005 - Consulta y gestión de reservas.
- EP-006 - Gestión del catálogo de vehículos.

Las Historias de Usuario implementadas se encuentran integradas en `develop` y posteriormente en `main`.

## Pruebas

El proyecto dispone de pruebas automatizadas para validar las distintas funcionalidades implementadas.

La ejecución completa actual mediante:

```bash
python -m pytest -v
```

finaliza correctamente con:

- 160 pruebas superadas.
- 5 subtests superados.

## Integración continua

Se ha configurado integración continua mediante GitHub Actions.

El workflow se encuentra en:

```text
.github/workflows/ci.yml
```

El CI se ejecuta automáticamente sobre las ramas `develop` y `main`, así como en Pull Requests dirigidas a estas ramas.

El workflow:

1. Obtiene el código del repositorio.
2. Configura Python 3.14.
3. Instala `pytest`.
4. Ejecuta automáticamente la suite completa de pruebas.

Las ejecuciones finales del CI en `develop` y `main` se completan correctamente.

## Documentación

La documentación del proyecto se encuentra principalmente en:

- `docs/planning`: planificación temporal y de iteraciones.
- `docs/quality`: Definition of Ready, Definition of Done y evidencias de pruebas.
- `docs/reviews`: revisiones y auditorías realizadas durante el proyecto.
- `docs/revisiones`: revisiones específicas de funcionalidades.

## Estado final

El proyecto dispone de:

- Historias de Usuario integradas.
- Seis épicas finalizadas.
- Integración completa en `develop`.
- Versión final integrada en `main`.
- Suite de pruebas automatizadas superada.
- Integración continua operativa mediante GitHub Actions.

## Enlace

- [Wiki del repositorio](https://github.com/UniExtremadura/Proyecto_GC03/wiki)