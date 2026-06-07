# Modulo 01 - Comprobacion de igualdad de numeros: Operador de igualdad

Curso: Python | Modulo: 1. Python Basico

---

## Conceptos cubiertos

### El operador de igualdad `==`

Para comparar si dos numeros son iguales, se usa el **operador de igualdad** `==`. A diferencia del signo `=`, que asigna un valor a una variable, el operador `==` compara dos valores y devuelve un resultado booleano.

Al comparar, solo hay dos resultados posibles: `True` o `False`.

```python
5 == 5   # True
9 == 10  # False
```

### Comparacion de numeros iguales

Cuando se comparan dos numeros identicos con `==`, el resultado es `True`.

```python
print(10 == 10)  # True
```

### Comparacion de numeros diferentes

Cuando los numeros comparados son distintos, el resultado es `False`.

```python
print(9 == 10)  # False
```

### Uso con variables

El operador `==` puede aplicarse sobre variables que almacenan numeros. Esto permite verificar si el valor almacenado en una variable coincide con un numero especifico.

```python
votes = 10
print(votes == 11)  # False
```

Un caso de uso practico es verificar si el PIN ingresado por un usuario coincide con el PIN guardado:

```python
entered_pin = 5448
expected_pin = 5440
print(entered_pin == expected_pin)  # False
```

### Diferencia entre `=` y `==`

| Operador | Uso | Ejemplo |
|---|---|---|
| `=` | Asignacion de valor | `x = 5` |
| `==` | Comparacion de igualdad | `x == 5` |

---

## Ejercicios

| Archivo | Descripcion |
|---|---|
| `ejercicio_01_igualdad_intro.py` | Introduce el operador `==` comparando dos numeros iguales |
| `ejercicio_02_igualdad_true.py` | Imprime la comparacion de dos numeros iguales: resultado `True` |
| `ejercicio_03_igualdad_false_9_10.py` | Compara numeros diferentes: `9 == 10`, resultado `False` |
| `ejercicio_04_igualdad_false_10_11.py` | Compara numeros diferentes: `10 == 11`, resultado `False` |
| `ejercicio_05_igualdad_false_99_100.py` | Agrega el operador de igualdad entre `99` y `100` |
| `ejercicio_06_igualdad_true_100.py` | Comprueba si `100 == 100`, resultado `True` |
| `ejercicio_07_suma_y_comparacion.py` | Combina una suma y una comparacion con `==` en dos sentencias `print` |
| `ejercicio_08_igualdad_con_variable.py` | Verifica si el valor de una variable es igual a un numero dado |
| `ejercicio_09_igualdad_false_10_13.py` | Muestra `False` comparando `10 == 13` |
| `ejercicio_10_comparacion_pin.py` | Ejemplo conceptual: compara dos variables numericas representando PINs |
