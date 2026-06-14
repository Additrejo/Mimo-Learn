# Comparando cadenas - Operador de igualdad y desigualdad

Modulo 2 - Tipos y Comparaciones

Se pueden usar comparaciones para verificar si una cadena es igual o no igual a otra cadena. Los operadores de comparacion devuelven un valor booleano: `True` o `False`.

---

## Operador de igualdad `==`

Para verificar si una cadena es igual a otra cadena, usamos el operador de igualdad `==`.

- Si ambas cadenas son iguales, el resultado es `True`.
- Si las cadenas son diferentes, el resultado es `False`.

```python
print("apple" == "apple")   # True
print("apple" == "orange")  # False
```

El operador `==` tambien funciona con variables que almacenan cadenas:

```python
fruit_1 = "apple"
fruit_2 = "orange"
print(fruit_1 == fruit_2)   # False
```

El resultado de la comparacion se puede almacenar en una variable:

```python
item_1 = "deerstalker hat"
item_2 = "pipe"
is_duplicate = item_1 == item_2
```

---

## Operador de desigualdad `!=`

Para verificar si una cadena no es igual a otra cadena, usamos el operador de desigualdad `!=`.

- Si las cadenas son diferentes, el resultado es `True`.
- Si las cadenas son iguales, el resultado es `False`.

```python
print("subscribed" != "rejected")    # True
print("subscribed" != "subscribed")  # False
```

El resultado tambien se puede almacenar en una variable y se pueden comparar variables entre si:

```python
same = "subscribed" != "subscribed"
print(same)  # False

previous_leader = "Anna"
new_leader = "Jim"
leader_changed = previous_leader != new_leader
```

---

## Nota importante

El operador `==` (doble igual) verifica igualdad. El operador `!=` verifica desigualdad. Ambos son distintos al operador `=` (simple igual), que se usa para asignar valores a variables.

```python
nombre = "Ana"        # asignacion
"Ana" == "Ana"        # comparacion de igualdad   -> True
"Ana" != "Maria"      # comparacion de desigualdad -> True
```

---

## Ejercicios

| Archivo | Descripcion |
|---|---|
| ejercicio_01_igualdad_true.py | Operador `==` con cadenas iguales, resultado True |
| ejercicio_02_igualdad_false.py | Operador `==` con cadenas diferentes, resultado False |
| ejercicio_03_comparar_variables.py | Comparar variables que almacenan cadenas |
| ejercicio_04_igualdad_y_desigualdad.py | Uso de `==` y `!=` en la misma ejecucion |
| ejercicio_05_practica_led.py | Practica: "LED+" == "LED" |
| ejercicio_06_practica_my_answer.py | Practica: almacenar cadena para resultado False |
| ejercicio_07_practica_act_ace.py | Practica: verificar si my_answer == solution |
| ejercicio_08_practica_liquid_solid.py | Practica: "liquid" == "solid" |
| ejercicio_09_practica_is_duplicate.py | Practica: almacenar resultado en is_duplicate |
| ejercicio_10_desigualdad_true.py | Operador `!=` con cadenas diferentes, resultado True |
| ejercicio_11_desigualdad_false.py | Operador `!=` con cadenas iguales, resultado False |
| ejercicio_12_resultado_en_variable.py | Almacenar resultado de `!=` en variable |
| ejercicio_13_practica_orange_yellow.py | Practica: "orange" != "yellow" |
| ejercicio_14_practica_my_answer.py | Practica: my_answer != solution |
| ejercicio_15_practica_wallpaper.py | Practica: wallpaper != "bliss.png" |
| ejercicio_16_practica_leader.py | Practica: previous_leader != new_leader |
| ejercicio_17_practica_cities.py | Practica: big_city != small_city |
