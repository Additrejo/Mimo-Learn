# Comparando numeros

Modulo 2 - Tipos y Comparaciones

Se pueden usar comparaciones para verificar si un numero es menor, mayor, menor o igual, o mayor o igual que otro numero. Los operadores de comparacion devuelven un valor booleano: `True` o `False`.

---

## Operador menor que `<`

Para verificar si un numero es menor que otro, se usa el operador `<`.

- Si el numero de la izquierda es menor, el resultado es `True`.
- Si no es menor, el resultado es `False`.

```python
print(1 < 235)   # True
print(235 < 1)   # False
```

---

## Operador mayor que `>`

Para verificar si un numero es mayor que otro, se usa el operador `>`.

- Si el numero de la izquierda es mayor, el resultado es `True`.
- Si no es estrictamente mayor (incluyendo cuando son iguales), el resultado es `False`.

```python
print(101 > 90)  # True
print(1 > 1)     # False
```

---

## Operador menor o igual que `<=`

Para verificar si un numero es menor o igual a otro, se usa el operador `<=`.

- Si el numero de la izquierda es menor o igual, el resultado es `True`.
- El resultado tambien es `True` cuando ambos numeros son iguales.

```python
print(1 <= 3)    # True
print(11 <= 11)  # True
```

El resultado de una comparacion se puede almacenar en una variable usando `=`. Tambien se pueden comparar variables entre si:

```python
result = 1 <= 15
print(result)  # True

min = 5
max = 10
result = min <= max
print(result)  # True
```

---

## Operador mayor o igual que `>=`

Para verificar si un numero es mayor o igual a otro, se usa el operador `>=`.

- Si el numero de la izquierda es mayor o igual, el resultado es `True`.
- El resultado tambien es `True` cuando ambos numeros son iguales.

```python
print(3099 >= 3099)  # True
print(10 >= 10)      # True
```

---

## Ejercicios

| Archivo | Descripcion |
|---|---|
| ejercicio_01_menor_que.py | Operador `<`, resultado True |
| ejercicio_02_menor_que_false.py | Operador `<`, resultado False |
| ejercicio_03_mayor_que.py | Operador `>`, resultado True |
| ejercicio_04_mayor_que_igual.py | Operador `>` con numeros iguales, resultado False |
| ejercicio_05_practica_menor.py | Practica: 30 < 40 |
| ejercicio_06_practica_mayor.py | Practica: 5 > 4 |
| ejercicio_07_practica_true.py | Practica: mostrar True con `>` |
| ejercicio_08_practica_false.py | Practica: mostrar False con `>` |
| ejercicio_09_menor_o_igual.py | Operador `<=`, resultado True |
| ejercicio_10_menor_o_igual_iguales.py | Operador `<=` con numeros iguales, resultado True |
| ejercicio_11_resultado_en_variable.py | Almacenar resultado de `<=` en variable |
| ejercicio_12_comparar_variables.py | Comparar variables entre si con `<=` |
| ejercicio_13_mayor_o_igual.py | Operador `>=`, resultado True |
| ejercicio_14_mayor_o_igual_iguales.py | Operador `>=` con numeros iguales, resultado True |
| ejercicio_15_practica_battery.py | Practica: battery_level <= 20 |
| ejercicio_16_practica_points.py | Practica: points >= 10 almacenado en variable |
| ejercicio_17_practica_solved.py | Practica: solved <= minimum |
| ejercicio_18_practica_mayor_igual.py | Practica: 60 >= 50 |
