# Modulo 01 - Comprobacion de igualdad de numeros: Operador de desigualdad

Curso: Python | Modulo: 1. Python Basico

---

## Conceptos cubiertos

### El operador de desigualdad `!=`

Para verificar si un numero no es igual a otro, se usa el **operador de desigualdad** `!=`. Devuelve `True` cuando los valores son diferentes y `False` cuando son iguales.

```python
print(1 != 10)   # True
print(10 != 10)  # False
```

### Almacenar el resultado de una comparacion en una variable

El resultado de cualquier comparacion, tanto con `==` como con `!=`, puede guardarse directamente en una variable. La variable almacenara el valor booleano resultante.

```python
result = 1 != 2
print(result)  # True

result = 1 == 2
print(result)  # False
```

### Comparar variables entre si

Es posible comparar variables con otras variables usando `==` o `!=`. Ambos operadores pueden usarse sobre los mismos valores para obtener resultados opuestos.

```python
one = 1
two = 2
print(one == two)  # False
print(one != two)  # True
```

### Almacenar comparaciones con variables

La comparacion puede almacenarse en una nueva variable, que recibe el valor booleano de la expresion evaluada.

```python
vote_count = 99
target = vote_count == 100
print(target)  # False

orders = 1000
capacity = orders == 1000
print(capacity)  # True
```

### Error comun: operador incompleto

El operador de desigualdad es `!=`. Escribir solo `!` sin el `=` produce un error de sintaxis.

```python
# Incorrecto:
print(score_one ! score_two)

# Correcto:
print(score_one != score_two)
```

---

## Ejercicios

| Archivo | Descripcion |
|---|---|
| `ejercicio_01_desigualdad_true.py` | Introduce `!=`: compara `1` y `10`, resultado `True` |
| `ejercicio_02_desigualdad_false.py` | Compara numeros iguales con `!=`: resultado `False` |
| `ejercicio_03_resultado_desigualdad.py` | Almacena `1 != 2` en una variable e imprime el resultado |
| `ejercicio_04_resultado_igualdad.py` | Almacena `1 == 2` en una variable e imprime el resultado |
| `ejercicio_05_igualdad_y_desigualdad.py` | Compara dos variables con `==` y `!=` en sentencias separadas |
| `ejercicio_06_desigualdad_variable.py` | Almacena `7 != 10` en una variable y determina el output |
| `ejercicio_07_comparacion_vote_count.py` | Almacena la comparacion `vote_count == 100` en una variable |
| `ejercicio_08_comparacion_orders.py` | Almacena la comparacion `orders == 1000` en una variable |
| `ejercicio_09_desigualdad_letters.py` | Verifica si `letters` no es igual a `0` usando `!=` |
| `ejercicio_10_igualdad_answer.py` | Verifica si `answer` es igual a `13` y almacena el resultado |
| `ejercicio_11_error_operador.py` | Identifica y corrige un operador de desigualdad incorrecto |
| `ejercicio_12_igualdad_variables.py` | Comprueba si `level` es igual a `highest_level` usando `==` |
