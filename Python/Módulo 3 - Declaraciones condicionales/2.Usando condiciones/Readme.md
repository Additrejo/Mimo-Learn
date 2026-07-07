# Usando condiciones

Este bloque profundiza en el uso de operadores de comparacion como condiciones dentro de declaraciones `if`, y en como almacenar el resultado de una comparacion en una variable para reutilizarlo.

## Conceptos

### Operadores de comparacion como condiciones

Las declaraciones `if` funcionan con todos los operadores de comparacion: `==`, `!=`, `>`, `<`, `>=` y `<=`. El operador elegido depende de la decision que se quiera tomar:

- `==` verifica si dos valores son iguales.
- `!=` verifica si dos valores son diferentes.
- `>=` y `<=` verifican si un valor es mayor o igual, o menor o igual, que otro.

Usamos comparaciones junto a declaraciones `if` para tomar decisiones mas inteligentes sobre ejecutar u omitir codigo, en lugar de que el bloque se ejecute siempre.

### Tipos de datos comparables

Con `==` se pueden comparar enteros, flotantes, cadenas y valores booleanos.

### Comparar variables booleanas

Una variable booleana puede compararse directamente con `True` o `False` usando `==`, por ejemplo `is_day == True`.

### Almacenar comparaciones en variables

El resultado de una comparacion se puede guardar en una variable (por ejemplo `pass_grade = score > 50` o `show_alert = inbox_full == True`). Esto evita reescribir la misma comparacion varias veces: la variable, que contiene un valor booleano, puede usarse directamente como condicion en un `if`.

## Ejercicios

1. `ejercicio_01_trivia-comparacion-igualdad.py` - Verificar una respuesta con `==`.
2. `ejercicio_02_trivia-comparacion-desigualdad.py` - Verificar una respuesta incorrecta con `!=`.
3. `ejercicio_03_descuento-mayor-igual.py` - Aplicar un descuento segun la edad usando `>=`.
4. `ejercicio_04_comparacion-booleana.py` - Comparar una variable booleana con `==`.
5. `ejercicio_05_variable-comparacion-nota.py` - Guardar una comparacion en una variable y usarla en un `if`.
6. `ejercicio_06_edad-conducir.py` - Verificar si la edad permite conducir con `>=`.
7. `ejercicio_07_alarma-dia-semana.py` - Configurar una alarma segun el dia con `!=`.
8. `ejercicio_08_restaurante-vegetariano.py` - Practica: sugerir un restaurante segun la dieta.
9. `ejercicio_09_reproducciones-cancion.py` - Practica: mostrar la cancion mas escuchada con `>=`.
10. `ejercicio_10_alerta-bandeja-entrada.py` - Practica: almacenar una comparacion booleana en una variable de alerta.
