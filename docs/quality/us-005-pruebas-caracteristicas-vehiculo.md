# US-005 — Pruebas de características de vehículos

## 1. Identificación

- **Historia de usuario:** GC03-60 — US-005: Consultar las características de un vehículo.
- **Subtarea:** GC03-65 — Pruebas funcionales deterministas y verificación de tiempos de respuesta.
- **Responsable:** Borja Gómez Castaño.
- **Fecha de ejecución:** 05/11/2026.
- **Estimación:** 2 horas.
- **Estado:** Pruebas locales completadas; integración con el catálogo pendiente de verificación.

## 2. Objetivo

Comprobar que la función de presentación de características de vehículos muestra correctamente los atributos correspondientes a cada vehículo y que su tiempo de respuesta es inferior a dos segundos en el entorno local.

Para ello se han utilizado datos sintéticos y pruebas automatizadas que permiten comparar los resultados obtenidos con los valores esperados.

## 3. Entorno y componentes utilizados

Las pruebas se han realizado en el entorno local de desarrollo mediante Python.

Archivos utilizados:

- `detalle_vehiculo.py`
- `tests/test_detalle_vehiculo.py`

La implementación utiliza la clase `VehiculoDetalle` y la función `mostrar_detalle_vehiculo()`.

Los atributos comprobados son:

- Identificador.
- Marca.
- Modelo.
- Categoría.
- Número de plazas.
- Capacidad de maletero o carga.
- Transmisión.
- Estado operativo.

## 4. Datos utilizados en las pruebas automatizadas

Se ha preparado un catálogo sintético en memoria con los siguientes vehículos:

| Campo | V-001 | V-002 |
|---|---|---|
| Identificador | V-001 | V-002 |
| Marca | Toyota | Ford |
| Modelo | Corolla | Transit |
| Categoría | Turismo | Furgoneta |
| Plazas | 5 | 3 |
| Maletero/carga | 471 litros | 8 m3 |
| Transmisión | Automática | Manual |
| Estado operativo | Disponible | Disponible |

La selección se simula accediendo al objeto correspondiente mediante su identificador dentro de un diccionario de datos de prueba.

Estos datos son independientes de los empleados en las comprobaciones manuales anteriores.

## 5. Pruebas automatizadas realizadas

### PT-01. Datos del vehículo seleccionado

Se selecciona el vehículo `V-001` del catálogo sintético y se genera su ficha mediante `mostrar_detalle_vehiculo()`.

Se comprueba mediante aserciones que aparecen correctamente el identificador, marca, modelo, categoría, plazas, capacidad de maletero, transmisión y estado operativo.

**Resultado: CORRECTO.**

### PT-02. Coincidencia exacta de los datos

Se genera la ficha del vehículo `V-001` y se compara la cadena completa devuelta por la función con el texto esperado.

La prueba utiliza `assertEqual()` para comprobar que todos los campos y valores coinciden exactamente.

**Resultado: CORRECTO.**

### PT-03. Correspondencia entre vehículos diferentes

Se generan las fichas de `V-001` y `V-002`.

Se comprueba que la ficha de Toyota Corolla contiene los datos de ese vehículo y no los de Ford Transit, y viceversa.

**Resultado: CORRECTO.**

### PT-04. Tiempo de respuesta

Se mide el tiempo de ejecución de `mostrar_detalle_vehiculo()` mediante `perf_counter()`.

**Resultado obtenido:**

```text
Tiempo de respuesta local: 0.000001 segundos
```

Se verifica mediante una aserción que el tiempo medido es inferior a dos segundos.

**Resultado: CORRECTO.**

Esta medición corresponde únicamente a la generación de la ficha en memoria.

## 6. Ejecución de las pruebas automatizadas

Comando ejecutado:

```powershell
python -m unittest discover -s tests -p "test_detalle_vehiculo.py" -v
```

Salida obtenida:

```text
test_datos_exactos ... ok
test_datos_vehiculo_seleccionado ... ok
test_tiempo_respuesta ... ok
test_vehiculos_diferentes ... ok

Ran 4 tests in 0.001s

OK
```

**Resultados:**

- Pruebas automatizadas: 4.
- Pruebas superadas: 4.
- Fallos: 0.
- Errores: 0.
- Duración total de ejecución de las pruebas: 0,001 segundos.

## 7. Comprobaciones manuales anteriores

Antes de preparar las pruebas automatizadas se realizaron tres comprobaciones directas sobre `mostrar_detalle_vehiculo()`.

### PM-01. Presentación de Toyota Corolla

Se verificó que la función mostraba los ocho atributos de un vehículo Toyota Corolla de prueba, con identificador `VEH-01` y capacidad de maletero de 470 litros.

**Resultado: CORRECTO.**

### PM-02. Presentación de Ford Transit

Se verificó la presentación de un vehículo Ford Transit de prueba, con identificador `VEH-02`, transmisión manual y estado operativo de mantenimiento.

Se comprobaron mediante aserciones varios atributos y se revisó la salida generada.

**Resultado: CORRECTO.**

### PM-03. Medición inicial de tiempo

Se realizó una medición previa del tiempo empleado por la función para generar una ficha.

**Tiempo registrado:** 0,000003 segundos.

**Resultado: CORRECTO.**

## 8. Resumen de resultados

| Comprobación | Resultado |
|---|---|
| Datos correspondientes al vehículo seleccionado del catálogo sintético | Correcto |
| Coincidencia exacta de los atributos | Correcto |
| Independencia entre fichas de vehículos | Correcto |
| Tiempo de generación de ficha inferior a 2 segundos | Correcto |
| Tres comprobaciones manuales previas | Correcto |
| Selección desde el catálogo real de CityDrive | Pendiente de integración |
| Tiempo de consulta completa desde la interfaz | Pendiente de integración |

## 9. Limitaciones

La implementación actual de `detalle_vehiculo.py` permite generar la ficha de un objeto `VehiculoDetalle`, pero no implementa por sí misma la búsqueda o selección del vehículo desde el catálogo real.

En las pruebas automatizadas se ha utilizado un diccionario de vehículos sintéticos para simular esa selección.

Asimismo, la medición de rendimiento corresponde a la ejecución de la función de presentación y no incluye recuperación de datos, navegación ni representación mediante una interfaz gráfica.

Por tanto, las pruebas realizadas verifican el comportamiento local del componente, pero no constituyen una prueba completa de integración del sistema.

## 10. Conclusión

Se han ejecutado cuatro pruebas automatizadas, todas con resultado correcto, además de tres comprobaciones manuales anteriores también satisfactorias.

Las pruebas confirman que la función genera fichas con los atributos esperados, distingue correctamente vehículos diferentes y presenta un tiempo de ejecución inferior a dos segundos en el entorno local.

Queda documentada la necesidad de verificar posteriormente la integración con la selección de vehículos desde el catálogo y la medición del flujo completo de consulta.

Con los resultados obtenidos queda comprobado el comportamiento local de presentación de características contemplado en GC03-65.