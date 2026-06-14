# Comparando cadenas - Operador de igualdad

Modulo 2 - Tipos y Comparaciones

Se pueden usar comparaciones para verificar si una cadena es igual o no igual a otra cadena. Los operadores de comparacion devuelven un valor booleano: `True` o `False`.

---

## Operador de igualdad `==`

Para verificar si una cadena es igual a otra cadena, usamos el operador de igualdad `==`.

- Si la cadena de la izquierda es igual a la de la derecha, el resultado es `True`.
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

## Nota importante

El operador `==` (doble igual) verifica igualdad y es diferente al operador `=` (simple igual), que se usa para asignar valores a variables.

```python
nombre = "Ana"       # asignacion
"Ana" == "Ana"       # comparacion -> True
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
