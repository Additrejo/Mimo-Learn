# Módulo 3: Declaraciones condicionales

Este módulo introduce las declaraciones condicionales en Python, la base para que un programa tome decisiones y ejecute distintas líneas de código según se cumplan o no determinadas condiciones.

## Bloques de este módulo

### [1. Tomando decisiones](./modulo-03-tomando-decisiones/modulo-03-tomando-decisiones.md)

Introduce la declaración `if`, su sintaxis básica y el concepto de condición. Cubre cómo los valores booleanos `True` y `False` determinan si un bloque de código se ejecuta o se omite, y cómo se construye una declaración `if` completa: palabra clave `if`, condición y dos puntos `:`.

### [2. Bloques de código](./modulo-03-bloques-de-codigo/modulo-03-bloques-de-codigo.md)

Profundiza en el concepto de bloque de código: el conjunto de líneas indentadas que dependen de una condición. Cubre la indentación, los errores de indentación (`IndentationError`), el uso de variables como condición, y la diferencia entre el código que pertenece al bloque `if` y el código que se ejecuta siempre, independientemente de la condición.

## Conceptos clave del módulo

- La declaración `if` ejecuta un bloque de código solo si su condición se evalúa como verdadera.
- Las condiciones pueden ser valores booleanos directos (`True`, `False`) o variables que almacenan esos valores.
- Un bloque de código puede contener una o varias líneas, siempre que compartan la misma indentación.
- La indentación (normalmente de dos espacios) define qué líneas pertenecen a un bloque de código.
- Una indentación incorrecta produce un `IndentationError`.
- El código que no está indentado dentro de un bloque `if` se ejecuta siempre, sin depender de la condición.

## Estructura de archivos

```
modulo-03-tomando-decisiones/
  modulo-03-tomando-decisiones.md
  ejercicio_01_condicion-true.py
  ejercicio_02_condicion-false.py
  ejercicio_03_cuenta-regresiva.py
  ejercicio_04_mostrar-notificaciones.py
  ejercicio_05_mostrar-o-no-mostrar.py
  ejercicio_06_la-respuesta-es-42.py
  ejercicio_07_modo-avion.py
  ejercicio_08_agregado-a-playlist.py

modulo-03-bloques-de-codigo/
  modulo-03-bloques-de-codigo.md
  ejercicio_01_bloque-de-codigo.py
  ejercicio_02_bloque-multilinea.py
  ejercicio_03_indentacion-dos-espacios.py
  ejercicio_04_error-indentacion-inconsistente.py
  ejercicio_05_error-indentacion-inesperada.py
  ejercicio_06_lineas-ilimitadas.py
  ejercicio_07_variable-condicion-false.py
  ejercicio_08_variable-condicion-true.py
  ejercicio_09_inbox-full-false.py
  ejercicio_10_is-online-true.py
  ejercicio_11_codigo-fuera-del-bloque.py
  ejercicio_12_expandir-bloque-codigo.py
  ejercicio_13_paid-false.py
  ejercicio_14_alarm-time-true.py
```
