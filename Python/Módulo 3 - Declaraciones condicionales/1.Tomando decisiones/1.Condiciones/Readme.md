# Tomando decisiones

Bloque introductorio del Módulo 3: Declaraciones condicionales.

## Conceptos cubiertos

### La declaración `if`

La declaración `if` ejecuta un bloque de código solo si una condición se evalúa como verdadera. Se interpreta como "si algo es verdadero, entonces haz esto".

```python
if True:
    print("Hello!")
```

### Condiciones y condicionales

Valores como `True` se llaman **condiciones**. Las declaraciones que dependen de condiciones se llaman **condicionales**. Las condiciones se encuentran entre la palabra clave `if` y los dos puntos `:`.

```python
if True:
    print("Hello")
```

### Omitir código con `False`

Si la condición se evalúa como falsa, el bloque de código se omite y no se ejecuta nada.

```python
if False:
    print("Hello!")
# No se imprime nada
```

### Estructura de la declaración `if`

Una declaración `if` se compone de:

- La palabra clave `if`
- Una condición (por ejemplo, `True` o `False`)
- Dos puntos `:`
- Un bloque de código indentado que se ejecuta u omite según la condición

```python
if True:
    print("Show notifications")
```

## Resumen

Los programas usan valores booleanos para decidir si ejecutar u omitir líneas de código. Esta es la base de la toma de decisiones en programación: la declaración `if` permite que un programa responda de forma diferente según las condiciones que se evalúan.
