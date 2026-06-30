# Bloques de código

Segundo bloque del Módulo 3: Declaraciones condicionales.

## Conceptos cubiertos

### Qué es un bloque de código

Las sentencias `if` no deciden si omitir o ejecutar el código completo de un programa. Solo toman decisiones sobre un **bloque de código**: el conjunto de líneas indentadas que siguen a la declaración `if`.

```python
if True:
    print("I'm a code block!")
```

### Bloques de varias líneas

Un bloque de código puede contener más de una línea. Todas las líneas que comparten la misma indentación pertenecen al mismo bloque de código y se ejecutan u omiten juntas.

```python
if True:
    print("Look at me!")
    print("I'm a code block")
```

No existe un número máximo de líneas que pueda tener un bloque de código: puede tener tantas como se necesiten.

### Indentación

La indentación es el espacio entre el código y el margen del editor. Se usa una indentación de dos espacios para resaltar qué líneas pertenecen a un bloque de código.

```python
if True:
    print("I'm two spaces away!")
```

### Errores de indentación

Si la indentación es incorrecta, la computadora no puede interpretar el código y se produce un `IndentationError`.

- Cuando una línea dentro del mismo bloque tiene menos indentación de la esperada, aparece `unindent does not match any outer indentation level`.
- Cuando una línea tiene más indentación de la esperada sin que corresponda a un nuevo bloque, aparece `unexpected indent`.

### Variables como condición

En lugar de usar directamente los valores booleanos `True` o `False`, se pueden guardar en una variable y usar esa variable como la condición de la declaración `if`.

```python
greet = True
if greet:
    print("Hello!")
```

Si la variable se establece en `False`, el bloque de código se omite.

```python
greet = False
if greet:
    print("Hello!")
# No se imprime nada
```

### Código fuera del bloque if

El código que no está indentado dentro de un bloque `if` no depende de la condición y se ejecuta siempre, sin importar si la condición es verdadera o falsa.

```python
if False:
    print("Loading...")

print("Done!")
# Output:
# Done!
```

## Resumen

Un bloque de código es el conjunto de líneas indentadas que dependen de una condición. La indentación, generalmente de dos espacios, determina qué líneas pertenecen a ese bloque. Las condiciones pueden ser valores booleanos directos o variables que almacenan esos valores, y solo el código dentro del bloque se ve afectado por la decisión de la declaración `if`.
