# US-021 — Pruebas funcionales del catálogo y rendimiento

## 1. Identificación

- **Historia de usuario:** GC03-18 — US-021: Consultar catálogo completo.
- **Subtarea:** GC03-63 — ST-0214: Probar catálogo y tiempo de respuesta.
- **Responsable:** Borja Gómez Castaño.
- **Fecha:** 07/11/2026.
- **Estado:** Pruebas automatizadas superadas.

## 2. Objetivo

Comprobar que CityDrive permite consultar correctamente el catálogo completo de vehículos, mostrando los datos almacenados y sus estados operativos.

También se verifica que las consultas reflejan las modificaciones del estado de los vehículos y que el tiempo de ejecución del servicio es inferior a dos segundos en un escenario local con un catálogo de mayor tamaño.

## 3. Componentes utilizados

Se han utilizado los siguientes archivos:

- `src/citydrive/models/vehiculo.py`: modelo de datos del vehículo.
- `src/citydrive/services/catalogo.py`: registro y consulta de vehículos.
- `src/services/obtener_vehiculos_catalogo.py`: servicio de obtención del catálogo.
- `tests/test_catalogo_rendimiento.py`: pruebas propias de GC03-63.
- `tests/test_gc03_21.py`: pruebas funcionales existentes de GC03-21.

Las pruebas se han realizado con Python y el módulo `unittest`, utilizando datos ficticios y sin modificar la implementación de los compañeros.

## 4. Datos de prueba

Se han registrado inicialmente dos vehículos ficticios:

| Campo | Vehículo 1 | Vehículo 2 |
|---|---|---|
| Marca | Toyota | Ford |
| Modelo | Corolla | Transit |
| Categoría | COCHE | FURGONETA |
| Plazas | 5 | 3 |
| Capacidad de carga | 400 litros | 1000 kg |
| Transmisión | Manual | Automática |
| Estado operativo | disponible | no disponible |

Los identificadores se generan automáticamente mediante el modelo del vehículo.

Para la prueba de rendimiento se utiliza un catálogo independiente de 400 vehículos, de los cuales 200 están disponibles y 200 no disponibles.

## 5. Pruebas automatizadas de GC03-63

| Caso | Descripción | Resultado |
|---|---|---|
| PT-01 | Obtener todos los vehículos del catálogo | Correcto |
| PT-02 | Conservar los datos de los vehículos | Correcto |
| PT-03 | Incluir vehículos no disponibles y mostrar su estado | Correcto |
| PT-04 | Reflejar cambios de estado en consultas posteriores | Correcto |
| PT-05 | Rechazar un catálogo inválido | Correcto |
| PT-06 | Comprobar que la consulta no modifica los vehículos | Correcto |
| PT-07 | Verificar el rendimiento con 400 vehículos | Correcto |

### PT-01. Obtención de vehículos

Se realiza una consulta sobre un catálogo con dos vehículos registrados.

**Resultado esperado:** devolver los dos vehículos con sus identificadores correctos.

**Resultado obtenido:** correcto.

### PT-02. Conservación de datos

Se comprueba que el vehículo Toyota Corolla conserva su marca, modelo, categoría, plazas, capacidad de carga, transmisión y estado operativo.

**Resultado esperado:** todos los valores coinciden con los registrados.

**Resultado obtenido:** correcto.

### PT-03. Vehículos no disponibles

Se consulta un catálogo que contiene una furgoneta cuyo estado es `no disponible`.

**Resultado esperado:** la furgoneta sigue apareciendo en el catálogo completo y conserva su estado.

**Resultado obtenido:** correcto.

### PT-04. Actualización del estado operativo

Se modifica el estado del Toyota Corolla a `mantenimiento` y se realiza otra consulta.

**Resultado esperado:** la consulta devuelve el nuevo estado.

**Resultado obtenido:** correcto.

### PT-05. Catálogo inválido

Se intenta consultar utilizando `None` y una lista vacía en lugar de un objeto `CatalogoVehiculos`.

**Resultado esperado:** el servicio rechaza ambas entradas mediante `ValueError`.

**Resultado obtenido:** correcto.

### PT-06. Consulta sin modificaciones

Se consulta el catálogo en dos ocasiones y se comparan los resultados.

**Resultado esperado:** los datos almacenados no se modifican por realizar la consulta.

**Resultado obtenido:** correcto.

### PT-07. Rendimiento del catálogo

Se prepara un catálogo con 400 vehículos ficticios.

La mitad tienen estado `disponible` y la otra mitad `no disponible`.

Se mide el tiempo de ejecución de `obtener_vehiculos_catalogo()` mediante `perf_counter()`.

Se comprueba que:

- Se devuelven los 400 vehículos.
- Exactamente 200 presentan estado `disponible`.
- El tiempo de consulta es inferior a dos segundos.

**Resultado obtenido:** correcto.

## 6. Ejecución de las pruebas

### 6.1. Pruebas de GC03-63

Comando utilizado:

`python -m unittest discover -s tests -p "test_catalogo_rendimiento.py" -v`

Resultado:

```text
Ran 7 tests in 0.004s

OK
```

**Resumen:**

| Concepto | Resultado |
|---|---|
| Pruebas ejecutadas | 7 |
| Pruebas superadas | 7 |
| Fallos | 0 |
| Errores | 0 |
| Duración total del conjunto | 0,004 segundos |

### 6.2. Verificación de las pruebas existentes de GC03-21

También se ha ejecutado el archivo de pruebas desarrollado previamente por Andrea.

Comando utilizado:

`python -m unittest discover -s tests -p "test_gc03_21.py" -v`

Resultado:

```text
Ran 10 tests in 0.003s

OK
```

Estas pruebas adicionales verifican la presentación de datos, los estados operativos, el catálogo vacío, el acceso al menú administrativo y una comprobación local de rendimiento.

En total se han ejecutado 17 pruebas con resultado satisfactorio entre ambos archivos.

## 7. Limitaciones

Las pruebas se han realizado utilizando un catálogo almacenado en memoria y ejecutando directamente funciones Python.

La medición de rendimiento de GC03-63 corresponde únicamente a la ejecución local del servicio. No incluye conexiones con bases de datos, tráfico de red ni tiempos de renderizado de una interfaz web.

El tiempo de 0,004 segundos corresponde al conjunto de las siete pruebas, no exclusivamente a la consulta del catálogo grande.

Por tanto, se verifica el requisito temporal en los escenarios locales probados, pero no se garantiza ese mismo rendimiento en un entorno de producción.

## 8. Conclusión

Se han ejecutado siete pruebas automatizadas propias de GC03-63 y diez pruebas funcionales existentes de GC03-21, todas con resultado correcto.

Se ha comprobado que el catálogo devuelve los vehículos registrados, conserva sus datos, muestra correctamente los estados operativos y refleja sus modificaciones en consultas posteriores.

También se ha validado que el servicio rechaza entradas inválidas, que las operaciones de consulta no alteran los datos y que la consulta local de 400 vehículos cumple el límite de dos segundos establecido en la prueba.

Con estos resultados se consideran superadas las comprobaciones funcionales y de rendimiento realizadas para GC03-63, dentro del alcance y las limitaciones del entorno de pruebas utilizado.