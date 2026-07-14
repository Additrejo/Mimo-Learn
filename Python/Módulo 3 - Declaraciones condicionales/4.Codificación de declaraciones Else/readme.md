# Declaraciones Else

Este bloque introduce la declaracion `else`, que funciona como el plan de respaldo de una declaracion `if`: define que hacer cuando la condicion del `if` es `False`.

## Conceptos

### El operador not como alternativa

Antes de conocer `else`, es posible lograr un resultado similar combinando una declaracion `if` con una segunda declaracion `if not`, que ejecuta su bloque de codigo cuando la condicion original es `False`. Sin embargo, esto obliga a evaluar la condicion dos veces.

### Que es la declaracion else

`else` es una declaracion condicional que se ejecuta cuando la condicion de la declaracion `if` es `False`. El gran software no solo decide que hacer cuando una condicion es `True`, tambien tiene un plan de respaldo si la condicion es `False`, y ese plan de respaldo es el bloque `else`.

### La declaracion else no necesita su propia condicion

A diferencia de `if`, `else` no lleva una condicion propia, porque maneja automaticamente todos los casos en los que la condicion del `if` correspondiente es `False`.

### Posicion de la declaracion else

La declaracion `else` siempre va al final del bloque de codigo del `if`, nunca antes.

### else como respuesta predeterminada

El bloque de codigo de una declaracion `else` se ejecuta para todos los casos en los que la declaracion `if` devuelve `False`. Por eso se puede pensar en `else` como una respuesta predeterminada: cubre cualquier caso que el `if` no contempla.

### Reemplazar dos declaraciones if por if / else

En lugar de escribir una declaracion `if` seguida de una segunda declaracion `if not`, se puede usar una unica declaracion `if / else` para lograr el mismo resultado de forma mas clara y sin evaluar la condicion dos veces.

## Ejercicios

1. `ejercicio_01_disponibilidad-not.py` - Usar el operador `not` en una segunda declaracion `if` para manejar el caso contrario.
2. `ejercicio_02_disponibilidad-if-else.py` - Reemplazar dos declaraciones `if` por una sola declaracion `if / else`.
3. `ejercicio_03_luces-if-else.py` - Usar `else` para encender las luces cuando `is_day` es `False`.
4. `ejercicio_04_adivina-numero.py` - Codificar una declaracion `else` para un juego de adivinar numeros.
5. `ejercicio_05_sugerencias-amigos.py` - Agregar las palabras clave `if` y `else` en sus posiciones correctas.
6. `ejercicio_06_membresia-dataset-2.py` - Establecer un valor de variable para que se ejecute el bloque `else`.
7. `ejercicio_07_membresia-dataset-1.py` - Establecer un valor de variable para que se ejecute el bloque `if` en lugar del `else`.
