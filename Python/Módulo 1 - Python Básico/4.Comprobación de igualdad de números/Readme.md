# Modulo 01 - Comprobacion de igualdad de numeros

Curso: Python | Modulo: 1. Python Basico

---

## Descripcion

Este bloque cubre los operadores de comparacion numerica en Python. Al comparar dos valores, el resultado siempre es un booleano: `True` o `False`. Estos operadores son fundamentales para verificar condiciones dentro de un programa.

---

## Lecciones

### 1. Operador de igualdad

Archivo de referencia: `modulo-01-operador-de-igualdad.md`

El **operador de igualdad** `==` compara si dos valores son identicos. Devuelve `True` cuando son iguales y `False` cuando son diferentes. Es importante no confundirlo con `=`, que se usa para asignar valores.

```python
print(10 == 10)  # True
print(9 == 10)   # False

votes = 10
print(votes == 11)  # False
```

### 2. Operador de desigualdad

Archivo de referencia: `modulo-01-operador-de-desigualdad.md`

El **operador de desigualdad** `!=` verifica si dos valores son diferentes. Devuelve `True` cuando no son iguales y `False` cuando si lo son. El resultado de cualquier comparacion puede almacenarse en una variable.

```python
print(1 != 10)   # True
print(10 != 10)  # False

result = 7 != 10
print(result)  # True
```

---

## Resumen de operadores

| Operador | Nombre | Devuelve `True` cuando... |
|---|---|---|
| `==` | Operador de igualdad | Los valores son identicos |
| `!=` | Operador de desigualdad | Los valores son diferentes |

---

## Estructura de archivos

```
comprobacion-igualdad-numeros/
├── modulo-01-comprobacion-igualdad-numeros.md   (este archivo)
├── modulo-01-operador-de-igualdad.md
├── modulo-01-operador-de-desigualdad.md
├── operador-de-igualdad/
│   ├── ejercicio_01_igualdad_intro.py
│   ├── ejercicio_02_igualdad_true.py
│   ├── ejercicio_03_igualdad_false_9_10.py
│   ├── ejercicio_04_igualdad_false_10_11.py
│   ├── ejercicio_05_igualdad_false_99_100.py
│   ├── ejercicio_06_igualdad_true_100.py
│   ├── ejercicio_07_suma_y_comparacion.py
│   ├── ejercicio_08_igualdad_con_variable.py
│   ├── ejercicio_09_igualdad_false_10_13.py
│   └── ejercicio_10_comparacion_pin.py
└── operador-de-desigualdad/
    ├── ejercicio_01_desigualdad_true.py
    ├── ejercicio_02_desigualdad_false.py
    ├── ejercicio_03_resultado_desigualdad.py
    ├── ejercicio_04_resultado_igualdad.py
    ├── ejercicio_05_igualdad_y_desigualdad.py
    ├── ejercicio_06_desigualdad_variable.py
    ├── ejercicio_07_comparacion_vote_count.py
    ├── ejercicio_08_comparacion_orders.py
    ├── ejercicio_09_desigualdad_letters.py
    ├── ejercicio_10_igualdad_answer.py
    ├── ejercicio_11_error_operador.py
    └── ejercicio_12_igualdad_variables.py
```
