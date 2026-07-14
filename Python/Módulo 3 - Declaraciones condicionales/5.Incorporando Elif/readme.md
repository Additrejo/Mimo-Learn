# Elif

Este bloque introduce la declaracion `elif`, que permite verificar una segunda condicion (o mas) cuando la condicion de la declaracion `if` es `False`.

## Conceptos

### Que significa elif

`elif` significa "else if". Se utiliza cuando hay una segunda condicion que debe verificarse unicamente cuando la condicion del bloque `if` no se cumple.

### Cuando se ejecuta el bloque de una declaracion elif

La declaracion `elif` ejecuta su bloque de codigo si las condiciones anteriores (`if` y cualquier `elif` previo) fueron `False` y su propia condicion es `True`.

### Multiples declaraciones elif

Siempre que vayan antes de la declaracion `else`, se pueden agregar tantas declaraciones `elif` como se necesiten. No hay un numero maximo de declaraciones `elif` que se puedan agregar a una declaracion `if`.

### La declaracion else junto con elif

Tambien se puede codificar una declaracion `else` al final de la cadena de `if` / `elif`, para ejecutar su bloque de codigo cuando todas las condiciones anteriores (`if` y `elif`) son `False`.

### Orden de evaluacion

Python evalua las condiciones en orden: primero la del `if`, luego la de cada `elif` en el orden en que aparecen. En cuanto una condicion es `True`, se ejecuta su bloque y se omiten el resto de las declaraciones `elif` y `else` de esa cadena.

## Ejercicios

1. `ejercicio_01_saludo-tarde.py` - Codificar una declaracion `elif` para mostrar un saludo de tarde.
2. `ejercicio_02_saludo-noche.py` - Codificar una declaracion `else` para mostrar un saludo de noche.
3. `ejercicio_03_edad-atraccion.py` - Codificar una declaracion `elif` para verificar un rango de edad.
4. `ejercicio_04_pedido-pizza.py` - Codificar las palabras clave de una declaracion `elif` para un pedido.
5. `ejercicio_05_pedido-no-reconocido.py` - Codificar una declaracion `else` para un caso no contemplado.
6. `ejercicio_06_segunda-elif-bienvenida.py` - Codificar una segunda declaracion `elif` en la misma cadena condicional.
