# Declaraciones Condicionales 1

Este bloque introduce los fundamentos de las declaraciones `if`: la palabra clave que las identifica, el tipo de valor que reciben como condicion, y como la indentacion determina que codigo pertenece al bloque condicional.

## Conceptos

### La palabra clave if

`if` es la palabra clave que decide si un bloque de codigo debe ejecutarse o no. Las declaraciones `if` tambien se llaman sentencias condicionales, porque dependen de una condicion para omitir o ejecutar su bloque de codigo.

### La condicion debe ser un valor booleano

La condicion de una declaracion `if` siempre es un valor booleano (`True` o `False`). Ese valor booleano puede venir directamente de una variable, de una comparacion, o del resultado de aplicar el operador `not`.

### Indentacion

Solo el codigo indentado dentro del bloque `if` depende de la condicion. El codigo que esta al mismo nivel que el `if` (sin indentacion adicional) se ejecuta siempre, sin importar si la condicion es `True` o `False`.

### Por que usar comparaciones o variables en lugar de True/False fijo

Usar comparaciones o variables como condicion es mejor que escribir `True` o `False` directamente, porque el valor de una variable puede cambiar. Esto permite que el mismo bloque `if` ejecute o salte su codigo dependiendo del valor actual de la variable.

### El operador not

El operador `not` invierte un valor booleano: `not True` da como resultado `False`, y viceversa. Este valor invertido tambien puede usarse como condicion de un `if`.

## Ejercicios

1. `ejercicio_01_paraguas-lluvia.py` - Ejecutar un bloque `if` basado en una variable booleana.
2. `ejercicio_02_cuenta-premium.py` - Codificar un operador para que la condicion sea `True`.
3. `ejercicio_03_personaje-mago.py` - Condicion con `!=` para un personaje de juego.
4. `ejercicio_04_modo-nocturno.py` - Crear una variable de condicion y usarla en un `if`.
5. `ejercicio_05_declaracion-if-false.py` - Codificar una declaracion `if` con condicion `False`.
6. `ejercicio_06_nivel-completado.py` - Variable de condicion para avanzar de nivel.
7. `ejercicio_07_hora-despertar.py` - Valor booleano para que el bloque de codigo se omita.
8. `ejercicio_08_cuenta-regresiva.py` - Variable como condicion para ejecutar una cuenta regresiva.
