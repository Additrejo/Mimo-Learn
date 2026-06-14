# Comparando numeros

Modulo 2 - Tipos y Comparaciones

Se pueden usar comparaciones para verificar si un numero es menor o mayor que otro numero. Los operadores de comparacion devuelven un valor booleano: `True` o `False`.

---

## Operador menor que `<`

Para verificar si un numero es menor que otro, se usa el operador `<`.

El numero de la izquierda se compara contra el numero de la derecha:

- Si el numero de la izquierda es menor, el resultado es `True`.
- Si el numero de la izquierda no es menor, el resultado es `False`.

```python
print(1 < 235)   # True
print(235 < 1)   # False
```

---

## Operador mayor que `>`

Para verificar si un numero es mayor que otro, se usa el operador `>`.

- Si el numero de la izquierda es mayor, el resultado es `True`.
- Si el numero de la izquierda no es estrictamente mayor (incluyendo cuando son iguales), el resultado es `False`.

```python
print(101 > 90)  # True
print(1 > 1)     # False
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
