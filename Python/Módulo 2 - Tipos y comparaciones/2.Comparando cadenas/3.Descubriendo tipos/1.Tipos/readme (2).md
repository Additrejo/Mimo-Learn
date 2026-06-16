# Descubriendo tipos

Modulo 2 - Tipos y Comparaciones

Este bloque cubre los tipos de datos basicos en Python, como verificar el tipo de una variable y como convertir entre tipos.

---

## Leccion 1: Tipos

En programacion, los valores como numeros, cadenas y booleanos se llaman tipos. Cada variable almacena un tipo de dato especifico.

### Entero (int)

Los enteros representan numeros enteros sin decimales.

```python
score = 42
minutes_left = 10
```

### Cadena (str)

Las cadenas son caracteres entre comillas `" "`. Se reconocen por las comillas que las rodean.

```python
sugar_content = "High"
name = "Jill"
```

### Booleano (bool)

El tipo boolean representa solo dos valores: `True` y `False`. Cuando almacenamos un valor en una variable, decimos que asignamos un valor.

```python
received_newsletter = True
is_on = False
```

### Flotante (float)

Los floats describen numeros de punto flotante con uno o mas lugares decimales.

```python
pi = 3.14159
average_score = 65.55
```

---

## Leccion 2: Conversion de tipos

Python tiene funciones integradas para convertir tipos de datos. Podemos obtener el tipo de una variable usando `type()`.

```python
is_ready = True
print(type(is_ready))  # <class 'bool'>
```

### Funcion int()

Convierte un valor a entero. Si se aplica a un float, elimina el decimal sin redondear. Si se aplica a un booleano, `True` equivale a `1` y `False` a `0`.

```python
converted_age = int("17")   # str -> int
print(int(9.99))            # 9, no redondea
print(int(True))            # 1
print(int(False))           # 0
```

### Funcion float()

Convierte un valor a flotante, anadiendo un punto decimal.

```python
weeks = 12
print(float(weeks))  # 12.0
```

### Funcion str()

Convierte valores numericos a cadena.

```python
password = 980790
print(str(password) == "81k29")  # False
```

### Funcion bool()

Convierte un valor a booleano. Si la variable tiene contenido, el resultado es `True`. Si esta vacia o es `0`, el resultado es `False`.

```python
bool("Sam")   # True
bool("")      # False
bool(8.5)     # True
bool(0)       # False
```

---

## Ejercicios

| Archivo | Descripcion |
|---|---|
| ejercicio_01_tipo_entero.py | Tipo entero: score = 42 |
| ejercicio_02_tipo_cadena.py | Tipo cadena: sugar_content = "High" |
| ejercicio_03_tipo_booleano.py | Tipo booleano: received_newsletter = True |
| ejercicio_04_asignacion_false.py | Asignacion de False a variable |
| ejercicio_05_tipo_float.py | Tipo flotante: pi = 3.14159 |
| ejercicio_06_practica_cadena.py | Practica: guardar cadena en name |
| ejercicio_07_practica_entero.py | Practica: guardar entero en minutes_left |
| ejercicio_08_practica_float.py | Practica: guardar float en average_score |
| ejercicio_09_practica_tres_tipos.py | Practica: asignar cadena, entero y booleano |
| ejercicio_10_practica_appearances.py | Practica: asignar 11 a number_of_appearances |
| ejercicio_11_type.py | Funcion type() con booleano |
| ejercicio_12_type_multiples.py | Funcion type() con multiples tipos |
| ejercicio_13_int_conversion.py | int() convierte cadena a entero |
| ejercicio_14_int_desde_float.py | int() en float elimina decimal sin redondear |
| ejercicio_15_tipo_para_comparar.py | Tipo entero necesario para comparar con < |
| ejercicio_16_str_conversion.py | str() convierte entero a cadena |
| ejercicio_17_float_conversion.py | float() convierte entero a flotante |
| ejercicio_18_int_desde_bool.py | int() en booleano: True=1, False=0 |
| ejercicio_19_bool_conversion.py | bool() segun contenido de la variable |
| ejercicio_20_practica_bool.py | Practica: bool() con pets y kids |
| ejercicio_21_practica_bool_cadena.py | Practica: bool() con cadena detail |
| ejercicio_22_practica_int_float.py | Practica: int() en float trunca sin redondear |
