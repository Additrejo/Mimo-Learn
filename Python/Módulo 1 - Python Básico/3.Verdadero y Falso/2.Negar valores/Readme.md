# Modulo 01 - Negar valores

Curso: Python | Modulo: 1. Python Basico

---

## Conceptos cubiertos

### El operador de negacion `not`

El operador `not` es el **operador de negacion** en Python. Se coloca delante de un valor booleano (`True` o `False`) y lo convierte en su opuesto.

- `not True` resulta en `False`
- `not False` resulta en `True`

```python
print(not True)   # False
print(not False)  # True
```

### Uso de `not` con variables

El operador `not` puede aplicarse directamente sobre variables que almacenan valores booleanos. Al imprimir `not variable`, se muestra el valor negado de lo que contiene la variable.

```python
available = True
print(not available)  # False
```

### Almacenar una negacion en una variable

Es posible guardar el resultado de una negacion en una nueva variable. Esto permite reutilizar el valor negado en otras partes del programa.

```python
morning = True
is_evening = not morning
print(is_evening)  # False
```

---

## Ejercicios

| Archivo | Descripcion |
|---|---|
| `ejercicio_01_not_true.py` | Imprime el resultado de `not True` directamente |
| `ejercicio_02_not_false.py` | Imprime el resultado de `not False` directamente |
| `ejercicio_03_not_variable.py` | Aplica `not` sobre una variable booleana al imprimir |
| `ejercicio_04_not_en_variable.py` | Guarda la negacion de una variable en otra variable |
| `ejercicio_05_not_true_en_variable.py` | Almacena `not True` en una variable y la imprime |
| `ejercicio_06_result_not_true.py` | Determina el valor almacenado por `result = not True` |
| `ejercicio_07_allow_duplicates.py` | Usa el operador de negacion para asignar un valor a una variable |
| `ejercicio_08_not_available.py` | Crea una variable con el valor negado de otra variable booleana |
