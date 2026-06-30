# Modulo 2: Tipos y Comparaciones

Curso Python - Mimo

Este modulo cubre los operadores de comparacion para numeros y cadenas, los tipos de datos basicos en Python y la conversion entre ellos.

---

## Bloques del modulo

### 1. Comparando numeros

Los operadores de comparacion permiten verificar la relacion entre dos numeros. Siempre devuelven `True` o `False`.

| Operador | Nombre | Ejemplo | Resultado |
|---|---|---|---|
| `<` | Menor que | `1 < 235` | `True` |
| `>` | Mayor que | `101 > 90` | `True` |
| `<=` | Menor o igual que | `11 <= 11` | `True` |
| `>=` | Mayor o igual que | `3099 >= 3099` | `True` |

El resultado de una comparacion se puede almacenar en una variable y se pueden comparar variables entre si:

```python
min = 5
max = 10
result = min <= max
print(result)  # True
```

Carpeta: `modulo-02-comparando-numeros/`

---

### 2. Comparando cadenas

Los mismos operadores de igualdad y desigualdad funcionan con cadenas de texto.

| Operador | Nombre | Ejemplo | Resultado |
|---|---|---|---|
| `==` | Igualdad | `"apple" == "apple"` | `True` |
| `!=` | Desigualdad | `"subscribed" != "rejected"` | `True` |

```python
fruit_1 = "apple"
fruit_2 = "orange"
print(fruit_1 == fruit_2)   # False

previous_leader = "Anna"
new_leader = "Jim"
leader_changed = previous_leader != new_leader
```

Carpeta: `modulo-02-comparando-cadenas/`

---

### 3. Descubriendo tipos

En programacion, los valores como numeros, cadenas y booleanos se llaman tipos. Python tiene cuatro tipos basicos:

| Tipo | Nombre | Ejemplo |
|---|---|---|
| `int` | Entero | `score = 42` |
| `str` | Cadena | `name = "Jill"` |
| `bool` | Booleano | `is_active = True` |
| `float` | Flotante | `pi = 3.14159` |

Python tiene funciones integradas para trabajar con tipos:

| Funcion | Descripcion | Ejemplo |
|---|---|---|
| `type()` | Devuelve el tipo de una variable | `type(42)` -> `<class 'int'>` |
| `int()` | Convierte a entero | `int("17")` -> `17` |
| `float()` | Convierte a flotante | `float(12)` -> `12.0` |
| `str()` | Convierte a cadena | `str(980790)` -> `"980790"` |
| `bool()` | Convierte a booleano | `bool("Sam")` -> `True` |

Notas importantes sobre conversion:
- `int()` en un float trunca sin redondear: `int(9.99)` -> `9`
- `int(True)` -> `1`, `int(False)` -> `0`
- `bool()` devuelve `False` si el valor esta vacio o es `0`

Carpeta: `modulo-02-descubriendo-tipos/`

---

### 4. Practica adicional

Dos rondas de ejercicios que repasan todos los temas del modulo.

Carpeta: `modulo-02-practica/`

---

## Estructura de carpetas

```
modulo-02-comparando-numeros/
modulo-02-comparando-cadenas/
modulo-02-descubriendo-tipos/
modulo-02-practica/
```
